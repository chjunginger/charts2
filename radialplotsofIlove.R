#creates the radialplots of Ilove as seen in my project
setwd("~/PycharmProjects/lyrics")
library(RColorBrewer)
fifthlevel<-read.csv("fifth.csv",header=F,)
levels(fifthlevel$V1)[levels(fifthlevel$V1)=="**other**"] <- "*"

fifthlevel$V3<-cumsum(fifthlevel$V2)
fourthlevel<-read.csv("fourth.csv",header=F)
levels(fourthlevel$V1)[levels(fourthlevel$V1)=="**other**"] <- "*"

fourthlevel$V3<-cumsum(fourthlevel$V2)
thirdlevel<-read.csv("third.csv",header=F)
levels(thirdlevel$V1)[levels(thirdlevel$V1)=="**other**"] <- "*"

thirdlevel$V3<-cumsum(thirdlevel$V2)
total=sum(thirdlevel$V2)

## data input (number of reads mapped to each category)
colorpalet<-colorRampPalette(c("aquamarine3","darkgoldenrod", "coral"))(total)




# parameter for pie chart
iniR=0.15 # initial radius


library('plotrix')

# from outer circle to inner circle
#0 circle: blank
pie(1, radius=0.02*iniR, init.angle=90, col=c('white'), border = NA, labels='')

#4 circle: 
g<-floating.pie(0,0,fifthlevel$V2,radius=7*iniR, startpos=pi/2,border="white",col=(ifelse(fifthlevel$V1=="**NA**"|fifthlevel$V1=="**otherNA**","white",colorpalet[fifthlevel$V3])))
g
pie.labels(0,0,g,labels=ifelse(fifthlevel$V1=="**NA**"|fifthlevel$V1=="**otherNA**","",as.character(fifthlevel$V1)),7*iniR)
#3 circle: 
g<-floating.pie(0,0,fourthlevel$V2,radius=5*iniR, startpos=pi/2,border="white",col=(ifelse(fourthlevel$V1=="**NA**"|fourthlevel$V1=="**otherNA**","white",colorpalet[fourthlevel$V3])))
g
pie.labels(0,0,g,labels=ifelse(fourthlevel$V1=="**NA**"|fourthlevel$V1=="**otherNA**","",as.character(fourthlevel$V1)),4.4*iniR)
#2 circle: 
g<-floating.pie(0,0,thirdlevel$V2,radius=3*iniR, startpos=pi/2,border="white",col=(ifelse(thirdlevel$V1=="**NA**"|thirdlevel$V1=="**otherNA**","white",colorpalet[thirdlevel$V3])))
g
pie.labels(0,0,g,labels=ifelse(thirdlevel$V1=="**NA**"|thirdlevel$V1=="**otherNA**","",as.character(thirdlevel$V1)),2*iniR)
#1 circle:
floating.pie(0,0, 1, radius=1.5*iniR, startpos=pi/2, col="white", border = NA)



