import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("customer_segmentation_data.csv")
features = ["Age","AnnualIncome","SpendingScore","PurchaseFrequency","OnlineEngagement"]
X = StandardScaler().fit_transform(df[features])
model = KMeans(n_clusters=4, random_state=42, n_init=20)
df["Cluster"] = model.fit_predict(X)
print(df.groupby("Cluster")[features].mean())
print("Silhouette score:", silhouette_score(X, df["Cluster"]))
df.to_csv("segmented_customers.csv", index=False)
