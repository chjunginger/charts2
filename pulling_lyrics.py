__author__ = 'christianjunginger'
#skript pulls the songs and artists from wikipedias billboard top 100 singles pages and stores it in billboard.txt
import urllib2
import re
import json
import time


def GetTop100forYear(Year):
    sourcecode=GetSourceCodeofTop100WikiPageForYear(Year)

    if yr>1981:
        return re.findall('<th scope=\"row\">([0-9]+?)</th>\n<td>\"<.*? title=\".*?\">(.*?)</a>\"</td>\n<td>.*?\">(.*?)</a>',sourcecode)
    else:
        return re.findall('<tr>\n<td>([0-9]+?)</td>\n<td(?:>\"<a .*?\stitle=\".*?\")?>(.*?)(?:</a>\")?</td>\n<td>.*?\">(.*?)</a>',sourcecode)

def GetSourceCodeofTop100WikiPageForYear(Year):
    link=urllib2.urlopen('http://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_%s'%Year)
    text=link.read()
    text=re.sub(ur"\xe2\x80\x9c|\xe2\x80\x9d","\"",text)
    return text

chartthisyear={}

with open('billboard.txt','w') as f:
    for Year in range(1956,2015):
        time.sleep(2) # avoid 503 errors
        chartthisyear[Year]=GetTop100forYear(Year)

    json.dump(chartthisyear,f,sort_keys=True,indent=4,ensure_ascii=True)

