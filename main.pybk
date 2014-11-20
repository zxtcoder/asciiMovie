#!/usr/bin/python
import  asciiMovie
import os,sys,math,time,copy,random

a=asciiMovie.asciiMovie(40,160)
a.addEmptyObj()
a.loadFile('b.txt',0,40,1,0,'cur')

a.addEmptyObj()
a.loadFile('c.txt',0,40,1,1,'cur')
a.loadFile('c.txt',0,40,1,1,'end')

#for i in range(0,len(a.objEnd[1])):
#    nc=random.random()*160; nr=random.random()*40-50
#    a.addPoint('cur',1,chr(i%74+48),nr,nc,0,0,0,0)
#
#for i in range(0,200):
#    a.clearBuf()
#    a.mixText(1,1)
#    a.runCommon(1)
#    a.addToBuf(0)
#    a.addToBuf(1)
#    a.showBuf()
#    time.sleep(0.1)
#
#a.addVecRand(1,5)
#for i in range(0,400):
#    a.clearBuf()
#    a.runCommon(1)
#    a.addToBuf(0)
#    a.addToBuf(1)
#    a.showBuf()
#    time.sleep(0.1)

#a.stripeRow(1,5,'init')
#for i in range(0,200):
#    a.clearBuf()
#    a.runCommon(1)
#    a.stripeRow(1,5,'end')
#    a.addToBuf(1)
#    a.addToBuf(0)
#    a.showBuf()
#    time.sleep(0.1)

#for i in range(0,200):
#    a.clearBuf()
#    a.lineShow(1,5)
#    a.addToBuf(1)
#    a.addToBuf(0)
#    a.showBuf()
#    time.sleep(0.1)

a.bubble(1,-1,-5,'init')
for i in range(0,200):
    a.clearBuf()
    a.bubble(1,-1,-5,'end')
    a.runCommon(1)
    a.addToBuf(1)
    a.addToBuf(0)
    a.showBuf()
    time.sleep(0.1)


