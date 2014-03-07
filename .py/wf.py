# -*- coding: utf-8 -*-

import urllib

def getf(l):
    print 'fetch %s' % l
    return urllib.urlopen(l).read()

def get_echoarea(name):
    try:
        return open('echo/%s' % name).read().splitlines()
    except:
        return ''

def filter_urls(my,out):
    nmy = my[:]
    for n in out:
        if not n in my:
            out = getf('%sm/%s' % (cfg[1], n))
            if out:
                open('msg/%s' % n,'w').write(out)
                nmy.append(n)
    return nmy


cfg = open('../config.cfg').read().splitlines()

for ea in cfg[2:]:
    my = get_echoarea(ea) or []
    out = getf('%se/%s' % (cfg[1], ea))
    if '<' in out: 
        print 'url broken!'
    else:
        nmy = filter_urls(my,out.splitlines())
        buf = '\n'.join(nmy)
        open('echo/%s' % ea, 'w').write(buf)
