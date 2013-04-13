def cleantext(a):
    
    import re
    text=open(a,'r').read()
    textup=text.upper()
    #print textup
#a=filter(lambda c:c.isalpha(),textup)#replace nonalpha
#print a
    a=re.sub('[^A-Z]',' ',textup)#replace nonalpha
    #print a
    b=" ".join(a.split())
    return b
    #compile the spaces
    #print b
