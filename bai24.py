# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:58:45 2024

@author: Bich Dao
BÀI 24. Nhập vào giờ, phút, giây. Kiểm tra xem giờ, phút, giây đó có hợp lệ hay 
không? In kết quả ra màn hình. 

"""
a=int(input("nhập vào giờ:"))
b=int(input("nhập vào phút:"))
c=int(input("nhập vào giây:"))
if 0<=a<24 and 0<=b<=60 and 0<=c<=60 :
  print("thời gian hợp lệ {0}h{1}p{2}s".format(a,b,c)) 
else:
    print("thời gian nhập vào trong hợp lệ")

