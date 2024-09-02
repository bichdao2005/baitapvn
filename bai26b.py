# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:11:42 2024

@author: Bich Dao
bài 26 (b) Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ 
tự tăng dần. Ví dụ: nhập số 6879 thì in ra số 6789 
"""
N=int(input("nhập vào số nguyên N: "))
N=str(N)
sapxep=sorted(N)
print("số sau khi sắp xếp:",''.join(sapxep))

