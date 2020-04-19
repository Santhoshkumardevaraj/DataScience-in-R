

library(DataExplorer)
#Mention the Dataset path briefly.
df_wine<-read.csv("Dataset.csv")

df_wine <- data.frame(scale(df_wine))

#PCA ANALYSIS

pca_wine<-prcomp(df_wine)

plot(pca_wine, type='l')

#plot_str(df_wine)
#plot_missing(df_wine)

#colnames(df_wine)

plot_histogram(df_wine)
plot_density(df_wine)



#K MEANS CLUSTERING

# Determine number of clusters
wss <- (nrow(pca_wine)-1)*sum(apply(df_wine,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(df_wine, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")


# K-Means Cluster Analysis
fit <- kmeans(df_wine, 3) # 5 cluster solution
# get cluster means
aggregate(df_wine,by=list(fit$cluster),FUN=mean)
# append cluster assignment
mydata <- data.frame(df_wine, fit$cluster)

#HEIRARCHICAL CLUSTERING

summary(pca_wine)

plot(hclust(dist(df_wine)), hang = -1)

plot_scatterplot(df_wine,by="Type",sampled_rows = 150L)


#create_report(df_wine)
