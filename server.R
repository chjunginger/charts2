library(shiny)
library(graphics)
library(xtable)
setwd("~/PycharmProjects/lyrics")
data<-read.csv("matrix_of_1_grm_count.txt",header=T)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {

  dataset <- reactive({
    data[, c(input$In1,input$In2,input$In3)]
  })
  context1 <- reactive({
    data2<-read.csv(sprintf("3_grms_%s.txt",input$contextyr),header=F)
    context1<-data2[grepl(sprintf("(^| )%s( |$)",input$In1),data2[,2]),]
    colnames(context1)<-c("no","triplet","count")
    context1[1:5,2:3]
  })
  context2 <- reactive({
    data2<-read.csv(sprintf("3_grms_%s.txt",input$contextyr),header=F)
    context2<-data2[grepl(sprintf("(^| )%s( |$)",input$In2),data2[,2]),]
    colnames(context2)<-c("no","triplet","count")
    context2[1:5,2:3]
  })
  context3 <- reactive({
    data2<-read.csv(sprintf("3_grms_%s.txt",input$contextyr),header=F)
    context3<-data2[grepl(sprintf("(^| )%s( |$)",input$In3),data2[,2]),]
    colnames(context3)<-c("no","triplet","count")
    context3[1:5,2:3]
  })
  
  output$distPlot <- renderPlot({
    range=c(min(min(dataset())),max(max(dataset())))
    plot(cbind(1956:2014,dataset()[,1]),type="l",col=c("red"),ylim=range,xlab="Year",ylab="No of songs containg the word")
    lines(cbind(1956:2014,dataset()[,2]),type="l",col=c("blue"))
    lines(cbind(1956:2014,dataset()[,3]),type="l",col=c("green"))
    title("Number of top 100 songs containing chosen words over time")
    abline(v=input$contextyr)
  })
  output$text1 <- renderTable({ 
    xtable(context1())
  })
  output$text2 <- renderTable({ 
    xtable(context2())
  })
  output$text3 <- renderTable({ 
    xtable(context3())
  })
})
