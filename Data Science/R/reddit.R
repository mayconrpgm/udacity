#https://flowingdata.com/2015/02/18/loading-data-and-basic-formatting-in-r/
#http://vita.had.co.nz/papers/tidy-data.pdf
#http://courses.had.co.nz.s3-website-us-east-1.amazonaws.com/12-rice-bdsi/slides/07-tidy-data.pdf

setwd("D:/Projetos/udacity/Data Science/R")

reddit <- read.csv('reddit.csv')
#reddit <- read.csv('https://s3.amazonaws.com/udacity-hosted-downloads/ud651/reddit.csv')

str(reddit)
names(reddit)
summary(reddit)

table(reddit$marital.status)

levels(reddit$age.range)
levels(reddit$employment.status)
levels(reddit$military.service)
levels(reddit$education)

library(ggplot2)

qplot(data = reddit, x = age.range)

reddit$age.range = factor(
  reddit$age.range,
  levels = c(
    "Under 18",
    "18-24",
    "25-34",
    "35-44",
    "45-54",
    "55-64",
    "65 or Above"
  ),
  ordered = TRUE
)

#using ordered instead of factor
reddit$age.range = ordered(
  reddit$age.range,
  levels = c(
    "Under 18",
    "18-24",
    "25-34",
    "35-44",
    "45-54",
    "55-64",
    "65 or Above"
  )
)
