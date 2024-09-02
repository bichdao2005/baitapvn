# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:59:18 2024

@author: Bich Dao
"""

"""
Viết chương trình nhập vào 2 số nguyên dương a, b, cho biết kết quả chia 
lấy phần nguyên và phần dư của a với b. 
"""
a=int(input("nhập vào a: "))
b=int(input("nhập vào b: "))
pdu=a%b
pnguyen=a//b
if a>0 and b>0:
    print("kết quả chia lấy phần dư: ", pdu)
    print("kết quả lấy phần nguyên :", pnguyen)
else:
    print("không xác định")
    