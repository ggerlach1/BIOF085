#!/bin/sh

## This script is targeted at Mac OS where sed -i requires a target
sed -i '' '/^</d' *.Rmd
