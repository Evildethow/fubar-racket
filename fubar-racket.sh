#!/usr/bin/env bash

python playlist.py > out.txt

count=0
while read line
do
    printf "[${count}] ${line}\n"
    let count=$count+1
done <out.txt

echo "Enter song number:"
read SONG

count=0
while read line
do
    if [ ${count} -eq ${SONG} ]; then
      mpsyt .${line}, 1 &
      #wait
      #mpsyt q
    fi
    let count=$count+1
done <out.txt

rm -f out.txt
