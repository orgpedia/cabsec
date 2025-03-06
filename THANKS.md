# Thanks ...
Orgpedia would like thank the following organizations, projects and people - by offering their services, software, date free of cost they have made Orgpedia possible - eternally grateful.

## Services
1. [GitHub](https://www.github.com/): All the code is hosted on GitHub and we plan to use the entire gamut of features it offers from GitHub Actions to GitHub Codespaces. The [www.orgpedia.in](www.orgpedia.in) site is also hosted on GitHub Pages.

2. [Google Cloudvision](https://cloud.google.com/vision): We use the Google Cloud OCR for extracting words from images, thanks for supporting all the main Indian languages and offering a very generious free tier and free trial.

3. [Cloudinary](https://cloudinary.com/): All the order images on the website are served from Cloudinary.

4. [Huggingface Hub](https://huggingface.co/): Hugging face hub is used to store and distrbute all the orgpedia models.

5. [Cloudflare Web Analytics](https://www.cloudflare.com/web-analytics/): Orgpedia uses Cloudflare's cookie-less web analytics for tracking the visitors on the website.

6. [Unpkg](https://unpkg.com/): Unpkg is used for hosting lunr.js the JS library for searching on the website.

## Data
1. [Cabinet Secretariat](https://cabsec.gov.in): Thanks to Cabinet Secratariat for making all the orders available on their website, starting from 1947 - to date.

2. [WikiData](http://www.wikidata.org) Orgpedia uses the wikidata ID for uniquely identifying an individual, also their data is used for translating names.

3. [Internet Archive - Wayback Machine](https://archive.org/web/): Orgpedia only processes the documents that are identitical the documents archived in the wayback machine. This service allows Orgpedia to isolate itself from ever-changing nature of the websites.

3. [LokSabha](): Thanks for providing images for all its members, both current past.

4. [RajyaSabha](): Thanks for providing images for all its members, both current past.

5. [Wikpedia](https://www.wikipedia.org): Thanks for making images available of ministers.

## Machine Learning Models:
1. [LayoutLMV2](https://huggingface.co/microsoft/layoutlmv2-base-uncased]): We use a fine tuned version of this model to identify the layout of the first page of the order and separate out useful information. Thanks to Hugging Face for providing an implementation and model hosting.

```
@inproceedings{Xu2020LayoutLMv2MP,
  title     = {LayoutLMv2: Multi-modal Pre-training for Visually-Rich Document Understanding},
  author    = {Yang Xu and Yiheng Xu and Tengchao Lv and Lei Cui and Furu Wei and Guoxin Wang and Yijuan Lu and Dinei Florencio and Cha Zhang and Wanxiang Che and Min Zhang and Lidong Zhou},
  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL) 2021},
  year      = {2021}
}
```

2. [Bert-base-NER](https://huggingface.co/dslim/bert-base-NER): We use this model as named-entity-recognizer, thanks to Hugging Face for providing an implementation and model hosting.
```
@article{DBLP:journals/corr/abs-1810-04805,
  author    = {Jacob Devlin and
               Ming{-}Wei Chang and
               Kenton Lee and
               Kristina Toutanova},
  title     = {{BERT:} Pre-training of Deep Bidirectional Transformers for Language
               Understanding},
  journal   = {CoRR},
  volume    = {abs/1810.04805},
  year      = {2018},
  url       = {http://arxiv.org/abs/1810.04805},
  archivePrefix = {arXiv},
  eprint    = {1810.04805},
  timestamp = {Tue, 30 Oct 2018 20:39:56 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1810-04805.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
@inproceedings{tjong-kim-sang-de-meulder-2003-introduction,
    title = "Introduction to the {C}o{NLL}-2003 Shared Task: Language-Independent Named Entity Recognition",
    author = "Tjong Kim Sang, Erik F.  and
      De Meulder, Fien",
    booktitle = "Proceedings of the Seventh Conference on Natural Language Learning at {HLT}-{NAACL} 2003",
    year = "2003",
    url = "https://www.aclweb.org/anthology/W03-0419",
    pages = "142--147",
}
```

## Translation Models/Services
1. [Google Translate](https://translate.google.co.in/): Google supports 19 of the 22 official indian languages.

2. [IndicTrans](https://github.com/libindic/indic-trans): We use this library for transliteration of names.
```
@inproceedings{Bhat:2014:ISS:2824864.2824872,
    author = {Bhat, Irshad Ahmad and Mujadia, Vandan and Tammewar, Aniruddha and Bhat, Riyaz Ahmad and Shrivastava, Manish}, 
    title = {IIIT-H System Submission for FIRE2014 Shared Task on Transliterated Search}, 
    booktitle = {Proceedings of the Forum for Information Retrieval Evaluation}, 
    series = {FIRE '14}, year = {2015}, isbn = {978-1-4503-3755-7}, location = {Bangalore, India}, pages = {48--53}, numpages = {6}, url = {http://doi.acm.org/10.1145/2824864.2824872}, 
    doi = {10.1145/2824864.2824872}, acmid = {2824872}, publisher = {ACM}, address = {New York, NY, USA},
    keywords = {Information Retrieval, Language Identification, Language Modeling, Perplexity, Transliteration}}
```
3. [Kashmiri, Santhali & Bodo](): These 3 languages are not supported by Google translate and a variety of resources were used for the translations and transliteration. More information can be found on this issue.

## Tools
1. [Python](http://www.python.org): Bulk of the code is written in Python, even the large chunk of the front-end.

2. [Unix/GNU Tools](https://en.wikipedia.org/wiki/GNU_toolchain): Lot of the pipelines are held with GNU tools like make, awk, shell, grep, tr.

2. [TailwindCSS](http://www.tailwindcss.com): We use tailwindCSS for stying the 

## Software
No software is distributed as a part of this package, but we have dependencies on this software.
