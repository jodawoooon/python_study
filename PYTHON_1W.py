## day1 미션 1. 자기소개 출력

print("안녕하세요? 여러분")
print("저는 파이썬을 무척 좋아합니다.")
print("9*8은 ",9*8," 입니다. ")
print("안녕히 계세요.")

## day2 미션 1. 간단한 숫자 맞추기 게임

print("숫자게임에 오신 것을 환영합니다.")
a = input("1부터 100 사이의 숫자를 추측해보세요: ")
if int(a) == 62:
    print("맞았습니다.")
else:
    print("틀렸습니다.")
print("게임이 종료되었습니다.")

## day2 미션 2. 자신의 영어 이니셜 쓰기

import turtle

t = turtle.Turtle()

t.forward(100)
t.backward(50)
t.right(90)
t.forward(70)

size = 20
for i in range(4):
    size = size + 3
    t.forward(size)
    t.right(30)

t.penup()
t.right(-210)
t.forward(150)

t.pendown()
t.left(90)
t.forward(130)
t.right(90)

size = 20
for i in range(5):
    t.right(30)
    size = size + 5
    t.forward(size)


t.penup()
t.right(210)
t.forward(100)
t.left(90)
t.forward(130)

t.pendown()
t.backward(50)
size = 15
for i in range(6):

    size = size + 3
    t.backward(size)
    t.left(30)
t.backward(50)

