import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("campaign_data.csv",parse_dates=["Date"])
df["CTR (%)"]=df.Clicks/df.Impressions*100
df["Conversion Rate (%)"]=df.Conversions/df.Clicks*100
df["Engagement Rate (%)"]=df.Engagements/df.Impressions*100
df["CPC"]=df.Spend/df.Clicks
df["CPA"]=df.Spend/df.Conversions
print(df.head())
print("Overall CTR:",round(df.Clicks.sum()/df.Impressions.sum()*100,2),"%")
print("Overall conversion rate:",round(df.Conversions.sum()/df.Clicks.sum()*100,2),"%")
print(df.groupby("Campaign")[["Impressions","Clicks","Conversions","CTR (%)","Conversion Rate (%)"]].sum())
