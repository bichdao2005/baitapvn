# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:05:35 2024

@author: Bich Dao
BÀI 27. Viết chương trình tính diện tích và chu vi các hình: hình vuông (v),
 hình chữ nhật (n) và hình tròn (t) với những thông tin được nhập từ bàn phím.  
Ví dụ,  
Nhập hình: n  
Tính P va S của hình chữ nhật 
Nhập chiều rộng = 3 
Nhập chiều dài = 5 
	         Kết quả P = 16  	S = 15       
 

"""

hinh=input("nhập vào hình cần tính diện tích và chu vi: ")
if hinh=='v':
    print("Tính Pvà S của hình vuông")
    a=float(input("nhập vào độ dài cạnh hình vuông: "))
    print("P=",a*4)
    print("S=",a**2)
elif hinh== "n":
    print("Tính P và S của hình chữ nhật")
    b=float(input("nhập chiều rộng:"))
    c=float(input("nhập chiều dài:"))
    print("P=",(b+c)*2)  
    print("S=",b*c)
elif hinh=="t":
    print("Tính P và S của hình tròn")
    r=float(input("nhập vào bán kính đường tròn:"))
    print("P=",r*2*3.14)
    print("S=",r*r*3,14)
else:
    print("không hợp lệ")