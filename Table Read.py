#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df1=pd.read_excel("C:/Users/Aritra/Desktop/fsmpro_asmt_question_2 (Autosaved).xlsx")


# In[2]:


df2=pd.read_csv("C:/Users/Aritra/Desktop/tbl_fsmpro_hh_answers.csv")
df3=pd.read_csv("C:/Users/Aritra/Desktop/fsmpro_asmt_options.csv")


# In[3]:


df1.head()


# In[ ]:


df1.fillna(0,inplace=True)
df2.fillna(0,inplace=True


# In[34]:


q=input("Enter ques: ")
a = df1[df1['question_text'].str.match(q)]
a


# In[35]:


b=a['qcode']
b


# In[36]:


df2.columns = df2.columns.str.upper()


# In[37]:


common_entries=df2[b].drop_duplicates()
common_entries


# In[13]:


df3.head()


# In[38]:


gk=[]

for i in df3['option_code']:
    for j in ass['Q6']:
        if i==j:
            gk.append(df3.index[df3.option_code == j])
            
            
gk


for i in gk:
    print(df3.loc[i]['option_text'].values)

            
        


# In[33]:


#df4=pd.merge(df1,df2)


# In[39]:


#q=input("Enter ques")
#a = df4[df4['question_text'].str.match(q)]
#b=a['qcode']
#if b in df4.columns:
    #print(df4[b].unique())


# In[17]:





# In[ ]:





# In[ ]:




