# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:00:36 2020

@author: Defender
"""

import pandas as pd

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from IPython import get_ipython
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler, normalize
import scipy.cluster.hierarchy as shc


try:
    df_wine=pd.read_csv('Dataset.csv',encoding='latin-1')
    df_wine.head()
    
    df_wine.describe()
    
     ##K MEANS CLUSTERING
    mms = MinMaxScaler()
    mms.fit(df_wine)
    data_transformed = mms.transform(df_wine)

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
  
                   

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    pred_y = kmeans.fit_predict(data_transformed)
    plt.figure(2)
    plt.scatter(data_transformed[:,0], data_transformed[:,1])
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')
    plt.show()
    
    
    ## HEIRARCHICAL CLUSTERING
    # Handling the missing values 
    df_wine.fillna(method ='ffill', inplace = True) 
   
    #Preprocessing the data

    
    # Scaling the data so that all the features become comparable 
    scaler = StandardScaler() 
    df_wine_scaled = scaler.fit_transform(df_wine) 
      
    # Normalizing the data so that the data approximately  
    # follows a Gaussian distribution 
    df_wine_normalized = normalize(df_wine_scaled) 
      
    # Converting the numpy array into a pandas DataFrame 
    df_wine_normalized = pd.DataFrame(df_wine_normalized) 
    
    #Reducing the dimensionality of the Data

    
    pca = PCA(n_components = 14) 
    df_wine_principal = pca.fit_transform(df_wine_normalized) 
    df_wine_principal = pd.DataFrame(df_wine_principal) 
    df_wine_principal.columns = ['Type','Alcohol','Malic','Ash','Alcalinity','Magnesium','Phenols','Flavanoids','Nonflavanoids','Proanthocyanins','Color','Hue','Dilution','Proline'] 

    
    plt.figure(figsize =(8, 8)) 
    plt.title('Dendogram for wine') 
    Dendrogram = shc.dendrogram((shc.linkage(df_wine_principal, method ='ward'))) 
    
   
    
except Exception as exp:
    print (exp)
