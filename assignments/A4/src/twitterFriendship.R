setwd(getwd())

csv <- read.table('output/twitterFollowers.csv',header = FALSE,sep = ",")
numRows <- nrow(csv)
ordered <- csv[order(csv$V2),]
cols <- c("gray", "red")[(ordered$V1 == "phonedude_mln")+1]
# index position of 'Michael Nelson' in data table
nelsonIndex <- which(ordered$V1=="phonedude_mln")
count <- ordered[nelsonIndex,]

b <- plot(ordered$V2,col = cols,main="Twitter Follower Plot",xlab = "Twitter Followers",ylab = "Number of Followers",xaxt='n')
abline(v=nelsonIndex,col="red",lwd=2,lty=3)

# Add f1-f_n on x-axis
axis(1, at=c(1,numRows),
     lab=c("F1",paste("F",numRows)))
# y axis is just for padding
text(nelsonIndex,8,paste("Michael Nelson:",count$V2),col = "red")
# Summary Stats
print("MEAN, SD, MEDIAN")
print(mean(ordered$V2))
print(sd(ordered$V2))
print(median(ordered$V2))
