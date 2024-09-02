# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:48:29 2024

@author: Bich Dao


Nhập vào bán kính của hình tròn, tính và in ra chu vi,
 diện tích của hình tròn đó. 
"""
import math
r=int(input("nhập vào bán kính của hình tròn: "))
c=r*2*math.pi
s=r**2*math.pi
print("chu vi của hình tròn: ",c)
print("diện tích của hình tròn là: ",s)

