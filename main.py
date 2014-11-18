#!/usr/bin/python

import os,sys,math,time

class asciiMovie:
    def __init__(self,row,col):
        self.row=row; self.col=col
        self.objList0=[]; self.objList1=[]
        self.buf=[]
        for i in range(0,self.row):
            self.buf.append([])
            for j in range(0,self.col):
                self.buf[-1].append(' ')

    def newObj(self):
	self.objList0.append([])
	self.objList1.append([])
        for i in range(0,self.row):
            self.objList0[-1].append([])
            self.objList1[-1].append([])
            ##self.objList1[a][row0][col0]['a',row,col,vr,vc,ar,ac]
            for j in range(0,self.col):
                self.objList0[-1][-1].append(' ')
                self.objList1[-1][-1].append(' ')
                self.objList1[-1][-1].append(i); self.objList1[-1][-1].append(j)
                self.objList1[-1][-1].append(0); self.objList1[-1][-1].append(0)
                self.objList1[-1][-1].append(0); self.objList1[-1][-1].append(0)

    def addData(self,fname,iObj):
        fp=open(fname,'r')
        for i in range(0,self.row):
            line=fp.readline()[:-1]
            for j in range(0,self.col):
                if(j<len(line)):
                    self.objList0[iObj][i][j]=line[j]
                    self.objList1[iObj][i][j][0]=line[j]
                else:
                    self.objList0[iObj][i][j]=' '
                    self.objList1[iObj][i][j][0]=' '
        fp.close()

    def clearObj(self,iObj,flag):
         for i in range(0,self.row):
            for j in range(0,self.col):
                if(flag=='0'):
                    self.objList0[iObj][i][j]=' '
                if(flag=='1'):
                    self.objList1[iObj][i][j][0]=' '
                    for k in range(1,7):
                        self.objList1[iObj][i][j][k]=0
                if(flag=='a'):
                    self.objList0[iObj][i][j]=' '
                    self.objList1[iObj][i][j][0]=' '
                    for k in range(1,7):
                        self.objList1[iObj][i][j][k]=0

    def clearBuf(self):
        for i in range(0,self.row):
            for j in range(0,self.col):
                self.buf[i][j]=' '
        
    def show(self):
        os.system('clear')
        for line in self.buf:
            print ''.join(line)

    def addToBuf(self,iObj,flag):
        "flag=over/add"
        if(flag=='over'):
            self.clearBuf()
        for i in range(0,self.row):
            for j in range(0,self.col):
                nrow=self.obfList1[iObj][i][j][1]; ncol=self.obfList1[iObj][i][j][2]
                if(self.objList1[iObj][i][j][0]!=' '):
                    self.buf[nrow][ncol]=self.objList1[iObj][i][j][0]

    def addVA(self,iObj,vr,vc,ar,ac):
        for i in range(0,self.row):
            for j in range(0,self.col):
                   

    def scrollDown(self,sN,sT):
        "sN: scroll sN rows every step, sT: interval time"
        for i in range(0,self.row/sN+1):
            self.moveObj(i*sN,0,0)
            self.addToBuf(0,'over')
            self.show()
            time.sleep(sT)
            
a=asciiMovie(40,100)
a.newObj()
a.addData('a.txt',0)
a.scrollDown(1,0.1)
