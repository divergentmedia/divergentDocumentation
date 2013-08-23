#!/bin/bash

pandoc -B coverpage.tex -s -S --toc -V documentclass=report --template=customTemplate.tex --variable fontsize=12pt Clipwrap.md --latex-engine=xelatex -o ClipWrap.pdf