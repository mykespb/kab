#!/bin/bash

ref='2018-03-31-happy'

./mk-mkmeet.py $ref.txt
mv $ref.html $ref-3.html
./mk-mkmeet1k.py $ref.txt
mv $ref.html $ref-1.html

