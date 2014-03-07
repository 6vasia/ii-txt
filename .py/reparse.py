# -*- coding: utf-8 -*-

import json, codecs, os

def get_echoarea(name):
    try:
        return open('echo/%s' % name).read().splitlines()
    except:
        return ''

cfg = open('../config.cfg').read().splitlines()

for ea in cfg[2:]:
    if not os.path.exists('../%s' % ea):
        os.makedirs('../%s' % ea)
    my = get_echoarea(ea) or []
    f = codecs.open('../%s/0000.txt' % ea,'w','utf-8')
    for i,m in enumerate(my,1):
        mo = json.loads(open('msg/%s' % m).read())
        buf = m + '\n' + mo['msgfrom'] + '\naddr: ' + str(mo['addr']) + '\nmsgto: ' + mo['msgto'] + '\n' + mo['subj'] + '\n\n' + mo['msg']
        codecs.open('../%s/%s.txt' % (ea,i),'w','utf-8').write(buf)
        f.write('== %s ========================= ' % i + buf + '\n\n\n')
    f.close()
