# -*- coding: utf-8 -*-

import codecs, os

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

f = codecs.open('../newmsg.txt','w','utf-8')
for m in open('.newmsg').read().splitlines():
    mo = _parz(codecs.open('msg/%s' % m,'r','utf-8').read())
    buf = m + '\n' + mo['msgfrom'] + ' (' + str(mo['addr']) + ')\nmsgto: ' + mo['msgto'] + '\n' + mo['subj'] + '\n\n' + mo['msg']
    f.write('== %s ========================= ' % mo['echoarea'] + buf + '\n\n\n')
f.close()
