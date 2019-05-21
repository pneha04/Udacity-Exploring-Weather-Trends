# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 11:31:33 2019

@author: NEHA PATIL
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('results.csv')
data['year'] = pd.to_datetime(data['year'],format='%Y')
data.set_index(data['year'],inplace=True)
#print(data['year'].head())
#data['city_temp_MA7']=(data.city_temp.rolling(7).mean())-10
data['city_temp_MA7']=data.city_temp.rolling(7).mean()
data['global_temp_MA7']=data.global_temp.rolling(7).mean()
#plt.grid(True)
plt.figure(figsize=(15,10))
plt.title("Weather Trends-Global V/S Local Temperatures")
#plt.ylim([10,25])
#plt.xlim([2000,2010])
data['city_temp_MA7'].plot(linewidth=1, c='blue',label='Bangalore city temperature in Celcius')
data['global_temp'].plot(linewidth=1, c='red',label='Average global Temperature in Celcius')
data['global_temp_MA7'].plot(linewidth=1, c='green',label=' Moving Average global Temperature in Celcius')
plt.grid(True)
plt.rc('grid', linestyle=":", linewidth=1, color='gray')
plt.legend(loc='best')
plt.xlabel('Year', fontsize=10)
plt.ylabel("Temperature (°C)", fontsize=10)
plt.show()
df=pd.DataFrame([data['year'],data['city_temp'],data['city_temp_MA7'],data['global_temp'],data['global_temp_MA7']])
df=df.transpose()
data.to_csv('moving_average.csv',sep='\t')
#corelation=np.corrcoef(list1,list2)
#print(corelation)