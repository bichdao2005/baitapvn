# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:03:17 2024

@author: Bich Dao
Cho 1 ký tự chữ thường. In ra ký tự chữ hoa tương ứng. 
"""
char=input("nhập vào một kí tự thường:")
if char.islower() and len(char)==1:
    print("kí tự chữ in hoa tương ứng:",char.upper())
else:
    print("vui lòng nhập 1 kí tự thường in hoa ")
