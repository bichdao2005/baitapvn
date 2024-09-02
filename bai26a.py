# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:10:14 2024

@author: Bich Dao
BÀI 26. (a) Cho ba số a, b, c được nhập vào từ bàn phím. Hãy in ra màn hình theo 
thứ tự tăng dần các số (Chỉ dùng 1 biến phụ). 

"""
a=float(input("nhập vào a:"))
b=float(input("nhập vào b:"))
c=float(input("nhập vào c:"))
if a>b:
    a, b = b, a  
if b>c:
    b, c = c, b  
if  a>b:
    a, b = b, a  
print("thứ tự tăng dần là {0},{1},{2}".format(a,b,c))
