# -*- coding: utf-8 -*-

import codecs, os, time

def get_echoarea(name):
    try:
        return open('echo/%s' % name).read().splitlines()
    except:
        return ''

def dateg(d,f):
    return time.strftime(f, time.gmtime(int(d)))

def _parz(msg):
    pz = msg.splitlines()
    mo = dict()
    optz = pz[0].split('/')
    mo.update( dict(zip(optz[::2],optz[1::2])) )
    for i,n in enumerate(('echoarea','date','msgfrom','addr','msgto','subj'),1):
        mo[n] = pz[i]
    mo['msg'] = '\n'.join(pz[8:])
    mo['date'] = int(mo['date'])
    return mo


cfg = open('../config.cfg').read().splitlines()

for ea in cfg[2:]:
    if not os.path.exists('../%s' % ea):
        os.makedirs('../%s' % ea)
    my = get_echoarea(ea) or []
    f = codecs.open('../%s/0000.txt' % ea,'w','utf-8')
    for i,m in enumerate(my,1):
        mo = _parz(codecs.open('msg/%s' % m,'r','utf-8').read())
        sdate = dateg(mo['date'],'%d/%m %H:%M')
        buf = m + '\n' + mo['msgfrom'] + ' (' + str(mo['addr']) + ') (' + sdate + ' GMT)\nmsgto: ' + mo['msgto'] + '\n' + mo['subj'] + '\n\n' + mo['msg']
        codecs.open('../%s/%s.txt' % (ea,i),'w','utf-8').write(buf)
        f.write('== %s ========================= ' % i + buf + '\n\n\n')
    f.close()
