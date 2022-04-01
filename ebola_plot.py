import matplotlib.pyplot as plt  
import csv 
import operator 
import datetime as dt
import pandas as pd


with open('C:/ProgramData/Mastering Python Data Visualization_Code/Mastering Python Data Visualization_Code/Chapter2/ebola.csv', 'rt') as f:
  filtereddata = [row for row in csv.reader(f) if row[3] != "0.0" and 
  row[3] != "0" and "deaths" in row[0]] 

sorteddata = sorted(filtereddata, key=operator.itemgetter(1))

guineadata  = [row for row in sorteddata if row[1] == "Guinea" and row[0] == "Cumulative number of confirmed Ebola deaths"]
sierradata  = [row for row in sorteddata if row[1] == "Sierra Leone" and row[0] == "Cumulative number of confirmed Ebola deaths"]
liberiadata = [row for row in sorteddata if row[1] == "Liberia" and row[0] == "Cumulative number of confirmed Ebola deaths"]


g_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for row in guineadata]
g_y = [row[3] for row in guineadata] 

s_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for row in sierradata]
s_y = [row[3] for row in sierradata] 

l_x = [dt.datetime.strptime(row[2], '%Y-%m-%d').date() for row in liberiadata]
l_y = [row[3] for row in liberiadata] 

plt.figure(figsize=(10,10))
plt.plot(g_x,g_y, color='red', linewidth=2, label='Guinea')
plt.plot(s_x,s_y, color='orange', linewidth=2, label = 'Sierra Leone')
plt.plot(l_x,l_y, color='blue', linewidth=2, label = 'Liberia')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Number of Ebola Deaths', fontsize=18)
plt.title("Confirmed Ebola Deaths", fontsize=20)
plt.legend(loc=2)
plt.show()



# 묭이 코드
data = pd.read_csv('C:/ProgramData/Mastering Python Data Visualization_Code/Mastering Python Data Visualization_Code/Chapter2/ebola.csv')
print(data.columns)
print(data.dtypes)
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



