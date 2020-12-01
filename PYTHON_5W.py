## 미션 1. 화면에 거북이 그리기
import turtle

window = turtle.Screen()
window.bgcolor("yellow")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")


size = 20
for i in range(30):
    t.stamp()
    size += 3
    t.forward(size)
    t.right(24)


## 미션 2. 동그라미 그리기

import turtle

t= turtle.Turtle()
t.circle(100)


## 미션 3. 팩토리얼 값 구하기

i = 1
f = 1
factorial = int(input("계산하고자 하는 팩토리얼 값을 입력하세요 : "))

while (i <= factorial):
    f = f * i
    i = i + 1

print(factorial,"!은 %d입니다." % f)


## 미션 4. 최대공약수 계산하기


x = int(input("첫 번째 정수를 입력하세요: "))
y = int(input("두 번째 정수를 입력하세요: "))

if y > x :
    z = x
    x = y
    y = z

while(y!=0):
    r = x % y
    x, y = y, r
print("최대 공약수는 %d이다." % x)


## 미션 5. 계좌번호 처리하기

x = input("계좌번호를 입력하세요 : ")
y = ""

for a in x:
    if a != "-":
        y = y + a
print(y)


## 미션 6. 주사위의 합 확률
from random import randint

count = int(input("주사위 실험 반복횟수 : "))
rollcount = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(count):
    die1 = randint(1,6)
    die2 = randint(1,6)
    rollcount[die1+die2] += 1
    
for i in range(2, 13):
    print(i, rollcount[i])


## 미션 7. 파이 계산

from random import *
from math import sqrt

n = int(input("반복 횟수를 입력하세요 :" ))

inside = 0
for i in range(0, n):
    x = random()
    y = random()
    if sqrt(x*x+y*y)<=1:
        inside+=1
pi = 4*inside/n
print(pi)
