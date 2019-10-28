#!/usr/bin/python

import os, base64, datetime

repo ='apps/it.murah.cx.app.farmacia/f/repo'

now = datetime.datetime.now()
output = 'images-' + now.strftime("%b-%d-%Y_%H-%M-%S")

os.mkdir(output)

for r, d, f in os.walk(repo):
    for file in f:
        fh = open(os.path.join(repo,file),'r')
        wh = open(os.path.join(output,file+'.jpeg'),'w')
        wh.write(base64.b64decode(fh.read()))
        fh.close()
        wh.close()
