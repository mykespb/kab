#!/bin/bash

for fname in *.jpg; do mogrify -resize 200 $fname; done
for fname in *.JPG; do mogrify -resize 200 $fname; done