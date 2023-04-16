# Name - Abhishek G. Bendre
"""
Project - 1
Python Program To Creat A Random Password Generator
"""

import random
import string

print(" <<~|*|~>> Welcome to Random Password Generator <<~|*|~>> ")


def my_fuction():
    length=int(input("Enter the length of password you want : "))
    lowerData=string.ascii_lowercase
    upperData=string.ascii_uppercase
    digitData=string.digits
    symbolsData=string.punctuation
    combine=lowerData+upperData+digitData+symbolsData
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    my_fuction()
    
my_fuction()