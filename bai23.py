# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:37:45 2024

@author: Bich Dao
BÀI 23. Giải và biện luận phương trình bậc hai: ax2 + bx + c = 0 
"""
import math
a=float(input("nhập vào a:"))
b=float(input("nhập vào b:"))
c=float(input("nhập vào c:"))
denta=b**2-4*a*c
if a!=0:
    if denta>0:
        x1=((-b)+math.sqrt(denta))/2*a
        x2=((-b)-math.sqrt(denta))/2*a
        print("phương trình có hai nghiệm phân biệt")
        print("x1=",x1)
        print("x2=",x2)
    elif denta==0:
        print("phương trình có nghiệm kép x=",(-b)/(2*a))
    elif denta<0:
        print("phương trình vô nghiệm")
    else:
        print("không xác định")
if a==0:
    print("đây không là phương trình bậc 2")
