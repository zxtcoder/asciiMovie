#!/usr/bin/python

import os,sys,math,time,copy

class asciiMovie:
    def __init__(self,row,col):
        self.row=row; self.col=col
        self.objBegin=[];self.objEnd=[]; self.obj=[]
        self.buf=[]
        for i in range(0,row):
            self.buf.append([])
            for j in range(0,col):
                self.buf[-1].append(' ')
        
    def addEmptyObj(self):
        self.objBegin.append([])
        self.objEnd.append([])
        self.obj.append([])

    def loadFile(self,fname,beginL,endL,stepL,iobj,flag):
        fp=open(fname,'r')
        content=fp.readlines()
        for i in range(beginL,endL,stepL):
            if(content[i][-1]=='\n'):
                line=content[i][:-1]
            for j in range(0,self.col):
                if(j>=self.col or line[j]==' '):
                    continue
                nrow=(i-beginL)/stepL; ncol=j
                if(flag=='cur'):
                    self.obj[iobj].append([])
                    self.obj[iobj][-1].append(line[j])
                    self.obj[iobj][-1].append(nrow); self.obj[iobj][-1].append(ncol)
                    self.obj[iobj][-1].append(0); self.obj[iobj][-1].append(0)
                    self.obj[iobj][-1].append(0); self.obj[iobj][-1].append(0)
                if(flag=='begin'):
                    self.objBegin[iobj].append([])
                    self.objBegin[iobj][-1].append(line[j])
                    self.objBegin[iobj][-1].append(nrow); self.objBegin[iobj][-1].append(ncol)
                    self.objBegin[iobj][-1].append(0); self.objBegin[iobj][-1].append(0)
                    self.objBegin[iobj][-1].append(0); self.objBegin[iobj][-1].append(0)
                if(flag=='end'):
                    self.objEnd[iobj].append([])
                    self.objEnd[iobj][-1].append(line[j])
                    self.objEnd[iobj][-1].append(nrow); self.objEnd[iobj][-1].append(ncol)
                    self.objEnd[iobj][-1].append(0); self.objEnd[iobj][-1].append(0)
                    self.objEnd[iobj][-1].append(0); self.objEnd[iobj][-1].append(0)
        fp.close()

    def addVec1(self,iobj,vr,vc,ar,ac):
        for item in self.obj[iobj]:
            item[3]=vr; item[4]=vc; item[5]=ar; item[6]=ac

    def move(self,iobj,drow,dcol):
        for item in self.obj[iobj]:
            item[1]=item[1]+drow;
            item[2]=item[2]+dcol;
            

    def runCommon(self,iobj):
        for item in self.obj[iobj]:
            item[1]=item[1] + item[3]
            item[2]=item[2] + item[4]
            item[3]=item[3] + item[5]
            item[4]=item[4] + item[6]

    def addToBuf(self,iobj):
        for item in self.obj[iobj]:
            ch=item[0]; nrow=item[1]; ncol=item[2]
            if(nrow>=0 and nrow<self.row and ncol>=0 and ncol<self.col):
                self.buf[nrow][ncol]=ch

    def clearBuf(self):
        for i in range(0,self.row):
            for j in range(0,self.col):
                self.buf[i][j]=' '

    def showBuf(self):
        os.system('clear')
        for i in range(0,self.row):
            line=''.join(self.buf[i])
            print line


a=asciiMovie(40,100)
a.addEmptyObj()
a.loadFile('a.txt',0,40,1,0,'cur')
a.addVec1(0,1,0,0,0)
for i in range(0,40):
    a.clearBuf()
    a.runCommon(0)
    a.addToBuf(0)
    a.showBuf()
    time.sleep(0.5)
