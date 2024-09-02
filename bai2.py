# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:51:47 2024

@author: Bich Dao
"""
"""
 Viết chương trình nhập vào 2 số nguyên a, b. Tính tổng, hiệu, tích, 
 thương của 2 số trên và in kết quả ra màn hình. Kết quả phép chia làm tròn 
 2, 3 chữ số sau dấu chấm (ví dụ kết quả 3.333333 thì làm tròn 3.333). 
 """
a=int(input("nhập vào số nguyên a: "))
b=int(input("nhập vào số nguyên b: "))
tong=a+b
hieu=a-b
tich=a*b
thuong=a/b
print("tổng:",tong)
print("hiệu:",hieu)
print("tích: ", tich)
print("thương:",round(thuong,3))
 