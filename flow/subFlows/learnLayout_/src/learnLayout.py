import sys
from pathlib import Path

import docint

if __name__ == '__main__':
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    input_files = list(input_dir.glob('*.json'))

    viz = docint.load('src/learnLayout.yml')
    docs = viz.pipe_all(input_files)
    for doc in docs:
        output_doc_path = output_dir / (doc.pdf_name + '.layout.json')
        doc.to_disk(output_doc_path)
