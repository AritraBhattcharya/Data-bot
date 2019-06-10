#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics
#url= "https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/898a40b035f7c951579041aecbfb2149331fa9f6/mtcars.csv"
#df1=pd.read_csv(url)
#df1.rename(columns={'Unnamed: 0':'Car Name'},inplace=True)
#df1.head()


loc = r"C:\Users\Aritra\Downloads\FSM_CSV\answers\tbl_fsmpro_hh_answers.csv"
df = pd.read_csv(loc)
df.head()


# In[9]:


#df1.sample(n=2,axis=1)


# In[2]:


print(pd.DataFrame(df.columns))


# In[4]:


lst=[]

x=int(input("The number of columns you want to select : "))
for i in range(x):
    k=input("Give the col name: ")
    if k in df.columns:
        lst.append(df[k])
        #print(df[k])
#df[df[k==df.columns()]]


#for i in range(x):
    #print("The column selected are :")
    #print(lst[i].values)
        
        
    
    
    



# In[135]:


print("The columns selected are :")
lst = pd.DataFrame(lst).T
lst


# In[136]:


print('''Arithmetic operations available to be performed are : 
                 
                1.Mean
                2.Median
                3.Max
                4.Min
                5.Sort
                6.Summary
                7.Range
                ''')
      


# In[137]:


def perform(argument): 
    switcher = { 
        1: lambda: print(lst[col].mean()),
        2: lambda: print(lst[col].median()),
        3: lambda: print(lst[col].max()),
        4: lambda: print(lst[col].min()),
        5: lambda: print(lst[col].sort_values()),
        6: lambda: print(lst[col].describe()),
        7: lambda: print(lst[col].min(),lst[col].max())
        
    }
    return switcher.get(argument, lambda: "nothing") ()


# In[138]:


op=int(input("Enter the operation you want to perform : "))
col=input("Enter the column you want to select :")
if col in df.columns:
    perform(op)
else:
    print("Invalid entry")


# In[15]:


'''my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}

def disp_table():
  
        return str(df1.head().values)'''


# In[139]:


print('''The arithemtic operations that can be performed are :
            1. Correlation
            2. Standard Deviation
            3. Variance
            ''')


# In[140]:


lst['q2'].std()


# In[176]:


x1=df['q1']
x2=df['q2']
x3=df['surveyid']
x4=pd.DataFrame(x1,x2,x3)
print(x4.corr())


# In[163]:


def cor():
    x1=df[x1]
    x2=df[x2]
    x3=pd.DataFrame(x1,x2)
    print(x3.corr())


def stddev():
    return df[col].std()



def a_perform(argument): 
    switcher = { 
        1: lambda: cor(),
        2: lambda: print(lst[col_1].std()),
        3: lambda: print(lst[col].max()),
        4: lambda: print(lst[col].min()),
        5: lambda: print(lst[col].sort_values()),
        6: lambda: print(lst[col].describe()),
        7: lambda: print(lst[col].min(),lst[col].max())
        
    }
    return switcher.get(argument, lambda: "nothing") ()


# In[162]:


a_op=int(input("Enter the operation you want to perform : "))
if a_op == 1:
    print("Enter the 2 columns in which correlation needs to be found out")
    x1=(input("Enter Column 1 :"))
    x2=(input("Enter Column 2 :"))
else:
    col_1=input("Enter the column you want to select :")
    if col_1 in df.columns:
        a_perform(a_op)
    else:
        print("Invalid entry")


# In[ ]:


def chatbot(x=input()):
    def disp_table():  
        return df1.head()
    def visuals():  
        return df1.corr()
    def dev():
        return df1.std()
    def var():
        return df1.var()
    def rug():
        return sns.rugplot(df1['disp'])
    def group_boxplot():
        sns.set(style="ticks", palette="pastel")
        a4_dims = (11.7, 8.27)
        sns.despine(offset=10, trim=True)
        sns.boxplot(x="Car Name", y="mpg", palette=["m", "g"],data=df1)
    def jointplot():
        return sns.jointplot(df1['mpg'], df1['disp'], kind="kde", height=7, space=0)
    def horizontal_barplot():
        f, ax = plt.subplots(figsize=(6, 15))
        return sns.barplot(x="disp", y="mpg", data=df1, color="b")

    if x in " city level information ":
        return disp_table()
    if x in " visual":
        return visuals()
    if x in " dev":
        return dev()
    if x in " varriance":
        return var()
    if x in " rugplot":
        return rug()
    if x in " jointplot":
        return jointplot()
    if x in " hor_plot":
        return horizontal_barplot()
    if x in " group_boxplot":
        return group_boxplot()


# In[6]:


chatbot("disp_table")

