install.packages("DataExplorer")

library(DataExplorer)

df_airline<-read.csv(file.choose())
df_airline<- df_airline[ -c(1) ]

df_airline_scaled <- data.frame(scale(df_airline))

summary(df_airline)



plot_histogram(df_airline_scaled)
plot_density(df_airline_scaled)


wss <- (nrow(df_airline_scaled)-1)*sum(apply(df_airline_scaled,2,var))
for (i in 2:15) wss[i] <- sum(kmeans(df_airline_scaled, centers=i)$withinss)
plot(1:15, wss, type="b", xlab="Number of Clusters", ylab="Within groups sum of squares")



fit <- kmeans(df_airline_scaled, 4) 

aggregate(df_airline_scaled,by=list(fit$cluster),FUN=mean)

km_df_airline <- data.frame(df_airline_scaled, fit$cluster)

plot(df_airline_scaled,col=km_df_airline$fit.cluster, main="k-means with 4 clusters")



summary(df_airline_scaled)

plot(hclust(dist(df_airline)), hang = -1)

plot_scatterplot(df_airline,by="Qual_miles",sampled_rows = 3000L)

