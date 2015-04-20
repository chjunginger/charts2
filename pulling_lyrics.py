__author__ = 'christianjunginger'
#skript pulls the songs and artists from wikipedias billboard top 100 singles pages and stores it in billboard.txt



import urllib2
import re
import json
import time



chartthisyear={}
with open('billboard.txt','w') as f:

#Returns a list of list with top 100 (#,song,artist) through the years 1956-2014
    for yr in range(1956,2015):
        #to avoid 503-errors
        time.sleep(2)
        wordcount={}
        lyricsdic={}
        notfoundcounter=0

        #pull the source code from wikipedia's Billboard annual Top 100 pages
        link=urllib2.urlopen('http://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_%s'%yr)
        text=link.read()
        text=re.sub(ur"\xe2\x80\x9c|\xe2\x80\x9d","\"",text)

        #the wikipage changed in starting that year
        if yr>1981:
            x=re.findall('<th scope=\"row\">([0-9]+?)</th>\n<td>\"<.*? title=\".*?\">(.*?)</a>\"</td>\n<td>.*?\">(.*?)</a>',text)
        else:
            x=re.findall('<tr>\n<td>([0-9]+?)</td>\n<td(?:>\"<a .*?\stitle=\".*?\")?>(.*?)(?:</a>\")?</td>\n<td>.*?\">(.*?)</a>',text)

        chartthisyear[yr]=x

    json.dump(chartthisyear,f,sort_keys=True,indent=4,ensure_ascii=True)

