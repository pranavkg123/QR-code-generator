# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XcDJ8TubBL6nx_9arnzEZkUFZbYJr9QY
"""

def calc ():
  a=int(input("enter the 1st number:"))
  b=int(input("enter the 2nd number:"))
  result=(input("enter the operation:"))
  if result=="+":
    print(a+b)
  elif result=="-":
    print(a-b)
  elif result=="*":
    print(a*b)
  elif result=="/":
    print(a/b)
  elif result=="%":
    print(a%b)
  elif result=="//":
    print(a//b)
  elif result=="":
    print(a**b)
  else:
    print("invalid operation")
  print(result)

calc()