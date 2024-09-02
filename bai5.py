# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:12:44 2024

@author: Bich Dao
"""

"""
Viết chương trình cho phép nhập vào giờ, phút và giây theo định dạng
 hh:mm:ss. Hãy đổi ra giây và in kết quả ra màn hình. 
 """
 
hh=int(input("nhập giờ: "))
mm=int(input("nhập phút: "))
ss=int(input("nhập giây: "))
print("{0}:{1}:{2}".format(hh,mm,ss))
print("đổi ra giây", hh*60*60+mm*60+ss)