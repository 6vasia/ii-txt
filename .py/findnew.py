# -*- coding: utf-8 -*-

import codecs, os

def outcount():
    i = str(int(open('../.out/.counter').read())+1)
    open('../.out/.counter','w').write( i )
    return '../.out/%s.out' % i

cfg = open('../config.cfg').read().splitlines()

for ea in cfg[2:]:
    lst = [x for x in os.listdir('../%s' % ea) if 'new' in x]
    for fmsg in lst:
        new = codecs.open('../%s/%s' % (ea,fmsg),'r','utf-8').read().splitlines()
        header = new[:new.index('')]
        if len(header) == 2:
            buf = [ea] + new
        elif len(header) == 3:
            buf = [ea] + new[1:4] + ['@repto:%s' % new[0]] + new[4:]
        codecs.open(outcount(),'w','utf-8').write( '\n'.join(buf) )
        os.remove('../%s/%s' % (ea,fmsg))
