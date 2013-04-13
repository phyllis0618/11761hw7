from decimal import*
from math import*


a=Decimal('2.255645067726071071006914703')
b=17551
c=log(a,2)-b*log(10,2)
d=14483
ans=Decimal(c/d)
print ans
