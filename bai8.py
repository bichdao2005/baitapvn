# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:55:20 2024

@author: Bich Dao


Viết chương trình tính số đo kiểm tra sức khỏe BMI.  
               𝐶â𝑛_𝑛ặ𝑛𝑔  (𝑘𝑔)
Công thức BMI = 	2  (𝑚) 
              𝐶ℎ𝑖ề𝑢_𝑐𝑎𝑜

"""
a=float(input("nhập cân nặng (kg) của bạn : "))
b=float(input("nhập vào chiều cao (m) của bạn: "))
BMI=a/(b*b)
print("số đo kiểm tra sức khỏe của bạn là:" ,BMI)

