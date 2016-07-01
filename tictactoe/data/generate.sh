#!/bin/bash

while read line; do
    for i in `seq 1 7`;
    do
        echo "$line" | sed "s/0/x/$i" >> weights_3
    done
done <weights_2
