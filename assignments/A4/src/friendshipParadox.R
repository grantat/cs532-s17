setwd(getwd())

csv <- read.table('output/facebookFriends.csv',header = FALSE,sep = ",")
numRows <- nrow(csv)
ordered <- csv[order(csv$V2),]
cols <- c("gray", "red")[(ordered$V1 == "Michael Nelson")+1]
# index position of 'Michael Nelson' in data table
nelsonIndex <- which(ordered$V1=="Michael Nelson")
count <- ordered[nelsonIndex,]

b <- plot(ordered$V2,col = cols,main="Facebook Friendship Plot",xlab = "Facebook Friends",ylab = "Number of Friends",xaxt='n')
abline(v=nelsonIndex,col="red",lwd=2,lty=3)

# Add f1-f_n on x-axis
axis(1, at=c(1,numRows),
     lab=c("F1",paste("F",numRows)))
# y axis is just for padding
text(nelsonIndex,350,paste("Michael Nelson:",count$V2),col = "red")
# Summary Stats
print("MEDIAN, MEAN, SD")
print(median(ordered$V2))
print(mean(ordered$V2))
print(sd(ordered$V2))
