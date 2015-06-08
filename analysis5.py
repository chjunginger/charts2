__author__ = 'christianjunginger'
#produces a matrix used in the shiny app
#to be improved and cleaned up :)
import numpy as np
import pandas as pd
import json
import re
import stat
import matplotlib.pyplot as plt
import pylab
import operator
import heapq

timeframe=range(1956,2015)
#timeframe=range(1970,1985)
#timeframe=range(1985,2000)
#timeframe=range(2000,2015)
w1="i"
w2="love"
#smaller percentthreshold => more categories
percentthreshold=0.005


def dict_nlargest(d,threshold):
    dictsum=sum(val for val in d.values())
    bestdic={}

    for u in d:

        if d[u]>totalsum*threshold:
            bestdic[u]=d[u]

    if dictsum-sum(val for val in bestdic.values())!=0:
        bestdic["**other**"]=dictsum-sum(val for val in bestdic.values())
    return bestdic


thephrases=[]








thirdwords={}
fourthwords=[]
fifthwords=[]


for yr in timeframe:
    print(yr)
    g = open('prep_lyrics_%s.txt'%yr)
    data=json.loads(g.read())


    for i in data:
        text=re.sub(r"-|\(|\)|^"," ",data[i].encode("ascii","ignore"))
        text=re.sub(r"\?|\!|\,|\;|\"",".",text)
        text=text.split()
        for j in range(len(text)-5):
            if (text[j].lower()==w1 and text[j+1].lower()==w2):
                thephrases.append("%s %s %s %s %s"%(text[j].lower(),text[j+1].lower(),text[j+2].lower(),text[j+3].lower(),text[j+4].lower()))



thirddic={}
for i in thephrases:

    if re.sub(r"\.","",i.split()[2]) in thirddic:
        thirddic[re.sub(r"\.","",i.split()[2])]+=1
    else:
        thirddic[re.sub(r"\.","",i.split()[2])]=1


totalsum=sum(val for val in thirddic.values())
print(totalsum)
thirdwords=dict_nlargest(thirddic,percentthreshold)
t=[]
for key in sorted(thirdwords.keys()):
    t.append([key,thirdwords[key]])
thirdwords=t







for z in range(len(thirdwords)):
    oo=thirdwords[z][0]
    print
    temp={}
    if oo=="**other**":
        temp["**otherNA**"]=thirdwords[z][1]
    else:
        for i in thephrases:
            i=i.split()
            if i[2].lower()==oo:
                if (re.sub("\.","",i[3])) not in temp:
                    temp[re.sub("\.","",i[3])]=1
                else:
                    temp[re.sub("\.","",i[3])]+=1
            elif (re.sub("\.","",i[2].lower())==oo):
                    if "**NA**" not in temp:
                        temp["**NA**"]=1
                    else:
                        temp["**NA**"]+=1

    temp=dict_nlargest(temp,percentthreshold)
    t=[]
    for key in sorted(temp.keys()):
        t.append([key,temp[key]])
    fourthwords.append(t)




for m in range(len(fourthwords)):
    oo=thirdwords[m][0]

    for z in range(len(fourthwords[m])):

        kk=fourthwords[m][z][0]
        outertemp=[]
        temp={}

        if kk=="**other**" or kk=="**otherNA**":
            temp["**otherNA**"]=fourthwords[m][z][1]

        elif kk=="**NA**":
            temp["**NA**"]=fourthwords[m][z][1]

        else:
            for i in thephrases:
                i=i.split()

                if (i[2]==oo and i[3]=="%s."%(kk)):
                    if "**NA**" not in temp:
                        temp["**NA**"]=1
                    else:
                        temp["**NA**"]+=1

                elif (i[2]==oo and i[3]==kk):
                    if (re.sub("\.","",i[4])) not in temp:
                        temp[re.sub("\.","",i[4])]=1
                    else:
                        temp[re.sub("\.","",i[4])]+=1


        temp=dict_nlargest(temp,percentthreshold)
        if temp !={}:
            t=[]

            for key in sorted(temp.keys()):
                t.append([key,temp[key]])
            outertemp.append(t)

        fifthwords.append(outertemp)



with open("third.csv","wb") as f:
    for e in range(len(thirdwords)):
        f.write("%s,%i\n"%(thirdwords[e][0],thirdwords[e][1]))


with open("fourth.csv","wb") as f:
    for i in range(len(fourthwords)):
        for e in range(len(fourthwords[i])):
            f.write("%s,%i\n"%(fourthwords[i][e][0],fourthwords[i][e][1]))


with open("fifth.csv","wb") as f:
    for i in range(len(fifthwords)):
        for j in range(len(fifthwords[i])):
            for e in range(len(fifthwords[i][j])):
                f.write("%s,%i\n"%(fifthwords[i][j][e][0],fifthwords[i][j][e][1]))

