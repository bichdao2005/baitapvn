# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:49:00 2024

@author: Bich Dao
BÀI 18. Viết chương trình cho 2 giờ (giờ, phút, giây) và thực hiện cộng, trừ 2 giờ 
này. 

"""
print("nhập vào giờ thứ nhất: ")
a=int(input("nhập vào giờ :"))
b=int(input("nhập vào phút :"))
c=int(input("nhập vào giây :"))
print("nhập vào giờ tứ hai:")
d=int(input("nhập vào giờ :"))
e=int(input("nhập vào phút :"))
f=int(input("nhập vào giây :"))
doigiay1=a*3600+b*60+c
doigiay2=d*3600+e*60+f
cong=doigiay1+doigiay2
tru=doigiay1-doigiay2
gio1=cong//3600
phut1=cong%3600//60
giay1=cong%3600%60

gio2=tru//3600
phut2=tru%3600//60
giay2=tru%3600%60
print("kết quả cộng hai giờ:",gio1,":",phut1,":",giay1)
print("kết quả tru hai giờ:",gio2,":",phut2,":",giay2)

