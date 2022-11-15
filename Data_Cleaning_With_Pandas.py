#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[16]:


#Import Data Using Saved Excel Files - FLIGHTS
flights_data = pd.read_csv('flights.csv')
flights_data.head()


# In[19]:


#Import Data Using Saved Excel Files - WEATHER
weather_data = pd.read_csv('weather.csv')
weather_np = weather_data.to_numpy()
weather_data.head()


# In[22]:


#Question1: How many flights from JFK to SLC?
flights_jfk_slc = len(flights_data[(flights_data.origin == 'JFK') & (flights_data.dest == 'SLC')]) #identify the respective columns for JFK and SLC and use len() to determine number of instances
print(flights_jfk_slc)
type(flights_jfk_slc)


# In[24]:


#Question 2: How many airlines fly to SLC? 
flights_dest_slc = len(flights_data[(flights_data.dest == 'SLC')]) #similar to question 1 , but this time the origin does not matter, just the destination to SLC
print(flights_dest_slc)
type(flights_dest_slc)


# In[26]:


#Question 3: Whta is the average arrival delay for flights to RDU?
#use .mean() method because we want the average
avg_arrivaldelay_RDU = flights_data[(flights_data.dest == 'RDU')]['arr_delay'].mean() #use arrival delay column for RDU
print(avg_arrivaldelay_RDU)
type(avg_arrivaldelay_RDU)


# In[36]:


#Question 4: What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?
JFK_SEA = flights_data[(flights_data['dest'] =='SEA')&(flights_data['origin'] == 'JFK')] #determine if there are flights from JFK to SEA
JFK_SEA
LGA_SEA = flights_data[(flights_data['dest'] =='SEA')&(flights_data['origin'] == 'LGA')] #determine if there are flights from LGA to SEA - there are NONE
LGA_SEA 
prop_JFK_SEA = len(flights_data[(flights_data.dest=='SEA') & (flights_data.origin=='JFK')])/len(flights_data[flights_data.dest=='SEA'])
prop_JFK_SEA


# In[69]:


#Question 5: Which date has the largest average departure delay? - #please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data_avg = (
    flights_data
    .assign(date=lambda row: pd.to_datetime(row[['year', 'month', 'day']]))
    .groupby('date')
    .mean()
) #creating the column and using group by then .mean method for average
flights_data_avg.nlargest(1, 'dep_delay')[['dep_delay']] #determining largest with dep;arture delay column 


# In[71]:


#Question 6: Which date has the largest average arrival delay? 
flights_data_avg = (
    flights_data
    .assign(date=lambda row: pd.to_datetime(row[['year', 'month', 'day']]))
    .groupby('date')
    .mean()
) #creating the column and using group by then .mean method for average
flights_data_avg.nlargest(1, 'arr_delay')[['arr_delay']] #determining largest with arrival delay column


# In[73]:


#Question 7: Which flight departing LGA or JFK in 2013 flew the fastest? - tailnumber and speed 
LGA_or_JFK = flights_data.loc[((flights_data['origin'] == 'LGA') | (flights_data['origin'] == 'JFK'))]
LGA_or_JFK['speed'] = LGA_or_JFK['distance']/LGA_or_JFK['air_time'] 
LGA_or_JFK['tailnum'][LGA_or_JFK['speed'] == LGA_or_JFK['speed'].max()]


# In[77]:


#Question 8: Replace all nans in the weather pd df with 0s
weather_data.fillna(0)


# In[83]:


#Question 9: How many observations were made in February? 
feb_obs= [weather_np[:, 3] == 2.0] #rows where the month is Feb (2)
print(np.count_nonzero(feb_obs)) #counting num of obs made in Feb


# In[92]:


#Question 10: What was the mean humidity in February?
feb_avg_humidity= np.split(weather_np[:,8], np.unique(weather_np[:, 3], return_index=True)[1][1:]) #selcting for the month of Feb and the respective humidity 
feb_humidity_select = feb_avg_humidity[1] #february column
print(np.mean(feb_humidity_select)) #mean


# In[95]:


#Question 11: What was the std for humidity in February? 
feb_std_humidity = np.split(weather_np[:,8], np.unique(weather_np[:, 3], return_index=True)[1][1:]) #selcting for the month of Feb and the respective humidity 
feb_humidity_select = feb_std_humidity[1] #february column
print(np.std(select)) #standard deviation for february 

