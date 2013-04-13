import sys
import random
from decimal import*
from math import*
def randomep():
    a=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ')
    randome1={}
    randome2={}
    
    for ch in a:
        if randome1.has_key(ch)==False:
            randome1[ch]=random.randrange(0,1001)
        if randome2.has_key(ch)==False:
            randome2[ch]=random.randrange(0,1001)
 
    sumch1=sum(randome1.values())
    sumch2=sum(randome2.values())
    ps1=[]
    ps2=[]
    for k, v in randome1.items():
        a=[k, Decimal(v)/Decimal(sumch1)]
        ps1.append(a)
  
    for k, v in randome2.items():
  
        a=[k, Decimal(v)/Decimal(sumch2)]
        ps2.append(a)

    r=(ps1,ps2)
    return r

print randomep()
