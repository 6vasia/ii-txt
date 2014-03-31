#!/bin/sh

cd .py
cat bbs.bbs
> .newmsg
python wf.py
python reparse.py
python newmsg.py
cd ..