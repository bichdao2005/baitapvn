# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:50:23 2024

@author: Bich Dao
BÀI 20. Nhập vào 3 số a, b, c từ bàn phím. In ra màn hình 
số có giá trị lớn nhất (không dùng hàm hỗ trợ). 
"""
a=float(input("nhập vào a:"))
b=float(input("nhập vào b:"))
c=float(input("nhập vào c:"))
maxx=a
if b>a:
    maxx=b
if c>a:
    maxx=c
print("số có giá trị lớn nhất là:", maxx)
