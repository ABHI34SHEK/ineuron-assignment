#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1
# 

# In[1]:


b=[]
for i in range(2000,3200):
    if (i%7==0 and i%5!=0):
        b.append(i)
print(b)


# # Question 2

# In[2]:


a = input("first name")
b = input("last name")
print(a+" "+b)


# # Question 3

# In[3]:


r = 12/2
pie = 3.14
volume_of_sphere = 4/3*pie*r*r*r
print(volume_of_sphere)

