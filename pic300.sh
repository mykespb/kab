#!/bin/bash

for fname in *.jpg; do mogrify -resize 300 $fname; done
for fname in *.JPG; do mogrify -resize 300 $fname; done