setwd(getwd())
data <- read.table("data/mergedRaw", header=FALSE, sep='|')

counts <- data$V2
pdf("../docs/RawHistogram.pdf")
barplot(counts, ylab="File Size Difference", xlab="Raw Files", main="Change in Size of Raw File")
dev.off()
