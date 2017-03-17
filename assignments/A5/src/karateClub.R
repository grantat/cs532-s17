library(igraph)
library(igraphdata) # provides karate data
setwd(getwd())

# ensure same seed/graph sample each run
set.seed(20)
# convert to graph format
data(karate)
kclub <- karate

# remove edges 
clust <- cluster_edge_betweenness(kclub)
# Original split
origCommunties <- plot.igraph(kclub)
# Second value is number of communities to create
groups <- cutat(clust, 2)
# Assumed should have split
plot(structure(list(membership=groups), class="communities"), kclub)
connected_components_count <- count_components(kclub)

# index counter for node edges
edgeIndex <- 1
# split into groups, actual
while(connected_components_count != 2){
  # starts at 1
  edgesRemoved <- delete.edges(kclub, clust$removed.edges[seq(1,edgeIndex-1)])
  connected_components_count <- count_components(edgesRemoved)
  # set new Graph
  origCommunties <- edgesRemoved
  edgeIndex <- edgeIndex + 1
}

print(paste("Iteration Count",edgeIndex))
plot.igraph(origCommunties)
