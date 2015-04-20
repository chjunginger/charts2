library(shiny)
categ<-names(read.csv("matrix_of_1_grm_count.txt",header=T))
# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Chart-Analytics"),
  
  # Sidebar with a slider input for the number of bins
  sidebarLayout(
    sidebarPanel(
      selectInput("In1",choices = categ[-1], label = "Word 1 (red)"),
      selectInput("In2",choices = categ[-1], label = "Word 2 (blue)"),
      selectInput("In3",choices = categ[-1], label = "Word 3 (green)"),
      sliderInput("contextyr",
                  "Get context for year:",
                  min = 1956,
                  max = 2014,
                  value = 1998)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot"),
      tableOutput("text1"),
      tableOutput("text2"),
      tableOutput("text3")
    )
  )
))
