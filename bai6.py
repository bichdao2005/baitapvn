# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:36:59 2024

@author: Bich Dao
"""

"""
Viết chương trình nhập vào năm sinh, in ra tuổi. 
Ví dụ nhập 1988 in ra (giả sử năm hiện tại là 2022):  
Ban sinh nam 1988 vay ban 33 tuoi. 
"""

ns=int(input("nhập vào năm sinh: "))
tuoi= 2022-ns
if ns<=2022 and ns>0 :
    print(f"bạn sinh năm {ns} vậy bạn {tuoi}.")
else:
    print ("không xác định ")
    