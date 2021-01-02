install.packages("DataExplorer")

library(DataExplorer)

df_crimedata<-read.csv(file.choose())
df_crimedata<- df_crimedata[ -c(1) ]

summary(df_crimedata)

df_crimedata_scaled <- data.frame(scale(df_crimedata))





plot_histogram(df_crimedata)
plot_density(df_crimedata)




wss <- (nrow(df_crimedata_scaled)-1)*sum(apply(df_crimedata_scaled,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(df_crimedata_scaled, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")



fit <- kmeans(df_crimedata_scaled, 4) 

aggregate(df_crimedata_scaled,by=list(fit$cluster),FUN=mean)

km_df_airline <- data.frame(df_crimedata_scaled, fit$cluster)

plot(df_crimedata_scaled,col=km_df_airline$fit.cluster, main="k-means with 4 clusters")



summary(df_crimedata)

plot(hclust(dist(df_crimedata)), hang = -1)


plot_scatterplot(df_crimedata,by="Qual_miles",sampled_rows = 50L)



