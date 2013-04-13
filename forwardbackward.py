from clean import*
from decimal import*
from math import*
import sys
from forward import*

file1=cleantext('hmm-traintest.txt')
A=('A','E','I','O','U',' ')
pi=(1,0)
alpha=forward(file1)
beta=backward(file1)
#print 'alpha',alpha[len(alpha)-1],'beta',beta[0]
#print 'alpha',alpha,'beta',beta
#print alpha[len(alpha)-1][1]
#print beta[0][0]
#for a in alpha:
#    print 'a=',a,'a[0]=',a[0],'a[1]=',a[1]
    
#for a in beta:
#    print 'b=',a,'b[0]=',a[0],'b[1]=',a[1]

def getalpha(t,i):    
    if i==1:
        return alpha[t][0]
    else:
        return alpha[t][1]

def getbeta(t,i):
     if i==1:
        return beta[t][0]
     else:
        return beta[t][1]

def sigma(t,i,j):
    sig=getalpha(t,i)*gettranp(i,j)*getbeta(t+1,j)*getep(j,file1[t+1])
    sumsig=0
    for a in range(1,3):
        for b in range(1,3):
            sumsig+=getalpha(t,a)*gettranp(a,b)*getbeta(t+1,b)*getep(b,file1[t+1])
            print t,a,b,getalpha(t,a)*gettranp(a,b)*getbeta(t+1,b)*getep(b,file1[t+1]),sumsig
    sigma=Decimal(sig)/Decimal(sumsig)
   
    print 'sig',sig
    print 'sum',sumsig
    print 'sigma',sigma
    return sigma
#sigma(0,1,2)
#sigma(10,1,2)

def theta(t,i):
    sumth=0
    for a in range(1,3):
        sumth+=sigma(t,i,a)
        #print t,a,getalpha(t,a)*getbeta(t,a)
        #print sumth
    #theta=(getalpha(t,i)*getbeta(t,i))/sumth
    #print 'theta',theta
        #print 'theta',sigma(t,i,a),sumth
    return sumth

sumthe=0
for a in range(1,3):
    sumthe+=sigma(0,1,a)
print 'sumthe',sumthe
print theta(0,1)

def tranpnew(i,j):
    sum1=0
    for T in range(0,len(file1)-1):
        
        sum1+=sigma(T,i,j)
        #print T,i,j,'sigma',sigma(T,i,j),'sum',sum1
    sum2=0
    for T in range(0,len(file1)):
        sum2+=theta(T,i)
        #print T,i,'theta',theta(T,i),'sum',sum2
    tranp=sum1/sum2
    return tranp
#print tranpnew(1,1),tranpnew(1,2),tranpnew(2,1),tranpnew(2,2)
#print file1[0]
def emitpnew():
 
    
    s1={}
    s2={}
    for T in range(0,len(file1)):
        
        
            
        if s1.has_key(file1[T])==False:
            
            s1[file1[T]]=theta(T,1)
        else:
            s1[file1[T]]+=theta(T,1)

        if s2.has_key(file1[T])==False:
            s2[file1[T]]=theta(T,2)
        else:
            s2[file1[T]]+=theta(T,2)
    sumch1=sum(s1.values())
    sumch2=sum(s2.values())
    #print 'sums1',sums1,sumch1,'sums2',sums2,sumch2
    ps1=[]
    ps2=[]
    for k, v in s1.items():
        a=[k, Decimal(v)/Decimal(sumch1)]
        ps1.append(a)
  
    for k, v in s2.items():
  
        a=[k, Decimal(v)/Decimal(sumch2)]
        ps2.append(a)
    #for a in ps1:
#        print '1',a
#    for a in ps2:
#        print '2',a
    eps=(ps1,ps2)
    
    #for a in eps:
#        print'a',a,'a0',a[0],'a1',a[1],'a2',a[2]
    return eps
#a=emitpnew()
#print a[0][0][0],a[1][1][1]
#def HMM(pi,    
    
        
