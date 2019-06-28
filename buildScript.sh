#!/bin/bash

BASEPATH=$1

docker run --volume "`pwd`:/data" dmpandoc:latest -B $BASEPATH/coverpage.tex -s --toc -V documentclass=report  --template=pandocTemplates/customTemplate.tex --variable fontsize=12pt -f markdown+smart $BASEPATH/$BASEPATH.md --pdf-engine=xelatex -o "output/$BASEPATH Manual.pdf"
docker run --volume "`pwd`:/data" dmpandoc:latest -s -f markdown-smart  --template=pandocTemplates/htmlTemplate --toc $BASEPATH/$BASEPATH.md -o output/$BASEPATH.html
