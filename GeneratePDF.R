#!/usr/bin/Rscript
args = commandArgs(trailingOnly=TRUE)

# test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input directory).n", call.=FALSE)
}
setwd(args[1])



library(exams)

filenames <- list.files(".", pattern="*.Rmd", full.names=TRUE)
ex <- c()

for( name in filenames){
  print(name)
  try( exams2pdf(name, dir = './pdfs', name = name))
  ex <- append(ex,name)


}


