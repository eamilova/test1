# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_MwHyRfQQYsW21dUo1cPsNKs5KXF9qad
"""

a = int(input())
b = int(input())
a1 = a // 1000
b1 = a // 100 % 10
while (((a1 * 10 + b1) * 10 + b1) * 10 + a1) <= b:
    p=str(a1)
    k=str(b1)
    print(p+k+k+p)
    b1 = b1 + 1
    if ( b1 > 9):
        a1 = a1 + 1
        b1 = 0