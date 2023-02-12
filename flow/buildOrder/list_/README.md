# Task: buildOrder/list_

This folder(task) handles documents with lists, finds numbers and lines and then lists. It runs ner on lists.

| Directory    | Files                          | Counts |
|--------------|--------------------------------|--------|
| input        | *.pdf.annotfirst.json          |    306 |
| output       | *.pdf.order.json               |    306 |
| intermediate | *.pdf.orderdetails.json         |    306 |
| conf         | *.findnum.yml[193], *.linefinder.yml[15], *.wordfix.yml[91], *.orderbuilder.yml[58], *.ordertagger.yml[26], *.id_assigner.yml[10] |    393 |

## Skipped Documents

## Sub Tasks
There are 10 sub_tasks.

### num_marker
    Errors: 16 [MarkerMisalgined: 16]
    Edits: 680 [replaceStr: 354, clearWords: 153, newWord: 129, mergeWords: 27, clearChar: 17]
    Conf Files: 193

### rotation_detector
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### line_finder
    Errors: 0 []
    Edits: 0 []
    Conf Files: 15

### list_finder2
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### para_fixer
    Errors: 0 []
    Edits: 557 [replaceStr: 317, mergeWords: 169, clearWords: 70, newWord: 1]
    Conf Files: 91

### post_parser_onsentence
    Errors: 23 [PostEmpty: 14, PostMismatch: 9]
    Edits: 0 []
    Conf Files: 0

### order_builder
    Errors: 46 [UnmatchedTexts: 46]
    Edits: 8 [mergeWords: 3, replaceStr: 5]
    Conf Files: 58

### order_tagger
    Errors: 0 []
    Edits: 16 [mergeWords: 4, replaceStr: 10, newWord: 2]
    Conf Files: 26

### id_assigner_vocab
    Errors: 0 []
    Edits: 0 []
    Conf Files: 10

### details_differ
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0


---
*This file is auto-generated from [src/buildOrder.yml](src/buildOrder.yml), and by adding edits and errors from json files in the output directory.*
