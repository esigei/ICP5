import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#creating a panda dataframe to hold X and Y values of the object
data=pd.DataFrame({'X':[1.0,1.5,3.0,5.0,3.5,4.5], 'Y':[1.0,2.0,4.0,7.0,5.0,5.0]})
np.random.seed(100)
k=2#number of clusters
#choosing a random value to create a centroid centroid
centroids={i+1:[np.random.randint(0,8),np.random.randint(0,8)] for i in range(k)}
# scatter plot for the results
plt.scatter(data['X'],data['Y'],color='k')#plotting a scatter plot for x and y values with 2 different colors
#create a map for plot colors
colormap={1:'b',2:'y'}
for i in centroids.keys():
    plt.scatter(*centroids[i],color=colormap[i])
plt.xlim(0,8)
plt.ylim(0,8)
plt.show()