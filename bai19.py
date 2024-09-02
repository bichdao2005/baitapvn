# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:17:00 2024

@author: Bich Dao
BÀI 19. Nhập vào 4 số nguyên a, b, c, d. In ra màn hình số có giá trị
 nhỏ nhất (không dùng hàm min). 
"""

a=int(input("nhập vào a:"))
b=int(input("nhập vào b:"))
c=int(input("nhập vào c:"))
d=int(input("nhập vào d:"))

snn=a
if b<a:
    snn=b
if c<a:
    snn=c
if d<a:
    snn=d

print("số có giá trị nhỏ nhất trong bốn số là:", snn)
    