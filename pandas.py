#!/usr/bin/env python
# coding: utf-8

# Introduction of Pandas
# pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.
# 
# # Import required library
# 
# import pandas as pd
# After the import command, we now have access to a large number of pre-built classes and functions.
# 
# The primary two components of pandas are the Series and DataFrame.
# 
# A Series is essentially a column, and a DataFrame is a multi-dimensional table made up of a collection of Series.
# 
# Creating DataFrames from scratch
# 
# There are many ways to create a DataFrame from scratch, but a great option is to just use a simple dict.

# In[35]:


import pandas as pd


# In[36]:


data = {
    'apples': [3, 2, 0, 1], 
    'oranges': [0, 3, 7, 2]
}


# And then convert it into pandas DataFrame

# In[37]:


purchases = pd.DataFrame(data)

purchases


# Each (key, value) item in data corresponds to a column in the resulting DataFrame.
# 
# The Index of this DataFrame was given to us on creation as the numbers 0-3, but we could also create our own when we initialize the DataFrame.
# 
# Let's have customer names as our index:

# In[38]:


purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
purchases


# So now we could locate a customer's order by using their name:

# In[39]:


purchases.loc['June'] #return the values at the certain location


# Reading data from CSVs
# 
# Let's go through the process to go from a comma separated values (.csv) file to a dataframe. This variable csv_path stores the path of the .csv, that is used as an argument to the read_csv function.
# 
# The result is stored in the object df, this is a common short form used for a variable referring to a Pandas dataframe.

# In[40]:


# Read data from CSV file


df = pd.read_csv('C:/Users/Farman vcds/Desktop/Nust/titanic_data.csv')
df


# We can use the method head() to examine the first five rows of a dataframe

# In[41]:


# Print first five rows of the dataframe

df.head()


# Check No. of Rows and Colomns in df

# In[42]:


df.shape


# We can check insights of dataframe using describe.

# In[43]:


df


# In[44]:


# checking Numerical data
df.describe() 


# to check categorical stats

# In[45]:


# checking Categorical data
df.describe(include="object")


# To check data types of each coloumn

# In[46]:


df.dtypes


# To check Null Values in dataframe

# In[48]:


df.isnull().sum()


# # Viewing Data and Accessing Data
# You can also get a column as a series. You can think of a Pandas series as a 1-D dataframe. Just use one bracket:

# In[14]:


#  Get the column as a series

x = df['Name']
x


# We can access the column 'Name' and assign it a new dataframe x:

# In[15]:


# Access to the column Name

x = df[['Name']]
x
x = type(df['Name'])
print(x)


# In[16]:


# Get the column as a dataframe

x = type(df[['Name']])
x


# You can do the same thing for multiple columns; we just put the dataframe name, in this case, df, and the name of the multiple column headers enclosed in double brackets. The result is a new dataframe comprised of the specified columns:

# In[50]:


# Access to multiple columns

y = df[['Name','Sex','Age']]
y


# One way to access unique elements is the iloc method, where you can access the 1st row and the 1st column as follows:

# In[18]:


# Access the value on the first row and the first column

df.iloc[0, 0] # index location 'iloc' is used with index


# You can access the 2nd row and the 1st column as follows:

# In[19]:


# Access the value on the second row and the first column

df.iloc[1,0]


# You can access the column using the name as well, the following are the same as above:

# In[20]:


# Access the column using the name

df.loc[0, 'Name']


# You can perform slicing using both the index and the name of the column:

# In[51]:


df


# In[21]:


# Slicing the dataframe

df.iloc[0:2, 0:3]


# # Group By
# Pandas dataframe.groupby() function is used to split the data into groups based on some criteria.

# In[22]:


df


# In[53]:


#apply groupby for a specific column
df.groupby(['Survived','Pclass']).mean()


# In[24]:


#apply groupby for a specific column
df.groupby(['Survived','Pclass'])['Age'].mean()


# # Pivot
# _____________________________________________________________________________________________________________________________
# Reshape data based on column values. Uses unique values from specified index / columns to form axes of the resulting DataFrame

# In[25]:


df.pivot(index='PassengerId', columns='Sex', values='Survived')


# # Pivot Table

# In[26]:


#Single value
pd.pivot_table(df, 
               values='Survived',
               index=['Pclass'],
               columns=['Sex'],
               aggfunc='sum'
              )


# In[27]:


#multiple value
pd.pivot_table(df, 
               values='Survived',
               index=['Pclass','Embarked'],
               columns=['Sex'],
               aggfunc='sum'
              )


# Both pivot_table and groupby are used to aggregate your dataframe. The difference is only with regard to the shape of the result.
# 
# Using pd.pivot_table(df, index=["a"], columns=["b"], values=["c"], aggfunc=np.sum) a table is created where a is on the row axis, b is on the column axis, and the values are the sum of c.
# 
# Example:

# In[28]:


import numpy as np
df = pd.DataFrame({"a": [1,2,3,1,2,3], "b":[1,1,1,2,2,2], "c":np.random.rand(6)})
pd.pivot_table(df, index=["a"], columns=["b"], values=["c"], aggfunc=np.sum)


# Using groupby, the dimensions given are placed into columns, and rows are created for each combination of those dimensions.
# 
# In this example, we create a series of the sum of values c, grouped by all unique combinations of a and b.

# In[29]:


df.groupby(['a','b'])['c'].sum()


# # Melt

# In[30]:


df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
df


# In[31]:


df.melt(id_vars=['A'], value_vars=['B','C'])


# The names of ‘variable’ and ‘value’ columns can be customized:

# In[32]:


df.melt(id_vars=['A'], value_vars=['B'],
        var_name='myVarname', value_name='myValname')


# # Lab Task
# 
# Create a pandas dataframe containing the following data: [2.1, 3.5, 4.2, 5.7, 6.9]. Set the index to ['a', 'b', 'c', 'd', 'e'].

# In[33]:


#Example
df = pd.DataFrame({'Name': {0: 'Abdullah', 1: 'Musa', 2: 'Nouman'},
                   'Address': {0: "Home", 1: "Gutter", 2: "Planet Come "},
                   'Height': {0: 2, 1: 4, 2: 6}})
df


# In[9]:


data ={
    'Name': ['Nadeem hussain'], 
    'age': [23],
    'Gender':['M']
}


# In[10]:


data = pd.DataFrame({'Name': {0: 'Nadeem hussain', 1: 'Musa', 2: 'Nouman'},
                      'age': {0: 23, 1: 30, 2: 70},
                      'Gender': {0: 'M', 1: 'M', 2: 'M'}})


# In[11]:


data


# In[12]:


df = pd.DataFrame(data)
df


# In[13]:


df.shape


# In[14]:


df.iloc[1,1]


# In[15]:


df.replace(3,3)


# In[19]:


df[['age']].sum()


# In[17]:


df

