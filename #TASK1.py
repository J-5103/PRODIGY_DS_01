import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'D:\Python\PRODIGY INFOTECH INTERNSHIP\TASK#1\population.csv')

print(data.head())
print(data.columns)

data_2020 = data[['Country Name', '2020']].dropna()

data_2020.columns = ['Country', 'Population']

top10 = data_2020.sort_values(by='Population', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.bar(top10['Country'], top10['Population'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.title('Population of Top 10 Countries in 2020')
plt.xlabel('Country')
plt.ylabel('Population')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data_2020['Population'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Population Across Countries in 2020')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.show()