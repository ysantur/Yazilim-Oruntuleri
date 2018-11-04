#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:59:12 2018

@author: sntr
"""

class Test:

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x
    
    
t=Test()
#t.__x=2

t.set_x(5)
print(t.get_x())