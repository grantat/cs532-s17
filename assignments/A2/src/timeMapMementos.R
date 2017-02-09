setwd(getwd())
# csv dataframe of URI, number of mementos
mementoCount <- read.table(header = FALSE,sep = ",",'output/timeMaps.csv')
# histogram
hgram <- hist(mementoCount$V2,col = "gray", breaks = seq(from=0, to=20000, by=1000), main="URIs vs. Number of Mementos",xlab = "Number of Mementos")
# add count labels
text(hgram$mids,hgram$counts, adj=c(0.5, -0.5), labels=hgram$counts)

