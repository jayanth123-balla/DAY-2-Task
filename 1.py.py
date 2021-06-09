#!/usr/bin/env python
# coding: utf-8

# In[21]:


age = int(input("Enter the age of person:"))
if (age>18):
    print("Elgible for vote")
else:
    print("Not elgible for vote")


# In[22]:


n=int(input("Enter the number:"))

if (n>0):
    print(n,"is positive")
else:
    print(n,"is negative")


# In[23]:


n=int(input("Enter a Number:"))

if ((n%2==0)&(n%4==0)):
    print(n,"is the even number and divisible by 4")
elif((n%2==0)&(n%4!=0)):
    print(n,"is the even number but not divisible by 4")
else:
    print(n,"is not even number")


# In[24]:


percentage=int(input("Enter the percentage of student:"))

if (percentage>=60):
    print("Distinction")
elif((percentage>=35)&(percentage<=60)):
    print("Pass")
else:
    print("Fail")


# In[25]:


year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"is a leap year")
else:
    print(year, "is not a leap year")


# In[ ]:




