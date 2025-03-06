import sys
from pathlib import Path

import docint
import orgpedia  # noqa: F401

if __name__ == "__main__":
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    viz = docint.load("src/buildOrder.yml")

    if input_path.is_dir():
        assert output_path.is_dir()
        input_files = list(input_path.glob("*.annotfirst.json"))

        docs = viz.pipe_all(input_files)

        for doc in docs:
            output_doc_path = output_path / (doc.pdf_name + ".order.json")
            doc.to_disk(output_doc_path)
    else:
        doc = viz(input_path)
        doc.to_disk(output_path)
