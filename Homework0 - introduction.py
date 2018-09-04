
# coding: utf-8

# ### Homework 0 - Introduction

# In this homework, I still use the Building Inventory data set.

# In[5]:


#First I will read in data as a data frame and plot the relationship between two random numerical variables
#Read in data
import pandas as pd
df=pd.read_csv("building_inventory.csv")
df.head()


# In[6]:


#check the basic information about the dataframe df
print(df.shape)
print(df.dtypes)
print(df.describe())


# In[7]:


#Change the column names in the data frame
df.columns = df.columns.str.replace(' ', '_')


# In[8]:


print(df.dtypes)


# In[9]:


#Let's try to get the plot about the relationship between two numerical variables
import matplotlib.pyplot as plt


# In[10]:


#I pick variables Year_Constructed and Congress_Dist
plt.scatter(df.Year_Constructed, df.Congress_Dist,s=df.Total_Floors)


# From the plot above, we can find most buildings were constructed after 1750. Let's clean the data and make a plot after using boolean expression.

# In[12]:


yearpick=df.Year_Constructed>1750
plt.scatter(df.Year_Constructed[yearpick], df.Congress_Dist[yearpick],s=df.Total_Floors)

#Refine the plot by adding titles
plt.title("State Buildings")
plt.xlabel("Year Constructed")
plt.ylabel("Congress Distance")


# Let's try the hexbin plot.

# In[13]:


plt.clf()
plt.hexbin(df.Year_Constructed[yearpick], df.Congress_Dist[yearpick], gridsize=32,bins='log',cmap='inferno')
plt.title("State Buildings")
plt.xlabel("Year Constructed")
plt.ylabel("Congress Distance")
plt.colorbar()
fig = plt.gcf()


# For practice, I will redo the code shown in class. First I will create a dictionary and then count the frequence in one character variable. 

# In[14]:


import csv
f = open("Building_Inventory.csv")
csv_reader = csv.reader(f)
header = next(csv_reader)


# In[15]:


data = {}
for name in header:
    data[name] = []
data


# In[16]:


for row in csv_reader:
    for name, value in zip(header, row):
        data[name].append(value)


# In[18]:


data.keys()


# In[19]:


len(data['City'])


# In[20]:


len(set(data['City']))


# In[22]:


from collections import Counter
c = Counter(data['City'])
c.most_common()


# In[25]:


max(c.values())


# In[27]:


import numpy as np


# In[29]:


Rep_Dist = np.array(data['Rep Dist'], dtype='int')
Rep_Dist[::5]


# In[31]:


Counter(data['Rep Dist']).most_common(10)


# In[36]:


city_count = Counter()
for city, repdist in zip(data['City'], data['Rep Dist']):
    if int(repdist) == 115:
        city_count[city] += 1


# In[37]:


city_count

