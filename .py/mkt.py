# -*- coding: utf-8 -*-

import sys, base64, os

for f in sys.argv[1:]:
    tx = open(f).read()
    ctx = base64.b64encode( tx )
    open(f + '.toss','w').write(ctx)
    os.rename(f,f+'msg')