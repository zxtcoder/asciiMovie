#!/usr/bin/python

import os,sys,math,time,copy,random

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
            line=content[i].strip('\n')
            numtmp=len(line)
            for j in range(0,numtmp):
                if(line[j]==' '):
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

    def addPoint(self,flag,iobj,ch,nr,nc,vr,vc,ar,ac):
        if(flag=='cur'):
            self.obj[iobj].append([])
            self.obj[iobj][-1].append(ch)
            self.obj[iobj][-1].append(nr); self.obj[iobj][-1].append(nc)
            self.obj[iobj][-1].append(vr); self.obj[iobj][-1].append(vc)
            self.obj[iobj][-1].append(ar); self.obj[iobj][-1].append(ac)
        if(flag=='begin'):
            self.objBegin[iobj].append([])
            self.objBegin[iobj][-1].append(line[j])
            self.objBegin[iobj][-1].append(nr); self.objBegin[iobj][-1].append(nc)
            self.objBegin[iobj][-1].append(vr); self.objBegin[iobj][-1].append(vc)
            self.objBegin[iobj][-1].append(ar); self.objBegin[iobj][-1].append(ac)
        if(flag=='end'):
            self.objEnd[iobj].append([])
            self.objEnd[iobj][-1].append(line[j])
            self.objEnd[iobj][-1].append(nr); self.objEnd[iobj][-1].append(nc)
            self.objEnd[iobj][-1].append(vr); self.objEnd[iobj][-1].append(vc)
            self.objEnd[iobj][-1].append(ar); self.objEnd[iobj][-1].append(ac)

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
            ch=item[0]; nrow=int(item[1]); ncol=int(item[2])
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
###########   Effect      #######################

    def addVec1(self,iobj,vr,vc,ar,ac):
        for item in self.obj[iobj]:
            item[3]=vr; item[4]=vc; item[5]=ar; item[6]=ac

    def addVecCir(self,iobj,nr,nc,vMax,vMin,a):
        for item in self.obj[iobj]:
            irow=item[1];icol=item[2]
            dr=irow-nr; dc=icol-nc
            dd=math.sqrt(dr*dr+dc*dc+0.0)
            if(dd==0):
                continue
            item[3]=(dr/dd*vMax); item[4]=(dc/dd*vMax*1.5);

    def addVecRand(self,iobj,v):
        for item in self.obj[iobj]:
            vr=(random.random()-0.5)*v
            vc=(random.random()-0.5)*v
            item[3]=vr; item[4]=vc

    def scroll(self,iobj,vr,vc,flag):
        num=len(self.obj[iobj])
        if(flag=='init'):
            for item in self.obj[iobj]:
                item[3]=vr; item[4]=vc
        if(flag=='end'):
            for i in range(0,num):
                nrC=self.obj[iobj][i][1]; ncC=self.obj[iobj][i][2]
                nrE=self.objEnd[iobj][i][1]; ncE=self.objEnd[iobj][i][2]
                dr=nrE-nrC; dc=ncE-ncC
                dd=math.sqrt(dr*dr+dc*dc)
                if(dd<=1):
                    vr=0;vc=0; 
                    self.obj[iobj][i][1]=nrE; self.obj[iobj][i][2]=ncE
                    self.obj[iobj][i][3]=vr; self.obj[iobj][i][4]=vc

    def snow(self,iobj,vr,vc):
        for item in self.obj[iobj]:
            item[3]=vr; item[4]=vc*(random.random()-0.5)

    def fountain(self,iobj,nr,nc,v,a):
        dAng=math.pi/7;i=0
        for i in range(0,50):
            self.addPoint('cur',iobj,'*',nr,nc,0,0,0,0)
        i=1
        dAng=-(random.random()+1)
        for item in self.obj[iobj][-21:]:
            item[3]=v*math.sin(i*dAng); item[4]=v*math.cos(i*dAng)*1.5
            item[5]=a; item[6]=0

    def lineShow(self,iobj,num):
        pnum=len(self.obj[iobj])
        bnum=len(self.objBegin[iobj])
        for i in range(pnum,pnum+num):
            if(i>=bnum):
                break
            self.obj[iobj].append(self.objBegin[iobj][i])

    def shadeHide(self,iobj,num):
        for i in range(0,num):
            pnum=len(self.obj[iobj])
            if(pnum<=0):
                break
            selIndex=int(random.random()*pnum)
            self.obj[iobj].pop(selIndex)

    def shadeShow(self,iobj,num):
        for i in range(0,num):
            pnum=len(self.objBegin[iobj])
            if(pnum<=0):
                break
            selIndex=int(random.random()*pnum)
            self.obj[iobj].append(self.objBegin[iobj][selIndex])
            self.objBegin[iobj].pop(selIndex)

    def mixText(self,iobj,v):
        num=len(self.obj[iobj])
        for i in range(0,num):
            nrC=self.obj[iobj][i][1]; ncC=self.obj[iobj][i][2]
            nrE=self.objEnd[iobj][i][1]; ncE=self.objEnd[iobj][i][2]
            dr=nrE-nrC; dc=ncE-ncC
            dd=math.sqrt(dr*dr+dc*dc)
            if(dd<=1):
                vr=0;vc=0; 
                self.obj[iobj][i][1]=nrE; self.obj[iobj][i][2]=ncE
                self.obj[iobj][i][3]=vr; self.obj[iobj][i][4]=vc
            else:
                vrand=v*(random.random()-0.5)
                vr=dr/dd*v+vrand; vc=dc/dd*v+vrand
                self.obj[iobj][i][3]=vr; self.obj[iobj][i][4]=vc

    def bubble(self,iobj,vr,vc,flag):
        num=len(self.obj[iobj])
        rowF=0; colF=0
        if(flag=='init'):
            self.addVec1(iobj,vr,vc,0,0)
        if(flag=='end'):
            for i in range(0,num):
                if(self.obj[iobj][i][1]>=self.row or self.obj[iobj][i][1]<=0):
                    rowF=1;
                if(self.obj[iobj][i][2]>=self.col or self.obj[iobj][i][2]<=0):
                    colF=1;
            if(rowF==1 or colF==1):
                for i in range(0,num):
                    if(rowF==1):
                        self.obj[iobj][i][3]*=-1
                    if(colF==1):
                        self.obj[iobj][i][4]*=-1
        

    def stripeRow(self,iobj,v,flag):
        num=len(self.obj[iobj])
        if(flag=='init'):
            for i in range(0,num):
                if(i%2==0):
                    self.obj[iobj][i][2]=self.obj[iobj][i][2]-self.col
                    self.obj[iobj][i][4]=v
                else:
                    self.obj[iobj][i][2]=self.obj[iobj][i][2]+self.col
                    self.obj[iobj][i][4]=-1*v
        if(flag=='end'):
            for i in range(0,num):
                nrC=self.obj[iobj][i][1]; ncC=self.obj[iobj][i][2]
                nrE=self.objEnd[iobj][i][1]; ncE=self.objEnd[iobj][i][2]
                dr=nrE-nrC; dc=ncE-ncC
                dd=math.sqrt(dr*dr+dc*dc)
                if(dd<=1):
                    vr=0;vc=0; 
                    self.obj[iobj][i][1]=nrE; self.obj[iobj][i][2]=ncE
                    self.obj[iobj][i][3]=vr; self.obj[iobj][i][4]=vc

