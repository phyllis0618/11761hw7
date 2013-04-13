from clean import*
from decimal import*
from math import*
file1=cleantext('hmm-traintest.txt')
A=('A','E','I','O','U',' ')
def count(A,file):
 
    file=file1
    dict={}
    for ch in file:
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
  #print "%s=%s" % (k, Decimal(v)/Decimal(sumch1))
    
    #print Decimal(sumch1)/Decimal(sumch)
    for k, v in dictstate2.items():
  #print "%s=%s" % (k, Decimal(v)/Decimal(sumch2))
        a=[k, Decimal(v)/Decimal(sumch2)]
        ps2.append(a)
    #print Decimal(sumch2)/Decimal(sumch)




    dicttr11=0
    dicttr12=0
    dicttr21=0
    dicttr22=0


    tr=[(file1[i],file1[i+1]) for i in range(len(file1)-1)]
    for item in tr:
    #print item
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
#print Decimal(dicttr11)/Decimal(dicttr11+dicttr12)
#print Decimal(dicttr12)/Decimal(dicttr11+dicttr12)
#print Decimal(dicttr21)/Decimal(dicttr21+dicttr22)
#print Decimal(dicttr22)/Decimal(dicttr21+dicttr22)
#print sumch
#print len(file1)

    tranp=[(Decimal(dicttr11)/Decimal(dicttr11+dicttr12),Decimal(dicttr12)/Decimal(dicttr11+dicttr12),Decimal(dicttr21)/Decimal(dicttr21+dicttr22),Decimal(dicttr22)/Decimal(dicttr21+dicttr22))]
#print 'tranp=',tranp
    r=(ps1,ps2,tranp)
    
    return r
