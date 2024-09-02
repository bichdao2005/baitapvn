# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:50:24 2024

@author: Bich Dao
BÀI 21. Nhập 1 số bất kỳ. Hãy in giá trị (chuỗi) của số nguyên 
đó nếu nó có giá trị từ 0 đến 9, ngược lại thông báo không đọc được.
 Ví dụ, Nhap 1 thì in ra “Mot”. Nhap 10 thì “Khong doc duoc” 

"""
so=int(input("nhập vào số nguyên:"))
so_chuoi=["Không","Một","Hai","Ba","Bốn","Năm","Sáu","Bảy","Tám","Chín"]
if 0<=so<=9:
    print(so_chuoi[so])
else:
    print("không đọc được")
