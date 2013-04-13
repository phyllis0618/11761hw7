from clean import*
from decimal import*
from math import*
import sys

file1=cleantext('hmm-traintest.txt')
A=('A','E','I','O','U',' ')


dict={}
for ch in file1:
    if dict.has_key(ch)==False :
        dict[ch] = 1
    else:
        dict[ch] += 1
sumch=sum(dict.values())
dictstate1={}
dictstate2={}
for ch in file1:
    if ch in A:
        if dictstate1.has_key(ch)==False :
            dictstate1[ch] = 1
        else:
            dictstate1[ch] += 1
    else:
        if dictstate2.has_key(ch)==False :
            dictstate2[ch] = 1
        else:
            dictstate2[ch] += 1
sumch1=sum(dictstate1.values())
sumch2=sum(dictstate2.values())
ps1=[]
ps2=[]
for k, v in dictstate1.items():
    a=[k, Decimal(v)/Decimal(sumch1)]
    ps1.append(a)
  
for k, v in dictstate2.items():
  
    a=[k, Decimal(v)/Decimal(sumch2)]
    ps2.append(a)
   
dicttr11=0
dicttr12=0
dicttr21=0
dicttr22=0
tr=[(file1[i],file1[i+1]) for i in range(len(file1)-1)]
for item in tr:
    
    if item[0] in A:
        if item[1] in A:
            dicttr11+=1
        else:
            dicttr12+=1
    else:
        if item[1] in A:
            dicttr21+=1
        else:
            dicttr22+=1

tranp=[Decimal(dicttr11)/Decimal(dicttr11+dicttr12),Decimal(dicttr12)/Decimal(dicttr11+dicttr12),Decimal(dicttr21)/Decimal(dicttr21+dicttr22),Decimal(dicttr22)/Decimal(dicttr21+dicttr22)]






def gettranp(i,j):
    if i==1:
        if j==1:
            return tranp[0]
        else:
            return tranp[1]
    else:
        if j==1:
            return tranp[2]
        else:
            return tranp[3]

def getep(i,a):
    if i==1:
        for char in ps1:
            if a==char[0]:
            
                return char[1]
                break
       
        else:
            return 0

    else:
        for char in ps2:
            if a==char[0]:
            
                return char[1]
                break
       
        else:
            return 0
  

def forward(file):
    alphas1=[]
    alphas2=[]
    alpha=[]
    s1=(1*gettranp(1,1)+0*gettranp(2,1))*getep(1,(file1[0]))
    s2=(0*gettranp(2,2)+1*gettranp(1,2))*getep(2,(file1[0]))
    alphaa=(s1,s2)
    alphas1.append(s1)
    alphas2.append(s2)
    alpha.append(alphaa)
    t=0
    #print alphas1[0],alphas2[0]
    #print len(file1)
    for t in range (1,len(file1)):
        s1=(alphas1[t-1]*gettranp(1,1)+alphas2[t-1]*gettranp(2,1))*getep(1,(file1[t]))
        s2=(alphas2[t-1]*gettranp(2,2)+alphas1[t-1]*gettranp(1,2))*getep(2,(file1[t]))
 
        alphas1.append(s1)
        alphas2.append(s2)
        alphaa=(s1,s2)
        alpha.append(alphaa)
        #print 't=',t,'alpha1',s1,alphas1[t],'alpha2',s2,alphas2[t]
        t=t+1
    #print alpha[len(file1)-1]
    #print Decimal(log(alphas2[len(file1)-1]))
    
 #   r=(alphas1,alphas2)
#    return r
    return alpha
    
#test=forward(file1)

def backward(file):
    betas1=[]
    betas2=[]
    beta=[]
    s1=0*gettranp(1,1)*getep(1,(file1[len(file1)-1]))+1*gettranp(1,2)*getep(2,(file1[len(file1)-1]))
    s2=1*gettranp(2,2)*getep(2,(file1[len(file1)-1]))+0*gettranp(2,1)*getep(1,(file1[len(file1)-1]))
    betas1.append(s1)
    betas2.append(s2)
    betaa=(s1,s2)
    beta.append(betaa)
    t=0
    #print betas1[0],betas2[0]
    #print len(file1)
    for t in range (1,len(file1)):
        s1=betas1[t-1]*gettranp(1,1)*getep(1,(file1[len(file1)-1-t]))+betas2[t-1]*gettranp(1,2)*getep(2,(file1[len(file1)-1-t]))
        s2=betas2[t-1]*gettranp(2,2)*getep(2,(file1[len(file1)-1-t]))+betas1[t-1]*gettranp(2,1)*getep(1,(file1[len(file1)-1-t]))
 
        betas1.append(s1)
        betas2.append(s2)
        betaa=(s1,s2)
        beta.append(betaa)
        #print 't=',t,'beta1',s1,betas1[t],'beta2',s2,betas2[t]
        t=t+1
    betas1.reverse()
    betas2.reverse()
    beta.reverse()
    #print beta[0]
 #   r=(alphas1,alphas2)
#    return r
    return beta
#test=backward(file1)
    
