#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go


# In[9]:


data=pd.read_csv("C:/Users/Rakesh/Datasets/Virat_Kohli.csv")


# In[10]:


data.head()


# In[11]:


data.isnull().sum()


# In[12]:


# Total Runs between 18th August 2008 to 22nd January 2017
data['Runs'].sum()


# In[13]:


# Average of Virat_Kohli during the same period
data["Runs"].mean()


# #### Virat Kohli's trend Analysis
# matches=data.index
# figure=px.line(data_frame=data, x=matches, y='Runs', title="Virat Kohli trend analysis")
# figure.show()

# ## In many innings Virat has scored runs close to 90 or more than 100 which is very good
# 

# In[14]:


# Batting Position
data["Pos"]=data["Pos"].map({3.0:"Batting at 3",4.0:"Batting at 4",2.0:"Batting at 2",1.0:"Batting at 1",7.0:"Batting at 7",5.0:"Batting at 5",6.0:"Batting at 6"})

Pos=data["Pos"].value_counts()
label=Pos.index
counts=Pos.values
colors=['gold','lightgreen','pink','blue','skyblue','cyan','orange']

fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text='Number of Matches at Different Batting Position')
fig.update_traces(hoverinfo='label+percent',textinfo='value', textfont_size=30, marker=dict(colors=colors,line=dict(color='black', width=3)))
fig.show()


# ### Almost 69% of innings Virat Kohli batted at no 3

# In[18]:



label = data["Pos"]
counts = data["Runs"]
colors = ['gold','lightgreen', "pink", "blue", "skyblue", "cyan", "orange"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Runs By Virat Kohli At Different Batting Positions')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[19]:


centuries=data.query("Runs>=100")
figure=px.bar(centuries,x=centuries['Inns'],y=centuries["Runs"],color=centuries["Runs"],
             title="Centuries by Virat Kohli in First Innings vs the second innings")
figure.show()


# In[22]:


# Dismissals of Virat Kohli
dismissal=data['Dismissal'].value_counts()
label=dismissal.index
counts=dismissal.values
colors=["gold","lightgreen","pink","blue","skyblue","cyan","orange"]

fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
fig.update_layout(title_text="Dismissal of Virat Kohli")
fig.update_traces(hoverinfo='label+percent',textinfo='value',textfont_size=30,
                 marker=dict(colors=colors,line=dict(color='black',width=3)))
fig.show()


# In[23]:


figure=px.bar(data, x=data["Opposition"], y=data["Runs"],color=data["Runs"],title="Most Runs Against Teams")
figure.show()


# In[24]:


strike_rate=data.query("SR>=120")
print(strike_rate)


# In[25]:


figure=px.bar(strike_rate, x=strike_rate['Inns'],
             y=strike_rate['SR'],
             color=strike_rate['SR'],
             title="Virat Kohli's strike rate 1st innings vs the second innings")
figure.show()


# In[26]:


figure=px.scatter(data_frame=data, x='Runs', y='4s',size="SR", trendline="ols", 
                 title="Relationship between runs scored and fours")
figure.show()


# In[27]:


figure=px.scatter(data_frame=data, x='Runs', y='6s',size="SR", trendline="ols", 
                 title="Relationship between runs scored and sixes")
figure.show()


# In[ ]:




