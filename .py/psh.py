# -*- coding: utf-8 -*-

import urllib,sys,os

def getf(l):
    print 'fetch %s' % l
    return urllib.urlopen(l).read()

cfg = open('../config.cfg').read().splitlines()

website = '%sz/push' % cfg[1]
auth = cfg[0]

for ml in sys.argv[1:]:
    txt = open(ml).read()
    out = getf('%s/%s/%s' % (website, auth, txt))
    os.remove(ml)
