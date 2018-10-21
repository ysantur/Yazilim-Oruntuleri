# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:19:59 2018

@author: ysantur@gmail.com
"""

#Creational
"""
Sınıfları bir interface yada sınıftan türeterek oluşturma işlemidir.
Genişletilebilir.
Sınıf sayısının çok olduğu durumda kullanışlıdır.
"""

class Person:
    def __init__(self):
        self.name = None
        self.gender = None
    
    def getName(self):
        return self.name

    def getGender(self):
        return self.gender
    
class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)
        
class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)
        
class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    list=[["Ali","M"], ["Sena","F"], ["Nurettin","M"]]
    for i in list:
        person = factory.getPerson(i[0], i[1])

