#!/usr/bin/env python
# coding: utf-8

# In[7]:


# a program that list down list of divisors of a given input
numb=int(input("Input your number here:"))
y=[]
for i in range(1,21):
    if numb % i==0:
        y.append(i)
        print(y)
        i+=1
    


# In[10]:


# a program to identify duplicates in two lists and create one list of unique list members
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

final_list=[]
for i in a:
    if i in b:
        final_list.append(i)
        x=list(dict.fromkeys(final_list))#create a dictionary with list values being keys.Dictionaries cannot have
                                       #duplicates
        print(x)
        i+=1


# In[60]:


# Randomly generate two lists to test the above concept
import random
a=[]
b=[]
last_list=[]
a=[random.randint(1,10)for i in range(5)]
b=[random.randint(1,10)for i in range(5)]
x=list(set(a) & set(b))
last_list.append(x)
print(last_list)


# In[46]:


#the lists are of random length between 5 and 15 and of course their elements are random between 1 and 50
# a = [randint(1, 50) for x in range(randint(5, 15))]
b = [randint(1, 50) for x in range(randint(5, 15))]
overlap = list(set(a) & set(b))
print(a, "\n", b, "\n", overlap)

