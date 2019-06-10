#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


loc = r"C:\Users\Aritra\Downloads\FSM_CSV\answers\tbl_fsmpro_hh_answers.csv"
df = pd.read_csv(loc)
df.head()


# In[3]:


#df_mod=df.fillna("NoVal")
#df_mod.head()


# In[88]:


def chatbot(x=input()):
    def get_name():
        return df['q1']
    def get_mob_num():
        return df['q2']
    def get_details():
        name_col = df['q1']
        name = input()
        for i in name_col:
            if i==name:
                return df[df['q1']==name]
    def invalid():
        name_col = df['q1']
        name = input()
        for i in name_col:
            if i==name:
                ab = df[df['q1']==name]
                w = ab.shape
                print(w)
                ab = ab.dropna(axis='columns')
                e = ab.shape
                print(e)
                diff = w[1]-e[1]
                print(diff)
                return ab
    def location():
        name_col = df['q1']
        name = input()
        for i in name_col:
            if i==name:
                
                ab = df[df['q1']==name]
                ab1 = ab['q24']
                ab2 = ab1[0].split(",")
                #print (type(ab1))
                #ab2 = pd.DataFrame(ab1.str.split())
                #ab1 = pd.DataFrame(ab1)
                print("The latitude is ",ab2[0]," and the longitude is ",ab2[1])
                
            
    if x in " show names":
        return get_name()
    if x in " get details":
        return get_details()
    if x in "get mob num":
        return get_mob_num()
    if x in "number of invalid entries":
        return invalid()
    if x in "find location":
        return location()
    


# In[89]:


chatbot("find location")


# In[ ]:





# In[ ]:





# In[ ]:





# In[95]:


name_col = df['q1']
name_list=[]
ab_name=[]
ab_year=[]
x = int(input("enter the number of persons whose graphs need to be found"))
for i in range(x):
    name = input()
    name_list.append(name)
print(name_list)
    
for i in name_list:
    for j in name_col:
        if i == j:
            ab=df[df['q1']==i]
            ab = ab[ab != 0]
            ab1=ab['q1']
            ab_name.append(ab1)
            ab2=ab['q28']
            ab_year.append(ab2)
            
    
print(ab_name)
print(ab_year)
    
    
for i in name_col:
    if i==name:
        ab = df[df['q1']==name]
        ab1 = ab['q24']


# In[ ]:





# In[ ]:





# In[ ]:




