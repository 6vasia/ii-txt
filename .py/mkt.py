# -*- coding: utf-8 -*-

import sys, zlib, base64, os

for f in sys.argv[1:]:
    tx = open(f).read()
    ctx = base64.urlsafe_b64encode( zlib.compress(tx,9) )
    open(f + '.toss','w').write(ctx)
    os.rename(f,f+'msg')