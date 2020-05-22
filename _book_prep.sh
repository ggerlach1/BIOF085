#!/bin/sh


for f in dev/0*.Rmd
do
  sed '/^</d' $f > ${f/dev/book}
done
cp -r dev/data book
cp -r dev/graphs book
cd book
Rscript -e 'bookdown::render_book("index.Rmd", "bookdown::gitbook")'
