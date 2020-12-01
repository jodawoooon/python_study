## 미션 1. 팩토리얼 함수

def fact(n):
    result = 1
    i = 1
    while(i <= n):
        result = result * i
        i = i + 1
        
    print("결과값 : ", result)



x = int(input("팩토리얼을 구하고자 하는 정수값 입력 : "))
fact(x)
print("------------------------------------------------------")

## 미션 2. 소수찾기 함수 - 도전문제
def get_primes(n):
    result = []
    for i in range(2, n+1):
        chk = True
        for j in range(2, i):
            if i%j == 0:
                chk = False
                break
        if chk == True:
            print(i, end=' ')
        

x = int(input("정수 입력 : "))
get_primes(x)
print("")

print("------------------------------------------------------")


## 미션 3. 패스워드 생성기 - 도전문제

import random

def changed_genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    

    while True:
        pw = ""
        for i in range(6):
            index = random.randrange(len(alphabet))
            pw = pw + alphabet[index]

        if any(c.isdigit() for c in pw):
            return pw
            break
           
    
print("패스워드 생성기")
print(changed_genPass())
print(changed_genPass())
print(changed_genPass())
print("------------------------------------------------------")

## 미션 4. 리스트에서 최소값 찾기

def find_minimum(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

list = [7,10,3,5,2]

print("list = ",list)
print("최소값 : ",find_minimum(list))
