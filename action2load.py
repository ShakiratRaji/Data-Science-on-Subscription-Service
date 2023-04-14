#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[2]:


df = pd.read_csv("actions2load.csv")


# ## DATA EXPLORATION

# In[3]:


df.head()


# In[4]:


df.dtypes


# In[5]:


df.shape


# In[6]:


df.nunique()


# In[7]:


# find out completeness of the data set
df.isnull().sum()


# ## DATA CLEANING

# In[8]:


# drop the column with least completeness   additional_data
df.drop(['additional_data'], axis = 1)


# In[9]:


df.isnull().sum()


# In[24]:


#df.drop_duplicates(subset=['product_id'], keep='first')


# ### Most Common and Least Common Event

# In[10]:


# Most common and Least common Event
event_frequency = df["event_type"].value_counts()
event_frequency


# In[11]:


# Most Common Event is ReadingOwnedBook 
# Least Common Event is CommentCreated 
print(' Most Common Event type is ',event_frequency.idxmax())
print(' Least Common Event type is ',event_frequency.idxmin())
#event_frequency.idxmax()


# ### Account ID with highest and lowest number of events.

# In[12]:


# Account ID with Highest and Lowest number of events.
df["account_id"].value_counts()


# In[13]:


# Account_id with highest number of events is 6bb61e3b7bce0931da574d19d1d82c88
# Account_id with highest number of events is 3519f4939d54c1911afa74226a78c3f9          
print( ' Account_id with highest number of events is ', df["account_id"].value_counts().idxmax())
print( ' Account_id with lowest number of events is ', df["account_id"].value_counts().idxmin())
#df["account_id"].value_counts().idxmax()


# ### Event Occurence based on time of the day

# In[14]:


# convert event_time to date time format
df["event_time"] = pd.to_datetime(df["event_time"])


# In[15]:


df.dtypes


# In[16]:


# create a new column event_year
df["event_year"] = df["event_time"].dt.year


# In[17]:


# create a new column event_month
df["event_month"] = df["event_time"].dt.month_name(locale = 'English')


# In[18]:


# create a new column day_of_the_month
df["day_of_the_week"] = df["event_time"].dt.day_name(locale = 'English')


# In[19]:


df.head()


# In[20]:


df.nunique()


# In[16]:


df["event_year"].value_counts()


# In[21]:


monthly_subscription=df.event_month.value_counts()[df.event_month.unique()]
monthly_subscription


# In[22]:


monthly_subscription.plot.bar(figsize =(8,4))
plt.ylabel("Number of Subscriptions")
plt.xlabel("Month of the Year")
plt.title("Monthly Subscription")


# In[23]:


df["day_of_the_week"].value_counts()


# In[24]:


df["day_of_the_week"].value_counts().plot.bar(figsize=(8,4))
plt.ylabel("Number of Subcription")
plt.xlabel("Day of the week")
plt.title("Day of the Week")


# In[25]:


# create new colum showing event time of the day
df["time"] = df["event_time"].dt.time


# In[26]:


df["event_time_of_the_day"] = df["event_time"].dt.hour
#df["event_time_of_the_day"] = df["event_time"].dt.minute


# In[27]:


df.head()


# In[28]:


subscription_time=df.event_time_of_the_day.value_counts()
sub=subscription_time.reset_index(drop = True)
sub


# In[29]:


sub.plot.bar(figsize =(8,4))
plt.ylabel("Number of Subscriptions")
plt.xlabel("Time of the Day")
plt.title("Subscription and Time of the day")


# ### Checking outliers in the number of events

# In[30]:


df2=pd.DataFrame(event_frequency)
df2


# In[31]:


df2.rename(columns={'event_type':'event_count'}, inplace=True) 


# In[33]:


plt.boxplot(df2)


# ### Removing Outliers from

# In[36]:


def drop_outlier(data,var):
    q1, q3 = np.percentile(data[var], [25, 75])
    iqr = q3 - q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    data = data[data[var]< upper]
    data = data[data[var]> lower]
    data.reset_index(drop=True, inplace = True)
    return data


# In[39]:


df3 = drop_outlier(df2, "event_count")


# In[40]:


plt.boxplot(df3)


# ### TIME SERIES

# In[42]:


cols =['event_time','event_type']
data= pd.read_csv("actions2load.csv", usecols=cols)
data.head()


# In[44]:


# check data types
data.dtypes


# In[45]:


# convert event_time to date time format and remove seconds
data['event_time'] = pd.to_datetime(data['event_time'], format='%Y-%m-%d %H:%M').map(lambda x: x.replace(second=0, microsecond=0))


# In[46]:


#cofirm data types
data.dtypes


# In[47]:


data.head()


# In[48]:


#count sum of event per time
data['event_time'].value_counts()[data.event_time.unique()]


# In[49]:


#create a dataframe from time and events count
data2=pd.DataFrame(data['event_time'].value_counts()[data.event_time.unique()])
data2


# In[50]:


#name the event count column properly
data2.rename(columns={'event_time':'event_count'}, inplace=True) 
data2


# In[ ]:


#data.set_index('event_time', inplace=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




