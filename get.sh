#!/bin/sh

cd .py
cat bbs.bbs
python wf.py
python reparse.py
cd ..