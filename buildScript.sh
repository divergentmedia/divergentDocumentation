#!/bin/bash


BASEPATH=$1

cd $1

pandoc -B coverpage.tex -s -S --toc -V documentclass=report --template=../pandocTemplates/customTemplate.tex --variable fontsize=12pt $BASEPATH.md --latex-engine=xelatex -o ../output/$BASEPATH.pdf
pandoc -s -S --template=../pandocTemplates/htmlTemplate --toc $BASEPATH.md -o ../output/$BASEPATH.html
