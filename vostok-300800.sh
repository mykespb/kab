#!/bin/bash

mkdir t
mkdir g

#mv *.JPG $.jpg
for f in $( ls *.JPG ); do
#    echo $f
    tgt=$(echo $f | sed -e "s/JPG$/jpg/")
    echo $f $tgt
    mv $f $tgt
done

cp *.jpg t
cp *.jpg g

pushd t
for fname in *.jpg; do mogrify -resize 300 $fname; done
popd

pushd g
for fname in *.jpg; do mogrify -resize 800 $fname; done
popd 

