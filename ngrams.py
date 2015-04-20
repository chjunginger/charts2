__author__ = 'christianjunginger'
# calculates 3-grams from all the lyrics; stores them in textfiles, seperate for each year as a key-value pair.
#key=3gram; value=number of songs that used the 3-gram that year

import re
import json




def countwords(lyric):
    lyricdic=[]
    lyric = re.sub(r'[^\w\s\']',' ',lyric)
    lyric=lyric.lower()
    text=lyric.split()

    for i in range(len(text)-2):
        word="%s %s %s"%(text[i],text[i+1],text[i+2])
        if word not in lyricdic:
            if word in wordcount:
                wordcount[word]+=1
            else:
                wordcount[word]=1
        lyricdic.append(word)



for yr in range(1956,2015):
    print(yr)
    #open and read the json file
    wordcount={}
    lyricsdic={}
    g=open('prep_lyrics_%s.txt'%yr)
    data=json.loads(g.read())
    fo=open("3_grms_%s.txt"%yr,"wb")

    for y in data:
        countwords(data[y])
        i=1


    for w in sorted(wordcount,key=wordcount.get,reverse=True):
        fo.write ("%i,%s,%s\n"%(i,w,wordcount[w]))
        i+=1
    #fo.write("%i,%s,%i\n"%(i,'not found lyrics', notfoundcounter))
    fo.close()


