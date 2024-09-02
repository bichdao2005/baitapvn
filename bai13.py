# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:16:18 2024

@author: Bich Dao
Nhập lần lượt ngày, tháng, năm sinh. Sau đó xuất ra theo định dạng sau: 
a)	Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990) 
b)	Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90) 
c)	Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20) 
(Sau đó làm ngược lại) 
"""
day=int(input("nhập vào ngày:"))
month=int(input("nhập vào tháng:"))
year=int(input("nhập vào năm:"))
print("câu a")
print("{0}/{1}/{2}".format(day,month,year))
print("{0} {1} {2}".format(day,month,year))
print("câu b")
year2=year%100
print("{0}/{1}/{2}".format(day, month,year2))
print("{0} {1} {2}".format(day, month,year))
print("câu c")
print("{0}/{1}/{2}".format(year,month,day))
print("{0} {1} {2}".format(year,month,day))



