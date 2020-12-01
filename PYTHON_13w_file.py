# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 19:05:13 2020

@author: DaunJO
"""
## 미션 1. 매출 파일 처리sale

inputfile = input("입력 파일 이름: ");
outputfile = input("출력 파일 이름: ");

infile = open(inputfile, "r")
outfile = open(outputfile, "w")

sum = 0
count = 0

for line in infile:
    sale = int(line)
    sum = sum + sale
    count += 1
    
outfile.write("총 매출 = "+ str(sum)+"\n")
outfile.write("평균 일 매출 = "+str(sum/count))

infile.close()
outfile.close()

## 미션 2. 스페이스 세기
def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    for line in infile:
        spaces += line.count(' ')
        tabs += line.count('\t')
    infile.close()
    
    return spaces, tabs

filename = input("파일 이름을 입력하시오: ");
spaces, tabs = parse_file(filename)
print("스페이스 = %d, 탭 = %d" % (spaces, tabs))

## 미션 3. 줄앞에 번호붙이기
infile = open("proverbs.txt")
outfile = open("output.txt", "w")
i = 1
for line in infile:
    outfile.write(str(i)+": "+line)
    i += 1
infile.close()
outfile.close()

## 미션 4. 각 문자 횟수 세기
filename = input("파일명을 입력하세요 : ").strip()
infile = open(filename, "r") #파일열기

freqs = {}

for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char] += 1 #char이 사전에 있으면 하나 증가
        else:
            freqs[char] = 1 #char이 사전에 없으면 1로 초기화

print(freqs)
infile.close()



## 미션 5. CSV 파일 읽기
f = open("C:\\test.csv", "r")
for line in f.readlines():
    line = line.strip()
    pirnt(line)
    parts = line.split(",")
    for part in parts:
        print("  ", part)
        
        
## 미션 6. 파일 암호화
        
key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    result = ''
    
    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result.lower()
    
    
def decrypt(n, ciphertext):
    result = ''
    
    for l in ciphertext:
        try:
            i =(key.index(l)-n)%26
            result += key[i]
        except ValueError:
            result += l
    return result

n = 3
text = 'the language of truth is simple.'
encrypted = encrypt(n, text)

decrypted = decrypt(n, encrypted)
print('평문 : ',text)
print('암호문: ',encrypted)
print('복호문: ', decrypted)



## 미션 7. 이미지 파일 복사하기
f1 = input("원본 파일 이읆을 입력하시오: ");
f2 = input("복사 파일 이름을 입력하시오: ");
infile = open(f1, "rb")
outfile = open(f2, "wb")
while True:
    copy = infile.read(1024)
    if not copy:
        break
    outfile.write(copy)
    
infile.close()
outfile.close()
print(f1+"를 "+f2+"로 복사하셨습니다. ")