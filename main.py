#!/usr/bin/python
import  asciiMovie
import os,sys,math,time,copy,random

tS=0.01

a=asciiMovie.asciiMovie(40,160)
a.addEmptyObj()
a.loadFile('data/0.txt',0,40,1,0,'cur')

#Frame 1  Title ############################
a.addEmptyObj()
a.loadFile('data/0101.txt',0,40,1,1,'end')
for i in range(0,1315):
    nr=random.random()*50-50; nc=random.random()*150+5
    a.addPoint('cur',1,'#',nr,nc,0,0,0,0)

for step in range(0,150):
    a.clearBuf()
    a.mixText(1,1)
    a.runCommon(1)
    a.addToBuf(1)
    a.addToBuf(0)
    a.showBuf()
    time.sleep(tS)

a.addVec1(1,-2,0,0,0)
for step in range(0,50):
    a.clearBuf()
    a.runCommon(1)
    a.addToBuf(1)
    a.addToBuf(0)
    a.showBuf()
    time.sleep(tS)


a.delAllObj()
a=asciiMovie.asciiMovie(40,160)
a.addEmptyObj()
a.loadFile('data/0.txt',0,40,1,0,'cur')

#Frame 2  Winter,Know #############################
a.addEmptyObj()
a.loadFile('data/0201.txt',0,40,1,1,'cur')
a.move(1,-50,0)
a.addVec1(1,1,0,0,0)

for step in range(0,50):
    a.clearBuf()
    a.runCommon(1)
    a.addToBuf(1)
    a.addToBuf(0)
    a.showBuf()
    time.sleep(tS)
a.addVec1(1,0,0,0,0)
    
a.addEmptyObj()
a.loadFile('data/0202.txt',0,40,1,2,'cur')#shoes
a.bubble(2,0,-4,'init')

a.addEmptyObj()
a.loadFile('data/0203.txt',0,1000,1,3,'cur')#snow
a.move(3,-360,0)

for step in range(0,120):
    a.clearBuf()
    a.snow(3,1,3)
    a.bubble(2,0,-4,'end')
    a.runCommon(2)
    a.runCommon(3)
    a.addToBuf(0)
    a.addToBuf(1)
    a.addToBuf(2)
    a.addToBuf(3)
    a.showBuf()
    time.sleep(tS)
 
for step in range(0,50):
    a.clearBuf()
    a.snow(3,1,3)
    a.bubble(2,0,-4,'end')
    a.shadeHide(1,20); a.shadeHide(2,20); a.shadeHide(3,30)
    a.runCommon(2)
    a.runCommon(3)
    a.addToBuf(0)
    a.addToBuf(1)
    a.addToBuf(2)
    a.addToBuf(3)
    a.showBuf()
    time.sleep(tS)

a.delAllObj()
a=asciiMovie.asciiMovie(40,160)
a.addEmptyObj()
a.loadFile('data/0.txt',0,40,1,0,'cur')

#Frame 3: QQ #######################################

a.addEmptyObj()
a.loadFile('data/0301.txt',0,40,1,1,'cur')#title
a.move(1,0,100)
a.addVec1(1,0,-2,0,0)

a.addEmptyObj()
a.loadFile('data/0302.txt',0,40,1,2,'cur')#qqWindow

a.addEmptyObj()
a.loadFile('data/0303.txt',0,40,1,3,'begin')#QQtext

for step in range(0,45):
    a.clearBuf()
    a.runCommon(1)
    a.addToBuf(0)
    a.addToBuf(1)
    a.addToBuf(2)
    a.showBuf()
    time.sleep(tS)
for step in range(0,100):
    a.clearBuf()
    a.lineShow(3,2)
    a.addToBuf(0)
    a.addToBuf(1)
    a.addToBuf(2)
    a.addToBuf(3)
    a.showBuf()
    time.sleep(tS)

for step in range(0,50):
    a.clearBuf()
    a.shadeHide(1,20); a.shadeHide(2,20); a.shadeHide(3,10)
    a.addToBuf(0)
    a.addToBuf(1)
    a.addToBuf(2)
    a.addToBuf(3)
    a.showBuf()
    time.sleep(tS)

a.delAllObj()
a=asciiMovie.asciiMovie(40,160)
a.addEmptyObj()
a.loadFile('data/0.txt',0,40,1,0,'cur')

#Frame 4:tucao love ################################



