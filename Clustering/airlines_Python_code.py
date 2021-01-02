import pandas as pd


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from IPython import get_ipython
from sklearn.preprocessing import StandardScaler 
import scipy.cluster.hierarchy as shc



try:
    df_airline=pd.read_csv('EastWestAirlines.csv',encoding='latin-1')


    del df_airline["ID"]
    
    df_airline.head()
    
    df_airline.describe()
     # Handling the missing values 
    df_airline.fillna(method ='ffill', inplace = True) 
   
    df_airline.hist(bins=30)
    #Preprocessing the data

    
    # Scaling the data so that all the features become comparable 
    scaler = StandardScaler() 
    df_airline_scaled = scaler.fit_transform(df_airline) 

    Sum_of_squared_distances = []
    k = list(range(1,15))


    for i in k:

        km = KMeans(n_clusters=i)
        km = km.fit(df_airline_scaled)
        Sum_of_squared_distances.append(km.inertia_)

    get_ipython().run_line_magic('matplotlib', 'qt')
    plt.figure(1)
    plt.plot(k, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
  
                   

    kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
    pred_y = kmeans.fit_predict(df_airline_scaled)
    plt.figure(2)
    plt.scatter(df_airline_scaled[:,0], df_airline_scaled[:,1])
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
    plt.show()
    
    
    # HEIRARCHICAL CLUSTERING  


    plt.figure(figsize =(8, 8)) 
    plt.title('Dendogram for Airline') 
    Dendrogram = shc.dendrogram((shc.linkage(df_airline, method ='ward'))) 
    
    plt.show() 

except Exception as exp:
    print (exp)
    