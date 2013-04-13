from clean import*
from decimal import*
from math import*
import sys

file1=cleantext('hmm-decode.txt')

tranp=(Decimal('0.2935938621001886003100493401'), Decimal('0.7061584571150777708630080687'), Decimal('0.7388871359975243713967463857'), Decimal('0.2612974615938796753911728810'))

ps1=[[' ', Decimal('0.1876222038878175836010117810')], ['A', Decimal('0.06865374173925510120607554017')], ['C', Decimal('0.01720997572436682455226465758')], ['B', Decimal('0.01099776843428776288979654011')], ['E', Decimal('0.1139891691368046929717912448')], ['D', Decimal('0.03956314355119994683273920145')], ['G', Decimal('0.01311644303375530749795565748')], ['F', Decimal('0.02442364207551253510778153545')], ['I', Decimal('0.05630206738192977296966838977')], ['H', Decimal('0.05678432763192034476527570365')], ['K', Decimal('0.003063669944411120769348838678')], ['J', Decimal('0.0006822000487871131154602276759')], ['M', Decimal('0.02333735955442875135466407059')], ['L', Decimal('0.03055918650243379806641716877')], ['O', Decimal('0.05220087588769709857126150069')], ['N', Decimal('0.05179388739633167843931252881')], ['Q', Decimal('0.001085154319625328314367438611')], ['P', Decimal('0.01113724556802987900361611008')], ['S', Decimal('0.04770836120937932728008795499')], ['R', Decimal('0.04914594808043693072890127491')], ['U', Decimal('0.02747882698784347601974441341')], ['T', Decimal('0.06570026769936718248316548709')], ['W', Decimal('0.01945762908492110084407310160')], ['V', Decimal('0.009939429479913395153615120795')], ['Y', Decimal('0.01740977240753577583910705444')], ['X', Decimal('0.0006255534700498905128169620966')], ['Z', Decimal('0.00001214976195828110968049633046')]]
ps2=[[' ', Decimal('0.1841367174537684510949839140')], ['A', Decimal('0.05555553826914279433816887725')], ['C', Decimal('0.02095354298381189488929690923')], ['B', Decimal('0.01262916660202835666806459170')], ['E', Decimal('0.09394008757823889926390199532')], ['D', Decimal('0.03406911237460958731653183063')], ['G', Decimal('0.01257303041650575948136298755')], ['F', Decimal('0.01765345261196536650792450462')], ['I', Decimal('0.05760097920809032886813714459')], ['H', Decimal('0.05232946208764123380189452436')], ['K', Decimal('0.003424480232990518533902915712')], ['J', Decimal('0.0009250701393804572112506543326')], ['M', Decimal('0.02310988685019529212798117281')], ['L', Decimal('0.03313411963081368317408033894')], ['O', Decimal('0.07716044608810772219377974136')], ['N', Decimal('0.06097596006483473600123058397')], ['Q', Decimal('0.001248418236744881100229043479')], ['P', Decimal('0.01151496037268053313868117160')], ['S', Decimal('0.05832243652228148873609082103')], ['R', Decimal('0.05346683376551786104023678460')], ['U', Decimal('0.01639423785237288214642994498')], ['T', Decimal('0.07048813078136413907217503883')], ['W', Decimal('0.01949624124441523267191802767')], ['V', Decimal('0.01068233131347801509076916478')], ['Y', Decimal('0.01724374193933724657885114702')], ['X', Decimal('0.0009098392111802138768122645836')], ['Z', Decimal('0.00006177616850242507531390385069')]]
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
    path=[]
    s1=(Decimal(0.5)*gettranp(1,1)+Decimal(0.5)*gettranp(2,1))*getep(1,(file1[0]))
    s2=(Decimal(0.5)*gettranp(2,2)+Decimal(0.5)*gettranp(1,2))*getep(2,(file1[0]))
    alphaa=(s1,s2)
    alphas1.append(s1)
    alphas2.append(s2)
    alpha.append(alphaa)
    if s1>s2:
        path.append('s1')
    else:
        path.append('s2')
    
    t=0
    #print alphas1[0],alphas2[0]
    #print len(file1)
    for t in range (1,len(file1)):
        s1=(alphas1[t-1]*gettranp(1,1)+alphas2[t-1]*gettranp(2,1))*getep(1,(file1[t]))
        s2=(alphas2[t-1]*gettranp(2,2)+alphas1[t-1]*gettranp(1,2))*getep(2,(file1[t]))
        if s1>s2:
            path.append('s1')
        else:
            path.append('s2')
        alphas1.append(s1)
        alphas2.append(s2)
        alphaa=(s1,s2)
        alpha.append(alphaa)
        #print 't=',t,'alpha1',s1,alphas1[t],'alpha2',s2,alphas2[t]
        t=t+1
    print alpha[len(file1)-1]
    print path
    print file1
    #print Decimal(log(alphas2[len(file1)-1]))
    
 #   r=(alphas1,alphas2)
#    return r
    return alpha
    
test=forward(file1)
