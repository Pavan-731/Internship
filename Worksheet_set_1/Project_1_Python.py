#!/usr/bin/env python
# coding: utf-8

# Q.1 Which of the following operators is used to calculate remainder in a division?
# A) # B) &
# C) % D) $
# 
# Ans1.C

# In[4]:


25%2


# Q.2 In python 2//3 is equal to?
# A) 0.666 B) 0
# C) 1 D) 0.67
# Ans2.B

# In[6]:


2//3


# Q.3 In python, 6<<2 is equal to?
# A) 36 B) 10
# C) 24 D) 45
# Ans3. C

# In[7]:


6<<2


# Q.4 In python, 6&2 will give which of the following as output?
# A) 2 B) True
# C) False D) 0
# Ans4. A

# In[8]:


6&2


# Q.5 In python, 6|2 will give which of the following as output?
# A) 2 B) 4
# C) 0 D) 6
# Ans5.D

# In[9]:


6|2


# Q.6 What does the finally keyword denotes in python?
# A) It is used to mark the end of the code
# B) It encloses the lines of code which will be executed if any error occurs while executing the lines of code in 
# the try block.
# C) the finally block will be executed no matter if the try block raises an error or not.
# D) None of the above
# 
# Ans6. C

# Q.7 What does raise keyword is used for in python?
# A) It is used to raise an exception. B) It is used to define lambda function
# C) it's not a keyword in python. D) None of the above
# Ans7. A

# Q.8 Which of the following is a common use case of yield keyword in python?
# A) in defining an iterator B) while defining a lambda function
# C) in defining a generator D) in for loop.
# Ans8. C

# Q.9 Which of the following are the valid variable names?
# A) _abc B) 1abc
# C) abc2 D) None of the above
# Ans9. A and C

# In[12]:


_abc=5+5


# In[13]:


print(_abc)


# In[14]:


1abc=5+5


# In[15]:


abc2=5+5


# In[16]:


print(abc2)


# Q.10 Which of the following are the keywords in python?
# A) yield B) raise
# C) look-in D) all of the above
# Ans10. A and B

# In[ ]:


get_ipython().set_next_input('Q.11 Write a python program to find the factorial of a number');get_ipython().run_line_magic('pinfo', 'number')


# In[20]:


#Ans. 11 Python program to find the factorial of a number provided by the user.

# To take input from the user
num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[ ]:


Q.12 Write a python program to find whether a number is prime or composite.


# In[27]:


#Ans. 12 Program to check if a number is prime or not


# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# In[ ]:


Q.13 Write a python program to check whether a given string is palindrome or not


# In[37]:


# Program to check if a string is palindrome or not

# To take input from the user
my_str = str(input("Enter a word: "))


# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[ ]:


Q.14 Write a Python program to get the third side of right-angled triangle from two given sides.?


# In[39]:


from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", c )


# In[ ]:


Q.15 Write a python program to print the frequency of each of the characters present in a given string.?


# In[42]:


count = 0
# To take input from the user
my_string = str(input("Enter a word: "))

# To take input from the user
my_char = str(input("Enter a Character whose frequency is required: "))

for i in my_string:
    if i == my_char:
        count += 1

print(count)


# In[ ]:




