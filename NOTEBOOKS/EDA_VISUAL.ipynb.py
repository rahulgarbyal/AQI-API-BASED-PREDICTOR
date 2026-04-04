import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

df = pd.read_csv("../DATA/processed/cleaned_aqi.csv")
df.head()
print(df.shape)
print(df.describe())

#AQI DISTRIBUTION
plt.figure(figsize = (10,5))
plt.hist(df['aqi_value'], bins = 50)
plt.title("Distribution of aqi values")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.show()

#TOP 10 MOST POLLUTED CITIES
top_cities = df.groupby('area')['aqi_value'].mean().sort_values(ascending = False).head(10)
plt.figure(figsize = (10,10))
top_cities.plot(kind = 'bar')
plt.title("Top 10 Most Polluted Cities")
plt.ylabel("Average AQI")
plt.show()

#TOP 10 LEAST POLLUTED CITIES
clean_cities = df.groupby('area')['aqi_value'].mean().sort_values().head(10)
plt.figure(figsize = (10,10))
clean_cities.plot(kind = 'bar')
plt.title("Top 10 Clean Cities")
plt.ylabel("Average AQI")
plt.show()

# STATE WISE AVG AQI
state_avg = df.groupby('state')['aqi_value'].mean().sort_values(ascending = False).head(15)
plt.figure(figsize = (12,12))
state_avg.plot(kind = 'bar')
plt.title("State-Wise Average AQI")
plt.ylabel("Average AQI")
plt.show()

#monthly trend
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

monthly_trend = df.groupby('month')['aqi_value'].mean()
plt.figure(figsize = (10,10))
monthly_trend.plot(marker='o')
plt.title("Monthly AQI Trend")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.grid(True)
plt.show()

#yearly trend
df['year'] = df['date'].dt.year
yearly_trend = df.groupby('year')['aqi_value'].mean()
plt.figure(figsize = (8,5))
yearly_trend.plot(marker='o')
plt.title("Yearly AQI Trend")
plt.xlabel("Years")
plt.ylabel("Average AQI")
plt.grid(True)
plt.show()

#Air quality status count
status_counts = df['air_quality_status'].value_counts()
plt.figure(figsize = (10,10))
status_counts.plot(kind = 'bar')
plt.title("Air Quality Status Distribution")
plt.ylabel("Count")
plt.show()

#Prominent Pollutant Frequency
pollutants = df['prominent_pollutants'].value_counts().head(10)
plt.figure(figsize = (10,10))
pollutants.plot(kind = 'bar')
plt.title("Most Frequent Pollutants")
plt.ylabel("Count")
plt.show()
