# R script for building manual using bookdown

library(bookdown)

system('sh _book_prep.sh') # removes potential TOC in the Rmd files
render_book('index.Rmd', 'bookdown::gitbook')
# render_book('index.Rmd','bookdown::pdf_book') # PDF version of manual


# NOTE: There is an issue with reticulate 1.15, Mac OS 10.13 and greater, 
# SIP in the Mac OS, and the notarized version of R, which is preventing 
# us from running the reticulate python interpretor using Rscript or from the
# command line or from R running in a terminal. This compilation can currently
# only be done from within RStudio. 
# 
# See https://github.com/rstudio/reticulate/issues/758
# 
# Otherwise writing a Makefile or a shell script would be a better method. 
