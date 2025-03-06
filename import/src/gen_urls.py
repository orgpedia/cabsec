# This script takes the urls.txt and generates urls.yml file

"""
./changePort/1995/1_Upload_1595.pdf:
  url: https://cabsec.gov.in/writereaddata/changeinportfolio/english/1_Upload_1595.pdf
  download_time: 2021-08-30 14:12:22

"""


import sys
from pathlib import Path

urls_path = Path(sys.argv[1])
pdf_info = []
for line in urls_path.read_text().split('\n'):
    if line.startswith('.'):
        log_path = Path(line.strip())

    elif line.startswith('#'):
        continue

    elif line.startswith('--'):
        line = line.replace('(try: 2) ', '')
        line = line.replace('--', '')
        (d, t, url) = line.split()
        pdf_name = Path(url).name
        print(f'{str(log_path.parent / pdf_name)}:')
        print(f'  url: {url}')
        print(f'  download_time: {d} {t}')
        print()
