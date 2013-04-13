from clean import*
from decimal import*
from math import*
import sys

file1=cleantext('hmm-test-korean.txt')

#tranp=(Decimal('0.2935938621001886003100493401'), Decimal('0.7061584571150777708630080687'), Decimal('0.7388871359975243713967463857'), Decimal('0.2612974615938796753911728810'))
tranp=(Decimal('0.3221132837983356473021868302'), Decimal('0.6919229669439437485890135563'), Decimal('0.6866123423461650239892715401'), Decimal('0.2990975617490370660910116090'))
#ps1=[[' ', Decimal('0.1876222038878175836010117810')], ['A', Decimal('0.06865374173925510120607554017')], ['C', Decimal('0.01720997572436682455226465758')], ['B', Decimal('0.01099776843428776288979654011')], ['E', Decimal('0.1139891691368046929717912448')], ['D', Decimal('0.03956314355119994683273920145')], ['G', Decimal('0.01311644303375530749795565748')], ['F', Decimal('0.02442364207551253510778153545')], ['I', Decimal('0.05630206738192977296966838977')], ['H', Decimal('0.05678432763192034476527570365')], ['K', Decimal('0.003063669944411120769348838678')], ['J', Decimal('0.0006822000487871131154602276759')], ['M', Decimal('0.02333735955442875135466407059')], ['L', Decimal('0.03055918650243379806641716877')], ['O', Decimal('0.05220087588769709857126150069')], ['N', Decimal('0.05179388739633167843931252881')], ['Q', Decimal('0.001085154319625328314367438611')], ['P', Decimal('0.01113724556802987900361611008')], ['S', Decimal('0.04770836120937932728008795499')], ['R', Decimal('0.04914594808043693072890127491')], ['U', Decimal('0.02747882698784347601974441341')], ['T', Decimal('0.06570026769936718248316548709')], ['W', Decimal('0.01945762908492110084407310160')], ['V', Decimal('0.009939429479913395153615120795')], ['Y', Decimal('0.01740977240753577583910705444')], ['X', Decimal('0.0006255534700498905128169620966')], ['Z', Decimal('0.00001214976195828110968049633046')]]
#ps2=[[' ', Decimal('0.1841367174537684510949839140')], ['A', Decimal('0.05555553826914279433816887725')], ['C', Decimal('0.02095354298381189488929690923')], ['B', Decimal('0.01262916660202835666806459170')], ['E', Decimal('0.09394008757823889926390199532')], ['D', Decimal('0.03406911237460958731653183063')], ['G', Decimal('0.01257303041650575948136298755')], ['F', Decimal('0.01765345261196536650792450462')], ['I', Decimal('0.05760097920809032886813714459')], ['H', Decimal('0.05232946208764123380189452436')], ['K', Decimal('0.003424480232990518533902915712')], ['J', Decimal('0.0009250701393804572112506543326')], ['M', Decimal('0.02310988685019529212798117281')], ['L', Decimal('0.03313411963081368317408033894')], ['O', Decimal('0.07716044608810772219377974136')], ['N', Decimal('0.06097596006483473600123058397')], ['Q', Decimal('0.001248418236744881100229043479')], ['P', Decimal('0.01151496037268053313868117160')], ['S', Decimal('0.05832243652228148873609082103')], ['R', Decimal('0.05346683376551786104023678460')], ['U', Decimal('0.01639423785237288214642994498')], ['T', Decimal('0.07048813078136413907217503883')], ['W', Decimal('0.01949624124441523267191802767')], ['V', Decimal('0.01068233131347801509076916478')], ['Y', Decimal('0.01724374193933724657885114702')], ['X', Decimal('0.0009098392111802138768122645836')], ['Z', Decimal('0.00006177616850242507531390385069')]]
ps1=[[' ', Decimal('0.1090310791212425323797912050')], ['A', Decimal('0.1004125016253232023770573272')], ['C', Decimal('0.008578783778585199629391336831')], ['B', Decimal('0.01739108518303611181214214209')], ['E', Decimal('0.06554034057472027849349933980')], ['D', Decimal('0.03449413424390157482083591162')], ['G', Decimal('0.05844024707991814699217257640')], ['I', Decimal('0.05469541500677155598972709313')], ['H', Decimal('0.03042050756149842835674303125')], ['K', Decimal('0.01849981897000885320916125163')], ['J', Decimal('0.02213643235456268981992681734')], ['M', Decimal('0.02353462962710497366451369761')], ['L', Decimal('0.03467890615794734021730146250')], ['O', Decimal('0.1160891827085474846151503498')], ['N', Decimal('0.09278597068784616143625106709')], ['P', Decimal('0.009575524522154218008702193123')], ['S', Decimal('0.03292323020660312079159429899')], ['R', Decimal('0.02547649698583370341411687259')], ['U', Decimal('0.09322099211735859048993474278')], ['T', Decimal('0.02646463016322419843617853524')], ['W', Decimal('0.008517560546351159625227028296')], ['V', Decimal('0.0001879369914429621163673866623')], ['Y', Decimal('0.01690459378601751330421433300')]]
ps2=[[' ', Decimal('0.1249946159483571876082399947')], ['A', Decimal('0.09933601600910783973564039968')], ['C', Decimal('0.01006114892699916668463691249')], ['B', Decimal('0.01177729381457031123021174139')], ['E', Decimal('0.1880155866389626294589403850')], ['D', Decimal('0.02847975734308252577391455377')], ['G', Decimal('0.06177973182587800605491435239')], ['I', Decimal('0.05811607933953379863388761639')], ['H', Decimal('0.02008135751317873512449853345')], ['K', Decimal('0.01897988611143441317756182535')], ['J', Decimal('0.02391150877047488066422535965')], ['M', Decimal('0.02683905883612012615546629976')], ['L', Decimal('0.01576791013811527085691265724')], ['O', Decimal('0.05768333699649661239436201379')], ['N', Decimal('0.09062700942452304593871168254')], ['P', Decimal('0.01028227277069438921267893824')], ['S', Decimal('0.02666830807135541820009464487')], ['R', Decimal('0.02899871963438429626502930597')], ['U', Decimal('0.04110117599152839303839944781')], ['T', Decimal('0.02727384242178744134442078794')], ['W', Decimal('0.006286120844841715682937085438')], ['V', Decimal('0.0001716186922151831826088735417')], ['Y', Decimal('0.02276764393635861358170658913')]]
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
    s1=(Decimal(0.5)*gettranp(1,1)+Decimal(0.5)*gettranp(2,1))*getep(1,(file1[0]))
    s2=(Decimal(0.5)*gettranp(2,2)+Decimal(0.5)*gettranp(1,2))*getep(2,(file1[0]))
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
    print alpha[len(file1)-1]
    #print Decimal(log(alphas2[len(file1)-1]))
    
 #   r=(alphas1,alphas2)
#    return r
    return alpha
    
test=forward(file1)

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
    print beta[0]
 #   r=(alphas1,alphas2)
#    return r
    return beta
test=backward(file1)
    
print(len(file1))
