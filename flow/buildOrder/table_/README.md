# Task: buildOrder/table_

Builds orders from documents containing tables, uses numbers on the left to form lists and then builds table and then an order.

| Directory    | Files                          | Counts |
|--------------|--------------------------------|--------|
| input        | *.pdf.annotfirst.json          |    282 |
| output       | *.pdf.order.json               |    273 |
| intermediate | *.pdf.linefinder.json           |    273 |
| intermediate | *.pdf.orderdetails.json         |    273 |
| conf         | *.findnum.yml[237], *.table_finder.yml[12], *.tableorder.yml[77], *.ordertagger.yml[46], *.id_assigner.yml[61] |    433 |

## Skipped Documents
1. [1_Upload_1990.pdf](/import/documents/1_Upload_1990.pdf):  Lot of dirty text,  two orders 1 of resignation and 1 of assumption, IMPORTANT
2. [1_Upload_2686.pdf](/import/documents/1_Upload_2686.pdf):  Faded paper unable to read
3. [1_Upload_2811.pdf](/import/documents/1_Upload_2811.pdf):  Hindi Department
4. [1_Upload_2812.pdf](/import/documents/1_Upload_2812.pdf):  Hindi Department / English Department
5. [1_Upload_2910.pdf](/import/documents/1_Upload_2910.pdf):  Black scan, with lots of mistakes
6. [1_Upload_2431.pdf](/import/documents/1_Upload_2431.pdf):  Reversed Department followed by name
7. [1_Upload_2290.pdf](/import/documents/1_Upload_2290.pdf):  dirty pdf
8. [1_Upload_2412.pdf](/import/documents/1_Upload_2412.pdf):  dirty pdf
9. [1_Upload_937.pdf](/import/documents/1_Upload_937.pdf):  dirty pdf

## Sub Tasks
There are 9 sub_tasks.

### num_marker
    Errors: 39 [MarkerMisalgined: 39]
    Edits: 2,439 [clearWords: 261, replaceStr: 1150, newWord: 674, newAdjWord: 31, mergeWords: 303, splitWord: 5, clearChar: 15]
    Conf Files: 237

### rotation_detector
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### line_finder
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### list_finder2
    Errors: 0 []
    Edits: 0 []
    Conf Files: 0

### table_finder
    Errors: 0 []
    Edits: 0 []
    Conf Files: 12

### table_order_builder
    Errors: 1,047 [UnmatchedTexts: 922, EnglishWordsInName: 93, IncorrectOfficerName: 14, OrderDateNotFound: 16, TableEmptyBodyCell: 2]
    Edits: 28 [mergeWords: 11, clearWords: 2, replaceStr: 15]
    Conf Files: 77

### order_tagger
    Errors: 0 []
    Edits: 0 []
    Conf Files: 46

### id_assigner_vocab
    Errors: 1 [OfficerIDNotFound: 1]
    Edits: 0 []
    Conf Files: 61

### details_differ
    Errors: 1 [OrderDateDiff: 1]
    Edits: 0 []
    Conf Files: 0


---
*This file is auto-generated from [src/buildOrder.yml](src/buildOrder.yml), and by adding edits and errors from json files in the output directory.*
