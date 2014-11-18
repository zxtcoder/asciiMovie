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
            for j in range(0,self.col):
                self.objList0[-1][-1].append(' ')
                self.objList1[-1][-1].append(' ')

    def addData(self,fname,iObj):
        fp=open(fname,'r')
        for i in range(0,self.row):
            line=fp.readline()[:-1]
            for j in range(0,self.col):
                if(j<len(line)):
                    self.objList0[iObj][i][j]=line[j]
                    self.objList1[iObj][i][j]=line[j]
                else:
                    self.objList0[iObj][i][j]=' '
                    self.objList1[iObj][i][j]=' '
        fp.close()

    def clearObj(self,iObj,flag):
         for i in range(0,self.row):
            for j in range(0,self.col):
                if(flag=='0'):
                    self.objList0[iObj][i][j]=' '
                if(flag=='1'):
                    self.objList1[iObj][i][j]=' '
                if(flag=='a'):
                    self.objList0[iObj][i][j]=' '
                    self.objList1[iObj][i][j]=' '

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
        for i in range(0,self.row):
            for j in range(0,self.col):
                if(flag=='add'):
                    if(self.objList1[iObj][i][j]!=' '):
                         self.buf[i][j]=self.objList1[iObj][i][j]
                if(flag=='over'):
                    self.buf[i][j]=self.objList1[iObj][i][j]

    def moveObj(self,nrow,ncol,iObj):
        self.clearObj(iObj,'1')
        for i in range(0,self.row):
            for j in range(0,self.col):
                i2=i+nrow; j2=j+ncol
                if(i2>=0 and i2<self.row and j2>=0 and j2<self.col):
                    self.objList1[iObj][i2][j2]=self.objList0[iObj][i][j]

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
