## 미션 1. 파티준비
x = int(input("참석자의 수를 입력하시오:"))
a = x*1
b = x*2
c = x*4
print("치킨의 수: ",a)
print("맥주의 수: ",b)
print("케익의 수: ",c)

print("------------------------------------------------------------------")

## 미션 2. 교환 프로그램 작성

x = 10
y = 20
print("x = ",x,",y = ",y)
z = x
x = y
y = z
print("x = ",x,",y = ",y)

print("------------------------------------------------------------------")

## 미션 3. 감자 재배
a = 20
b = 10
c = 40
d = 3
x=a+c*52-d*365-b*52
print("감자의 수 : ",x)

print("------------------------------------------------------------------")

## 미션 4. 복리 계산
x = 24
y = 0.06
z = 382
print("원리금 : ",x*(1+y)**z)

print("------------------------------------------------------------------")

## 미션 5. 등산 시간 계산

from math import *

a=10/20
h = sqrt(3**2+4**2)
b=h/10
c=h/30
d=8/20
print("주행 시간 : ",a+b+c+d)

print("------------------------------------------------------------------")

## 미션 6. 구의 부피
r = 5
x = 4/3*3.141592*r**3
print("구의 부피 : ",x)

print("------------------------------------------------------------------")

## 미션 7. 별까지 거리 계산
x = 40*10**12
y = 299792458/1000
z = (x/y)
print("시간(년) : ",z/(60*60*24*365))

print("------------------------------------------------------------------")

## 미션 8. 자동판매기 프로그램
x = int(input("물건값을 입력하시오 : "))
a = int(input("1000원 지폐 개수 : "))
b = int(input("500원 동전 개수 : "))
c = int(input("100원 동전 개수 : "))
y = a*1000+b*500+c*100-x

c500 = y//500
y = y%500

c100 = y//100
y = y%100

c10 = y//10
y = y%10

c1 = y

print("500원= ",c500," 100원= ",c100," 10원= ",c10," 1원= ",c1)

print("------------------------------------------------------------------")
