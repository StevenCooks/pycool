# Makefile for unittests
#

TESTSDIR = tests

.PHONY: test
test:
	python -m unittest discover $(TESTSDIR)

.PHONY: coverage
coverage:
	coverage run -m unittest discover $(TESTSDIR)

