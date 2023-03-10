.DEFAULT_GOAL := help

org_code := cabsec

tasks := doOcr_ annotateFirst_ buildOrder/manual_ buildOrder/para_ buildOrder/list_ buildOrder/table_ buildTenure_
tasks := $(foreach t,$(tasks),flow/$t)


.PHONY: help install import flow export check readme lint format pre-commit $(tasks)

help:
	$(info Please use 'make <target>', where <target> is one of)
	$(info )
	$(info   install     install packages and prepare software environment)
	$(info )
	$(info   import      import data required for processing document flow)
	$(info   flow        execute the tasks in the document flow)
	$(info   export      export the data generated by the document flow)
	$(info )
	$(info   check       check if files are correctly laid in the flow directory)
	$(info   readme      generate the readme for the flow/task directories)
	$(info )
	$(info   lint        run the code linters)
	$(info   format      reformat code)
	$(info   pre-commit  run pre-commit checks, runs yaml lint, you need pre-commit)
	$(info )
	$(info Check the makefile to know exactly what each target is doing.)
	@echo # dummy command

install: pyproject.toml
	poetry install --only=dev

import:
	poetry run op importall import/

flow: $(tasks)
$(tasks):
	poetry run make -C $@

check:
	poetry run op check > export/logs/info.check.log

readme:
	poetry run op readme > export/logs/info.readme.log

lint:
	poetry run black -q .
	poetry run ruff .

format:
	poetry run black -q .
	poetry run ruff --fix .

export: format lint check readme
	poetry run op exportpackage export/data export/orgpedia_$(org_code)
	poetry build
#	poetry publish

# Use pre-commit if there are lots of edits,
# https://pre-commit.com/ for instructions
# Also set git hook `pre-commit install`
pre-commit:
	pre-commit run --all-files

