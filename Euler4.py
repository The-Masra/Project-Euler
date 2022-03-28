#!/usr/bin/env python
# coding: utf-8

# ## Largest palindrome product
# Problem 4
# 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.
# 

def palindrome(x):
    
    '''
    for example :
    3 digit upperlimit is 999 and lowerlimit is 100
    
    '''
    upperlimit = (10**x) - 1  
    lowerlimit = 1 + upperlimit//10
    print("Upperlimit is {} and Lowerlimit is {}".format(upperlimit, lowerlimit))
    n =0
    for a in range(upperlimit, lowerlimit, -1):
        for b in range(a, lowerlimit, -1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]:
                    n = a * b
                    print("a is {}, b is {}".format(a,b))

    print(n)

    
x = int(input(print("Enter n-Digit of number you want to create Largest Palindrome:") ))
palindrome(x)

