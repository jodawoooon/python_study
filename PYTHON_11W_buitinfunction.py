# -*- coding: utf-8 -*-
"""
Created on Mon May 25 23:25:19 2020

@author: DaunJO
"""


## 미션 1. 키를 이용한 정렬 예제
class Person(): # 사람 클래스
    def __init__(self, name, age): #생성자 메소드. 이름과 나이 저장
        self.name = name
        self.age = age
        
    def __repr__(self): #객체를 문자열로 return 
        return "<이름: %s, 나이: %d>" % (self.name, self.age)
def Key(person):
    return person.age;
ps = [Person("홍길동", 40), Person("조다운", 24), Person("김길동",30)]
print(sorted(ps, key = Key))

## 미션 2. 피보나치 이터레이터

class Iterator:
    def __init__(self, x=1, y=0, max=1000): #생성자 메소드 정의
        self.x = x
        self.y = y
        self.max = max
        
    def __iter__(self): #이터러블 객체 자신 반환
        return self
    
    def __next__(self): #다음 반복을 위한 값
        n = self.x + self.y # n = 앞 두수의 합
        if n>self.max: 
            raise StopIteration() #max넘기면 예외발생
        self.x = self.y 
        self.y = n # 앞 두수의 합이 바로 뒤의 수열
        return n
    
for i in Iterator():
    print(i, end="  ")
    

## 미션 3. 동전 던지기 게임
    
import random #random 모듈
coinList = ["head", "tail"] 

while(True):
    YesOrNo = input("동전 던지기를 계속 하시겠습니까? yes or no ")
    if YesOrNo == "yes":
        coin = random.choice(coinList) #coinList 시퀀스의 항목 중 랜덤하게 선택.
        print(coin)
    else:
        break
