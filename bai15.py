# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:25:04 2024

@author: Bich Dao
"""

a=float(input("nhập số a:"))
b=float(input("nhập số b:"))
A=a+b
B=a**(1/3)+b**(1/3)
C=(a*b)**(1/3)
D=(a**(1/3)- b**(1/3))**2
print("biểu thức sau có kết quả là ", ((A/B)-C)/D)