import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

d = pd.read_csv("customers.csv")
X = d[['Age','Annual Income (k$)','Spending Score (1-100)']]
k = KMeans(n_clusters=3, random_state=0).fit(X)
d['Cluster'] = k.labels_

print("Data with cluster labels:\n", d)
print("\nMean:\n", d.groupby('Cluster').mean(numeric_only=True))
print("\nStd:\n", d.groupby('Cluster').std(numeric_only=True))

plt.scatter(d['Age'], d['Spending Score (1-100)'], c=d['Cluster'], cmap='rainbow')
plt.title("K-Means Clustering of Customers")
plt.xlabel("Age"); plt.ylabel("Spending Score (1-100)")
plt.show()
