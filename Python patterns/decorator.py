#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:54:32 2018

@author: sntr
"""
#Structural Pattern

class Decorator:
    
    
    def test(self):
        print("Class method")
    
    @staticmethod
    def static_test():
        print("Static method")
        


x=Decorator()
x.test()
x.static_test()

Decorator.test()
Decorator.static_test()