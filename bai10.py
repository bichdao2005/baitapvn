# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:33:21 2024

@author: Bich Dao
BÀI 10. Cho số xe (gồm 4 chữ số) của bạn. Cho biết số xe của bạn được mấy nút? 
"""

a=int(input("nhập số xe của bạn:"))
b=a//1000
c=(a%1000)//100
d=(a%1000)%100//10
e=(a%1000)%100%10
sonut=b+c+d+e
if sonut>=10:
    print("số nút xe của bạn là:",sonut//10+sonut%10)
elif sonut<10:
    print("số nút xe của bạn là:", sonut)
else:
    print("không xác định")