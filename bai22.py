# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:25:31 2024

@author: Bich Dao
BÀI 22. Giải và biện luận phương trình bậc nhất: ax + b = 0 
"""
a=float(input("nhập vào a:"))
b=float(input("nhập vào b:"))
if a==0 and b==0:
    print("phương trình có vô số nghiệm")
elif a==0 and b!=0:
    print("phương trình vô nghiệm")
elif a!=0 :
    print("phương trình có nghiệm là x=",-b/a)
else:
    print("không xác định")
