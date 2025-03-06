import base64
import datetime
import hashlib
import json
import sys
from pathlib import Path

import pydantic
from docint.pipeline.meta_writer import DocMeta
from docint.util import read_config_from_disk
from waybackpy import WaybackMachineCDXServerAPI, WaybackMachineSaveAPI, exceptions

# TODO
# 1. Multiple modes of execution 1) Get archive URL 2) Compare SHA 3) Upload if not present
# 2. Add functionality for upload if not present ( need asynchronous way of doing this)
# 3. ALlow retries for downloading the document with proper timeout (requests library).


class ArchiveInfo(pydantic.BaseModel):
    url: str
    archive_url: str
    content_url: str
    archive_time: datetime.datetime
    archive_sha1: str
    archive_status_code: str
    archive_length: int
    archive_mimetype: str


class WaybackArchive:
    UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'  # noqa

    def get_content_url(self, archive_url):
        url_pos = archive_url[6:].index('https:') + len('https:') - 1
        content_url = archive_url[:url_pos] + 'id_' + archive_url[url_pos:]
        return content_url

    def get_archive_info(self, url: str, age: str):
        assert age in ('newest', 'oldest')

        cdx_api = WaybackMachineCDXServerAPI(url, self.UserAgent)

        try:
            newest = cdx_api.newest() if age == 'newest' else cdx_api.oldest()
        except (exceptions.NoCDXRecordFound, ConnectionResetError) as e:  # noqa
            print(f'Unable to find {url} in wayback')
            return None

        content_url = self.get_content_url(newest.archive_url)
        return ArchiveInfo(
            url=url,
            archive_url=newest.archive_url,
            content_url=content_url,
            archive_time=newest.datetime_timestamp,
            archive_sha1=newest.digest,
            archive_status_code=newest.statuscode,
            archive_length=newest.length,
            archive_mimetype=newest.mimetype,
        )

    def save_url(self, url: str):
        save_api = WaybackMachineSaveAPI(url, user_agent=self.UserAgent)
        save_api.save()
        print(f'SAVED: {save_api.archive_url}')
        # do get_archive_info after saving, as save_api does not contain sha and other info


def main():
    input_dir = Path(sys.argv[1])

    urls_yaml = Path('conf/documents.yml')
    archive_json = Path('conf/urls.archive.json')

    yml_dict = read_config_from_disk(urls_yaml)
    urls_dict = {}
    for (pdf_repo_path, pdf_info) in yml_dict.items():
        pdf_path = Path(pdf_repo_path)
        pdf_name = pdf_info.get('name', pdf_path.name)
        urls_dict[pdf_name] = (pdf_info['url'], pdf_info['download_time'], pdf_repo_path)

    if archive_json.exists():
        archive_dict = json.loads(archive_json.read_text())
    else:
        archive_dict = {}

    wayback_archive = WaybackArchive()

    for input_pdf in input_dir.glob('*.pdf'):
        doc_meta = archive_dict.get(input_pdf.name, None)
        (url, download_time, pdf_repo_path) = urls_dict[input_pdf.name]
        if not doc_meta:

            with open(input_pdf, 'rb') as f:  # noqa
                h = hashlib.sha1(open(input_pdf, 'rb').read())
                pdf_digest = base64.b32encode(bytearray(h.digest())).decode('utf-8')

            archive_info = None
            for age in ['oldest', 'newest']:
                archive_info = wayback_archive.get_archive_info(url, 'oldest')
                if not archive_info:
                    print(f'{url}: NOT FOUND in the archive.')
                    break
                elif archive_info.archive_sha1 == pdf_digest:
                    doc_meta = DocMeta(
                        url=url,
                        pdf_repo_path=str(pdf_repo_path),
                        download_time=download_time,
                        archive_url=archive_info.archive_url,
                        archive_time=archive_info.archive_time,
                        archive_sha=pdf_digest,
                        archive_status_code=archive_info.archive_status_code,
                        sha_matched=True,
                    )
                    archive_dict[input_pdf.name] = doc_meta
                    archive_json.write_text(
                        json.dumps(archive_dict, default=pydantic.json.pydantic_encoder)
                    )

                    print(f'{input_pdf.name}: {age} sha1 MATCHED.')
                    break
                else:
                    sha1 = archive_info.archive_sha1
                    print(f'{input_pdf.name}: {age} sha1 did not match. {pdf_digest} -> {sha1}')
            # end for

            if not archive_info:
                print(f'Uploading the url {url}')
                wayback_archive.save_url(url)
            elif input_pdf.name not in archive_dict and archive_info:
                doc_meta = DocMeta(
                    url=url,
                    pdf_repo_path=str(pdf_repo_path),
                    download_time=download_time,
                    archive_url=archive_info.archive_url,
                    archive_time=archive_info.archive_time,
                    archive_sha=archive_info.archive_sha1,
                    archive_status_code=archive_info.archive_status_code,
                    sha_matched=False,
                )
                archive_dict[input_pdf.name] = doc_meta
                archive_json.write_text(
                    json.dumps(archive_dict, default=pydantic.json.pydantic_encoder)
                )
        else:
            pass


if __name__ == '__main__':
    main()
