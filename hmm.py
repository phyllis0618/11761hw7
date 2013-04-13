from clean import*
from decimal import*
from math import*
import sys
from forward import*
from forwardbackward import*

file1=cleantext('hmm-traintest.txt')
#p=(1,0)
emip=(ps1,ps2)
#p=(theta(0,1),theta(0,2))
p=(0,1)
a=(tranpnew(1,1),tranpnew(1,2),tranpnew(2,1),tranpnew(2,2))
b=emitpnew()
#print p,a,b

def hmm(pi,al,be):
    #tranp=al
    #ps1=be[0]
    #ps2=be[1]
    def gettranpp(i,j):
        if i==1:
            if j==1:
                return al[0]
            else:
                return al[1]
        else:
            if j==1:
                return al[2]
            else:
                return al[3]

    def getepp(i,a):
        if i==1:
            for char in be[0]:
                if a==char[0]:
            
                    return char[1]
                    break
       
            else:
                return 0

        else:
            for char in be[1]:
                if a==char[0]:
            
                    return char[1]
                    break
       
            else:
                return 0
  

    def forwardd(file,p):
        alphaas1=[]
        alphaas2=[]
        alphaa=[]
        s1=(Decimal(p[0])*Decimal(gettranpp(1,1))+Decimal(p[1])*Decimal(gettranpp(2,1)))*Decimal(getepp(1,(file1[0])))
        s2=(Decimal(p[1])*Decimal(gettranpp(2,2))+Decimal(p[0])*Decimal(gettranpp(1,2)))*Decimal(getepp(2,(file1[0])))
        alphaaa=(s1,s2)
        alphaas1.append(s1)
        alphaas2.append(s2)
        alphaa.append(alphaaa)
        t=0
        
        for t in range (1,len(file1)):
            s1=(alphaas1[t-1]*gettranpp(1,1)+alphaas2[t-1]*gettranpp(2,1))*getepp(1,(file1[t]))
            s2=(alphaas2[t-1]*gettranpp(2,2)+alphaas1[t-1]*gettranpp(1,2))*getepp(2,(file1[t]))
  
            alphaas1.append(s1)
            alphaas2.append(s2)
            alphaaa=(s1,s2)
            alphaa.append(alphaaa)
        
            t=t+1
 
        return alphaa
    


    def backwardd(file,p):
        betaas1=[]
        betaas2=[]
        betaa=[]
        s1=Decimal(p[1])*gettranpp(1,1)*getepp(1,(file1[len(file1)-1]))+Decimal(p[0])*gettranpp(1,2)*getepp(2,(file1[len(file1)-1]))
        s2=Decimal(p[0])*gettranpp(2,2)*getepp(2,(file1[len(file1)-1]))+Decimal(p[1])*gettranpp(2,1)*getepp(1,(file1[len(file1)-1]))
        betaas1.append(s1)
        betaas2.append(s2)
        betaaa=(s1,s2)
        betaa.append(betaaa)
        t=0
 
        for t in range (1,len(file1)):
            s1=betaas1[t-1]*gettranpp(1,1)*getepp(1,(file1[len(file1)-1-t]))+betaas2[t-1]*gettranpp(1,2)*getepp(2,(file1[len(file1)-1-t]))
            s2=betaas2[t-1]*gettranpp(2,2)*getepp(2,(file1[len(file1)-1-t]))+betaas1[t-1]*gettranpp(2,1)*getepp(1,(file1[len(file1)-1-t]))
    
            betaas1.append(s1)
            betaas2.append(s2)
            betaaa=(s1,s2)
            betaa.append(betaaa)
        
            t=t+1
        betaas1.reverse()
        betaas2.reverse()
        betaa.reverse()
        return betaa

    alphaa=forwardd(file1,pi)
    betaa=backwardd(file1,pi)
    #print 'alphaa',alphaa[len(alphaa)-1],'betaa',betaa[0]
    #print 'alphaa',alphaa,'betaa',betaa


    def getalphaa(t,i):    
        if i==1:
            return alphaa[t][0]
        else:
            return alphaa[t][1]

    def getbetaa(t,i):
         if i==1:
            return betaa[t][0]
         else:
            return betaa[t][1]

    def sigmaa(t,i,j):
        sig=getalphaa(t,i)*gettranpp(i,j)*getbetaa(t+1,j)*getepp(j,file1[t+1])
        sumsig=0
        for a in range(1,3):
            for b in range(1,3):
                sumsig+=getalphaa(t,a)*gettranpp(a,b)*getbetaa(t+1,b)*getepp(b,file1[t+1])
                #print t,a,b,getalphaa(t,a)*gettranp(a,b)*getbetaa(t+1,b)*getepp(b,file1[t+1]),sumsig
        sigma=Decimal(sig)/Decimal(sumsig)
   
        return sigma

    def thetaa(t,i):
        sumth=0
        for a in range(1,3):
            sumth+=getalphaa(t,a)*getbetaa(t,a)
        
        thetaa=(getalphaa(t,i)*getbetaa(t,i))/sumth
        #print 'theta',thetaa
        return thetaa
    def tranpneww(i,j):
        sum1=0
        for T in range(0,len(file1)-1):
        
            sum1+=sigmaa(T,i,j)
            #print T,i,j,'sigma',sigmaa(T,i,j),'sum',sum1
        sum2=0
        for T in range(0,len(file1)):
            sum2+=thetaa(T,i)
            #print T,i,'theta',thetaa(T,i),'sum',sum2
        tranppp=sum1/sum2
        return tranppp

    def emitpneww():
  
    
        s1={}
        s2={}
        for T in range(0,len(file1)):
        
        
            
            if s1.has_key(file1[T])==False:
            
                s1[file1[T]]=thetaa(T,1)
            else:
                s1[file1[T]]+=thetaa(T,1)
  
            if s2.has_key(file1[T])==False:
                s2[file1[T]]=thetaa(T,2)
            else:
                s2[file1[T]]+=thetaa(T,2)
        sumch1=sum(s1.values())
        sumch2=sum(s2.values())
 
        ps1=[]
        ps2=[]
        for k, v in s1.items():
            a=[k, Decimal(v)/Decimal(sumch1)]
            ps1.append(a)
  
        for k, v in s2.items():
  
            a=[k, Decimal(v)/Decimal(sumch2)]
            ps2.append(a)
   
        eps=(ps1,ps2)
      
 
        return eps
    pp=(thetaa(0,1),thetaa(0,2))
    #print thetaa(0,1),thetaa(0,2)
    aa=(tranpneww(1,1),tranpneww(1,2),tranpneww(2,1),tranpneww(2,2))
    bb=emitpneww()
    hmm=(pp,aa,bb)
    return hmm
#hmm1=hmm(p,a,b)
#print hmm1[0],hmm1[1],hmm1[2]
#hmm2=(hmm1[0],hmm1[1],hmm1[2])
#print 'hmm1',hmm1,'hmm2',hmm2
print len(file1)
    
    
    
