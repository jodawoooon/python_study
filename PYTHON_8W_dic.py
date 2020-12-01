# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:37:48 2020

@author: DaunJO
"""



## 미션 1. 이미지 반전 프로그램

from cs1media import *

img = load_picture("img.jpg")
w, h = img.size()
for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        r, g, b = 255-r, 255-g, 255-b
        img.set(x, y, (r,g,b))
img.show()


## 미션 2. 이미지를 흑백으로 반전시키기
from cs1media import *


img = load_picture("img.jpg")
w, h = img.size()

for y in range(h):
    for x in range(w):
        
        r, g, b = img.get(x, y)

        avg = (r+g+b)//3
        if avg > 130:
            img.set(x,y,(255,255,255))
        else:
            img.set(x,y,(0,0,0))
img.show()


## 미션 3. 회문 검사하기

def check_palindrome(string):
    
    f = 0
    e = len(string) - 1
    
    while True:
        if f > e:
            return True

        if string[f] != string[e]:
            return False
        
        f += 1
        e -= 1


str = input("문자열을 입력하시오 : ")
str = str.replace(" ", "")

if (check_palindrome(str) == True):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
    
    
    
## 미션 4. 단어 카운터
fname = input("파일 이름 :")
file = open(fname, "r")

table = dict()

for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1
print(table,"\n\n")



for word in table:
    print(word, " : ", end='')
    while True:
        
        if(table[word]==0):
            break
        print("*", end='')
        table[word] -= 1
    print("")

file.close()    
    
    
## 미션 5. 축약어 만들기

table = { "B4": "Before", "TX": "Thanks", "BBL" : "Be Back Later", "BCNU" : "Be Seeing You", "HAND" : "Have A Nice Day" }

msg = input("번역할 문장을 입력하시오 : ")
words = msg.split()
result = ""

for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word
        
print(result)


        
       

# ## 미션 6. csv 파일로부터 딕셔너리로
#파일에서 머릿글은 key 값으로 아래 글은 value 로 값을 분리한다. 

tip = dict()

f = open("D:/tip.csv", "r")
key = []
value = []

for line in f.readlines():
    line = line.strip()
    item = line.split(",")
    if item[0] == 'total_bill':
        
        key = item
        for i in range(0,7):
            tip[key[i]] = []
    else:
        for i in range(0,7):
            tip[key[i]].append(item[i])

    
print(tip)
f.close()


        

  


## 미션 6. csv 파일로부터 딕셔너리로

# import csv

# import pandas as pd
# df = pd.read_csv("D:/tip.csv") #you wanted float datatype
# tip = df.to_dict(orient='list')


# print(tip)
