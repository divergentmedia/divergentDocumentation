#!/bin/sh

echo "lets build a manual"

ASSETS_PATH="assets"
HTML_EXTRAS_PATH="htmlextras"
TOOLCHAIN_PATH="toolchain"
DATE_SEED=$(date +%s)
TMP_PATH="/tmp/manualmaker$DATE_SEED"

echo "making deriveddata folder at $TMP_PATH"

mkdir $TMP_PATH
perl $TOOLCHAIN_PATH/Markdown_1.0.1/Markdown.pl --html4tags $1 > $TMP_PATH/markdownbody.html
cp -R $ASSETS_PATH/* $TMP_PATH

cat $ASSETS_PATH/$HTML_EXTRAS_PATH/pre.html $TMP_PATH/markdownbody.html $ASSETS_PATH/$HTML_EXTRAS_PATH/post.html > $TMP_PATH/fullmanual.html
exit 0;
$TOOLCHAIN_PATH/wkhtmltopdf toc --xsl-style-sheet $TMP_PATH/pdfextras/toc.xsl page $TMP_PATH/fullmanual.html --header-html $TMP_PATH/pdfextras/header.html --footer-html $TMP_PATH/pdfextras/footer.html $2

exit 0