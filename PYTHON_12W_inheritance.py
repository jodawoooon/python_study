# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:56:38 2020

@author: DaunJO
"""

## 미션 #1: Sportscar 클래스
#일반적인 자동차를 나타내는 클래스인 Car 클래스를 상속받아서 
#수퍼카를 나타내는 클래스인 SportsCar를 작성하는 것이 쉽다. 
#다음 그림을 참조하여 Car 클래스와 SportsCar 클래스를 작성해보자

class Car:
    def __init__(self, speed):
        self.speed = speed
        
    def setSpeed(self, speed):
        self.speed = speed
        
    def getDesc(self):
        return "차량 =(" + str(self.speed) + ")"
        
class SportsCar(Car):
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.turbo = turbo
        
    def setTurbo(self, turbo):
        self.turbo = turbo
        


car = SportsCar(10, True)
print(car.getDesc())
car.setTurbo(False)
print("================================")

## 미션 #2 : 도형
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        print("area")
        
    def perimeter(self):
        print("perimeter")

class Rectangle(Shape): #Shape클래스 상속받아 작성
    def __init__(self, x, y, w, h):
        super().__init__(x, y) #부모 클래스 생성자 호출
        self.w = w
        self.h = h
        
    def area(self): #area()오버라이드
        return self.w*self.h
    
    def perimeter(self):
        return 2*(self.w+self.h)
    
r = Rectangle(1,1,10,20) #객체 생성
print("면적 ",r.area())
print("둘레 ",r.perimeter())
print("================================")
## 미션 #3: 학생과 강사

class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        
class Student(Person):
    
    stclass = []
    gpa = 0
    
    def __init(self, name, number):
        super().__init__(name, number)

        
    def setClass(self, stclass):
        self.stclass.append(stclass)
        
    def __str__(self):
        return "이름="+self.name+"\n주민번호="+self.number+"\n수강과목="+str(self.stclass)+"\n평점="+str(self.gpa)
    
    
class Teacher(Person):
    tcclass = []
    salary = 3000000
    def __init(self, name, number):
        super().__init__(name, number)

        
    def setClass(self, tcclass):
        self.tcclass.append(tcclass)
        
    def __str__(self):
        return "이름="+self.name+"\n주민번호="+self.number+"\n강의과목="+str(self.tcclass)+"\n월급="+str(self.salary)
    
st = Student("홍길동", "12345678")
st.setClass("자료구조")
print(st)

    
tc = Teacher("김철수", "12349939")
tc.setClass("Python")
print(tc)
print("================================")


##미션 #4: 은행 계좌
class BankAccount:
    def __init__(self, name, number, balance):
        self.balance = balance
        self.number = number
        self.name = name
        
    def deposit(self, incomming):
        self.balance += incomming
        return self.balance

    def withdraw(self,outcomming):
        if outcomming > self.balance:
            print("잔액이 부족합니다.")
        else :
            self.balance -= outcomming
            
class SavingsAccount(BankAccount):
    def __init__(self, name, number, balance, interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate
    
    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate
        
    def get_interest_rate(self):
        return self.interest_rate
    
    def add_interest(self):
        self.balance += self.balance * self.interest_rate #예금에 이자 더하기
    
class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withdraw_charge = 10000 #수수료
        
    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount+self.withdraw_charge)
    
al = SavingsAccount("홍길동", 123456, 10000, 0.05)
al.add_interest()
print("저축 예금의 잔액=", al.balance)

a2 = CheckingAccount("김철수", 123457, 2000000)
a2.withdraw(100000)
print("당좌예금의 잔액 =", a2.balance)
print("================================")


##미션5. 직원과 매니저

class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def getSalary(self):
        return salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        
    def getSalary(self):
        salary = super().getSalary()
        return salary + self.bonus
    
    def __repr__(self):
        return "이름 : "+self.name+"; 월급: "+str(self.salary)+"; 보너스: "+str(self.bonus)
    
kim = Manager("김철수", 2000000, 1000000)
print(kim) # __repr__() 호출
print("================================")



## 미션6. Vehicle과 Car, Truck

class Vehicle:
    def __init__(self, name):
        self.name = name
    def drive(self):
        raise NotImplementedError("이것은 추상메소드입니다. ") #구현되지 않았다는 예외 발생
        
    def stop(self):
        raise NotImplementedError("이것은 추상메소드입니다. ")
        
class Car(Vehicle):
    def drive(self):
        return '승용차를 운전합니다'
    def stop(self):
        return '승용차를 정지합니다'
    
class Truck(Vehicle):
    def drive(self):
        return '트럭을 운전합니다'
    def stop(self):
        return '트럭을 정지합니다'
    
cars = [Truck('truck1'), Truck('truck2'), Car('car1')]

for car in cars:
    print(car.name + ': ' + car.drive())
print("================================")

## 미션7. Card와 Deck
    
class Card:
    suitNames = ['클럽', '다이아몬드', '하트', '스페이드']
    rankNames = [None, '에이스', '2', '3', '4', '5', '6', '7', '8', '9', '10', '잭', '퀸', '킹']
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return Card.suitNames[self.suit]+" "+Card.rankNames[self.rank]
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
                
    def __str__(self):
        lst = [str(card) for card in self.cards]
        return str(lst)

deck = Deck()
print(deck)
