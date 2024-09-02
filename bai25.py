# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:58:46 2024

@author: Bich Dao
BÀI 25. Nhập 1 chữ cái, nếu là chữ thường thì đổi thành chữ hoa,
 ngược lại đổi thành chữ thường. 
"""
a=input("nhập vào 1 chữ cái:")
if a.islower():
    print(a.upper())
else:
    print(a.lower())