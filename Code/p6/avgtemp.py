import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from subprocess import check_output
Temp_data=pd.read_csv('GlobalLandTemperaturesByCountry.csv')
India_temp=Temp_data[Temp_data['Country']=='India'].dropna()
India_temp['dt']=pd.to_datetime(India_temp.dt)
India_temp['year']=India_temp['dt'].map(lambda x: x.year)
print(India_temp['year'].max())   #2013
time_period=range(1913,2013)

average_temp=[]
for year in time_period:
    average_temp.append(India_temp[India_temp['year']==year]['AverageTemperature'].mean())
plt.figure(figsize=(10,8))
plt.plot(time_period,average_temp)
plt.xlabel('years')
plt.ylabel('Average Temperature')
plt.title('Average Temperature of India over years')
z=np.polyfit(time_period,average_temp,10)
p = np.poly1d(z)
plt.plot(time_period,p(time_period),"r--")
print("average_temp=%.6fyears+(%.6f)"%(z[0],z[1]))
plt.show()
