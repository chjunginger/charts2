# charts2
collection of skripts for my chart-analysis on muchodata.wordpress.com

the following skripts are available

1.  pulling_lyrics.py pulls the names and artists of the top 100 songs from the wiki pages and stores them locally
2.  not available: the crawler, that takes each of theses songs and gets the lyrics from one of two lyrics websites
3.  ngrams.py that creates ngrams from the lyrics separate for each year and song
4.  analysis4.py that creates a matrix with rows= years from 1956 to 2014, cols=a set of interestion words, cells=number of songs of that year, that used this specific word at least once (matrix used in ui.R and server.R)
5.  analysis5.py that creates a dataset of words which follow the sentece "i love" and the counts how often these phrases were used in a specific time frame. This set is used in radialplotofIloves.R
6.  ui.R and server.R which make up the shiny app
7.  radialplotofIloves.R, which creates the radial plots of "I love..." as seen in my project
