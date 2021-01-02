import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from IPython import get_ipython
import scipy.cluster.hierarchy as shc



try:
    df_crimedata=pd.read_csv('crime_data.csv',encoding='latin-1')


    del df_crimedata["City"]
    
    df_crimedata.head()
    
    df_crimedata.describe()
    df_crimedata.fillna(method ='ffill', inplace = True) 
    
    df_crimedata.hist(bins=30)
    
    scaler = StandardScaler() 
    data_transformed = scaler.fit_transform(df_crimedata) 

    Sum_of_squared_distances = []
    k = list(range(1,15))

     

    for i in k:

        km = KMeans(n_clusters=i)
        km = km.fit(data_transformed)
        Sum_of_squared_distances.append(km.inertia_)

    get_ipython().run_line_magic('matplotlib', 'qt')
    plt.figure(1)
    plt.plot(k, Sum_of_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
  
    
    
    
    kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
    pred_y = kmeans.fit_predict(data_transformed)
    plt.figure(2)
    plt.scatter(data_transformed[:,0], data_transformed[:,1])
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
    plt.show()
    
     # HEIRARCHICAL CLUSTERING  


    plt.figure(figsize =(8, 8)) 
    plt.title('Dendogram for crimedata') 
    Dendrogram = shc.dendrogram((shc.linkage(df_crimedata, method ='ward'))) 
    
    plt.show() 

except Exception as exp:
    print (exp)