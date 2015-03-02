__author__ = 'christianjunginger'
import urllib2
import urllib
import re
import json
import operator
import time



#Parses through LyricsMode.com to find the lyrics
def getlyric(artist,song):
    global notfoundcounter
    global yr
    #preprocess artist and song
    artist=re.sub(r'&amp;|\.|#|\?|=|\|\(|\)|\'|!','',artist)
    artist=re.sub(r'\xc3\xa9','e',artist)
    if artist[0:3].lower()=="the":
        artist=artist[4:]
    song=re.sub(r'\(.*?\)','',song)
    song=re.sub(r'&amp;|\.|#|\?|=|\|\(|\)|\'|!','',song)
    song=re.sub(r'\xc3\xa9','e',song)

    artist=re.sub(r'  |-',' ',artist)
    song=re.sub(r'  |-',' ',song)
    song=song.strip()
    artist=artist.strip()

    if artist[0].isalpha():
       art_0=artist[0]
    else:
        art_0='0-9'

    print(art_0,song,artist)
    try:
        response=urllib2.urlopen('http://www.lyricsmode.com/lyrics/%s/%s/%s.html'%(art_0,re.sub(' ','_',artist),re.sub(' ','_',song)))
        text=response.read()
    except urllib2.HTTPError as err:
        if err.code==503:
            print(yr)
            raise
        else:
            print(err.code)
            notfoundcounter+=1
            return(" ")

    lyric=re.findall("<p id=\"lyrics_text\"(.*?)</p>",text,re.DOTALL)[0]
    #replace newline,[ ],everything in < >
    lyric=re.sub('\[.+?\]|^.+?>|<.+?>',' ',lyric,flags=0)
    return(lyric)




#returns a list of list with top 100 (#,song,artist) through the years (parsed from wikipedia)
#1956 first year of top100 Billboard
for yr in range(1956,1957):
    time.sleep(10)
    wordcount={}
    lyricsdic={}
    notfoundcounter=0


    link=urllib2.urlopen('http://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_%s'%yr)
    text=link.read()
    text=re.sub(ur"\xe2\x80\x9c|\xe2\x80\x9d","\"",text)

    #the wikipage changed for year 1982 and following
    if yr>1981:
        x=re.findall('<th scope=\"row\">([0-9]+?)</th>\n<td>\"<.*? title=\".*?\">(.*?)</a>\"</td>\n<td>.*?\">(.*?)</a>',text)
    else:
        x=re.findall('<tr>\n<td>([0-9]+?)</td>\n<td(?:>\"<a .*?\stitle=\".*?\")?>(.*?)(?:</a>\")?</td>\n<td>.*?\">(.*?)</a>',text)


    for y in x:
        lyricsdic[int(y[0])]=getlyric(y[2],y[1])

    #writetofile(countwords,yr,notfoundcounter)
    with open('lyrics_%s.txt'%yr,'w') as f:
        json.dump(lyricsdic,f,sort_keys=True,indent=4)



