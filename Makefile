# Makefile for unittests
.PHONY: test

test:
	coverage run -m unittest discover tests

