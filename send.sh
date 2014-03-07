#!/bin/sh

cd .py
python findnew.py
python mkt.py ../.out/*.out
python psh.py ../.out/*.toss
cd ..