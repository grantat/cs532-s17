library(Kendall)
setwd(getwd())
# csv dataframe of PR, TFIDF, URI
csv <- read.table('output/pageRankTfidf.csv',header = TRUE,sep = ",")

ken <- Kendall(csv$PR,csv$TFIDF)
summary(ken)