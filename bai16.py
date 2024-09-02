# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:36:43 2024

@author: Bich Dao
b16 :Viết chương trình đổi từ giờ/phút/giây thành giây. 
Ví dụ, nhập 1h8p8s thì in ra 4088 giây 

"""
h=int(input("nhập giờ:"))
p=int(input("nhập phút:"))
s=int(input("nhập giây:"))
print("{0}h{1}p{2}s".format(h,p,s))
print("đổi ra giây :", h*60*60+p*60+s)

