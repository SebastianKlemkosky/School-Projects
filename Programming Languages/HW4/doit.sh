#!/bin/bash

for i in {1..7}; do
  echo ========= mmm$i
  gcc -Wall mmm$i.c -o /tmp/mmm$i
  /tmp/mmm$i 34 82 -4 -22 13 -83 0 3
done

echo ========= python
python3 mmm.py 34 82 -4 -22 13 -83 0 3
