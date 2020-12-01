# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:04:39 2020

@author: DaunJO
"""


## 미션 1. 자동차 클래스 작성

class Car:
    def __init__(self, speed=0, gear=1, color="white", efficiency=0):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
        self.__efficiency = efficiency
        
    #getters
        
    def getSpeed(self):
        return self.__speed
    
    def getGear(self):
        return self.__gear
    
    def getColor(self):
        return self.__color
    
    def getEfficiency(self):
        return self.__efficiency
    
    #setters
    
    def setSpeed(self, speed):
        self.__speed = speed
        
    def setGear(self, gear):
        self.__gear = gear
        
    def setColor(self, color):
        self.__color = color
        
    def setEfficiency(self, efficiency):
        self.__efficiency = efficiency
        
    def cal_fuel(self, distance):
        #주행거리(distance)를 입력받는다.
        #연비는 주행거리/소모되는 연료량이다.
        #따라서 지정된 거리를 주행하는데 필요한 연료의 양은
        fuel = distance/self.__efficiency
        print(distance,"km를 주행하는데 필요한 연료 : ",fuel)
    
    def __str__(self):
        
        return '(%d, %d, %s, %d)' % (self.__speed, self.__gear, self.__color, self.__efficiency)

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.setEfficiency(8) #연비 = 8
myCar.cal_fuel(30) #주행거리 = 30km

print(myCar)
print("========================================================")

## 미션 2. 연락처 클래스 작성

class ContactInfo:
    def __init__(self, name, age, email, phone, address):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address
        
    #getters
        
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getAddress(self):
        return self.address
    
    #setters
    
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setEmail(self, email):
        self.email = email
    def setPhone(self, phone):
        self.phone = phone
    def setAddress(self, address):
        self.address = address
        
    def __str__(self):
        return '(%s, %d, %s, %s, %s)' % (self.name, self.age, self.email, self.phone, self.address)
        
contact = ContactInfo("조다운", 24, "abc@cbnu.ac.kr", "010-0000-0000", "경기도 의왕시")
print(contact)
        
    
        