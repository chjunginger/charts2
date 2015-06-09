__author__ = 'christianjunginger'
#gets  all ngrams and counts how many distinct songs use it (per year)

import re
import json
n=3 #length of ngram


def PreprocessLyric(lyric):
    lyric = re.sub(r'[^\w\s\']',' ',lyric)
    lyric=lyric.lower()
    return lyric.split()


def GetNgramSongCountsForYear(AllLyricsOfYear):
    for OneTo100 in AllLyricsOfYear:
        AlreadyCountedNgramOfLyric=[]
        text=PreprocessLyric(AllLyricsOfYear[OneTo100])

        for i in range(len(text)-(n-1)):
            ngram="%s %s %s"%(tuple(text[i:i+n]))
            if ngram not in AlreadyCountedNgramOfLyric:
                AlreadyCountedNgramOfLyric.append(ngram)
                if ngram in wordcount:
                    wordcount[ngram]+=1
                else:
                    wordcount[ngram]=1
    return wordcount




for Year in range(1956,1957):
    print(Year)
    wordcount={}
    AllLyricsOfYear=json.loads(open('prep_lyrics_%s.txt'%Year).read())
    fo=open("%i_grms_%s.txt"%(n,Year),"wb")
    NgramCountList=GetNgramSongCountsForYear(AllLyricsOfYear)


    for (i,w) in enumerate(sorted(NgramCountList,key=NgramCountList.get,reverse=True)):
        fo.write ("%i,%s,%s\n"%(i+1,w,NgramCountList[w]))
    fo.close()


