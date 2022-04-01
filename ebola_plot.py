import matplotlib.pyplot as plt  
import csv 
import pandas as pd


# data import
data = pd.read_csv('C:/ProgramData/Mastering Python Data Visualization_Code/Mastering Python Data Visualization_Code/Chapter2/ebola.csv')
print(data.columns)
print(data.dtypes)

# yyyy-mm-dd type object -> datetime 변경
data = data.astype({'Date':'datetime64'})
m_filtereddata = pd.merge(data[(data['Indicator'].str.find('deaths') != -1)], data[data['value'] != float(0)])
len(m_filtereddata)
m_sorteddata = m_filtereddata.sort_values([m_filtereddata.columns[1], m_filtereddata.columns[2]])

set(m_sorteddata['Country'])
m_guineadata = m_sorteddata[(m_sorteddata['Country'].str.find('Guinea') != -1)][(m_sorteddata['Indicator'] == 'Cumulative number of confirmed Ebola deaths')].reset_index(drop=True)
m_sierradata = m_sorteddata[(m_sorteddata['Country'].str.find('Sierra Leone') != -1)][(m_sorteddata['Indicator'] == 'Cumulative number of confirmed Ebola deaths')].reset_index(drop=True)
m_liberiadata = m_sorteddata[(m_sorteddata['Country'].str.find('Liberia') != -1)][(m_sorteddata['Indicator'] == 'Cumulative number of confirmed Ebola deaths')].reset_index(drop=True)

plt.figure(figsize=(10,10))
plt.plot(m_guineadata['Date'], m_guineadata['value'], color='red', linewidth=2, label = 'Guinea')
plt.plot(m_sierradata['Date'], m_sierradata['value'], color='orange', linewidth=2, label = 'Sierra Leone')
plt.plot(m_liberiadata['Date'], m_liberiadata['value'], color = 'blue', linewidth=2, label = 'Liberia')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Number of Ebola Deaths', fontsize=18)
plt.title("Confirmed Ebola Deaths", fontsize=20)
plt.legend(loc=1)
plt.show()



