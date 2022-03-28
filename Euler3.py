#!/usr/bin/env python
# coding: utf-8

# ## Largest prime factor
# 
# Problem 3
# 

# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

# In[30]:


def max_prime_factor(num):
    
    check = 1
    for i in range(1, int(num/2), 2):
        
        if num % i == 0:
            print("One of our factor is :", i)
            check = check * i
            print(check)

        if num == check:
            print("Largest prime factor of ",num , " is :",i)
            break
            
    



max_prime_factor(600851475143)

