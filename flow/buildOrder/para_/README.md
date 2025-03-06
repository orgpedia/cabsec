# Task: buildOrder/para_

This folder(task) handles documents with paragraphs, uses ner model to mark person and custom post finder

| Directory    | Files                          | Counts |
|--------------|--------------------------------|--------|
| input        | *.pdf.annotfirst.json          |    209 |
| output       | *.pdf.order.json               |    209 |
| intermediate | *.pdf.orderdetails.json         |    209 |
| conf         | *.bodymarker.yml[30], *.wordfix.yml[53], *.orderbuilder.yml[21], *.ordertagger.yml[26] |    130 |

## Skipped Documents

## Sub Tasks
There are 7 sub_tasks.

### body_marker
    Errors: 0 []
    Edits: 53 [clearWords: 12, newWord: 4, addWordIdxs: 1, replaceStr: 24, clearChar: 2, mergeWords: 10]
    Conf Files: 30

### para_fixer
    Errors: 0 []
    Edits: 92 [replaceStr: 45, mergeWords: 27, clearWords: 20]
    Conf Files: 53

### post_parser_onsentence
    Errors: 8 [PostMismatch: 8]
    Edits: 0 []
    Conf Files: 0

### order_builder
    Errors: 2 [UnmatchedTexts: 2]
    Edits: 0 []
    Conf Files: 21

### order_tagger
    Errors: 0 []
    Edits: 3 [mergeWords: 2, replaceStr: 1]
    Conf Files: 26

### id_assigner_vocab
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### details_differ
    Errors: 1 [PostIDDiff: 1]
    Edits: 0 []
    Conf Files: 0


---
*This file is auto-generated from [src/buildOrder.yml](src/buildOrder.yml), and by adding edits and errors from json files in the output directory.*
