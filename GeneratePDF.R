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

#print(ex)
#try(exams2nops(filenames))
#ex <- filenames[1:45]
#print(ex)
#print(length(ex))
#try(exams2nops(ex))
#try(exams2nops(ex,dir = '.',name = 'Exam_test', institution = "Statistics 2 Midterm2020",blank = TRUE,samepage = TRUE))


#test <- c('CENTRAL LIMIT 1.Rmd','CENTRAL LIMIT 2.Rmd','CONFIDENCE INTERVAL 2.Rmd','CONFIDENCE INTERVAL 3.Rmd')
#exams2nops(test)
