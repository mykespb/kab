#!/bin/bash

for fname in *.jpg; do mogrify -resize 800 $fname; done
for fname in *.JPG; do mogrify -resize 800 $fname; done