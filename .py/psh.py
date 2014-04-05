# -*- coding: utf-8 -*-

import urllib,sys,os
cfg = open('../config.cfg').read().splitlines()

def postf(s):
    data = urllib.urlencode({'tmsg': s,'pauth': cfg[0]})
    #{"Content-type": "application/x-www-form-urlencoded"}
    u = urllib.urlopen(cfg[1] + 'point', data)
    return u.read()

for ml in sys.argv[1:]:
    txt = open(ml).read()
    out = postf(txt)
    if out.startswith('msg ok'):
        os.remove(ml)
    elif out == 'msg big!':
        print 'ERROR: very big message (limit: 64k)!'
    elif out == 'auth error!':
        print 'ERROR: AUTH!'
    else:
        print 'ERROR: WHY?'
