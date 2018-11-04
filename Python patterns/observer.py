#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 21:15:20 2018

@author: sntr
"""
#Observer Behavioural pattern 
#Herbir thread gözlemci gibi çalışır, olay tetiklendiğinde çıktıyı yazdırır yada başka bir iş yapar
import threading
import time
import pdb

class Downloader(threading.Thread):
   
   def run(self):
      print ('downloading')
      for i in range(1,5):
         self.i = i
         time.sleep(2)
         print('unfunf')
         return 'hello world'

class Worker(threading.Thread):
   def run(self):
      for i in range(1,5):
         print('worker running: %i (%i)' % (i, t.i))
         time.sleep(1)
         t.join()

         print('done')

t = Downloader()
t.start()

time.sleep(1)

t1 = Worker()
t1.start()

t2 = Worker()
t2.start()

t3 = Worker()
t3.start()