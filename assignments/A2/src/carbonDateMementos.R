setwd(getwd())
# Merged Dataset with memento count and days
mementoDays <- read.table(header = FALSE,sep = ",",'output/carbonDateMerged.csv')
# filtered set w/ atleast 1 memento
withMementos <- subset(mementoDays, mementoDays$V2 > 0)
emptyDate <- subset(mementoDays, is.na(mementoDays$V3))
plot(withMementos$V3,withMementos$V2,ylab="Number of Mementos",xlab="Age in Days",main="Scatter Plot for Days vs. Mementos")
