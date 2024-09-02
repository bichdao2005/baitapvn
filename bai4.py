# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:07:48 2024

@author: Bich Dao
"""

"""
Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số. Xuất ra
 màn hình tổng các chữ số của N. Ví dụ: Nhập N=48, kết quả xuất 
 ra màn hình là 4 + 8 = 12 
 """
N=int(input("Nhập vào số nguyên dương N có 2 chữ số: "))
if N>=10 and N<=99:
    print("tổng các chữ số của N:", N//10+N%10)
else:
    print("không xác định")