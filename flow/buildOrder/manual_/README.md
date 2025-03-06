# Task: buildOrder/manual_

This folder(task) manually tags difficult to parse documents.

| Directory    | Files                          | Counts |
|--------------|--------------------------------|--------|
| input        | *.pdf.annotfirst.json          |     26 |
| output       | *.pdf.order.json               |     26 |
| intermediate | *.pdf.orderdetails.json         |     26 |
| conf         | *.ordertagger.yml[26]          |     26 |

## Skipped Documents

## Sub Tasks
There are 3 sub_tasks.

### order_tagger
    Errors: 0 []
    Edits: 33 [replaceStr: 14, mergeWords: 17, newWord: 1, addWordIdxs: 1]
    Conf Files: 26

### id_assigner_vocab
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### details_differ
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0


---
*This file is auto-generated from [src/buildOrder.yml](src/buildOrder.yml), and by adding edits and errors from json files in the output directory.*
