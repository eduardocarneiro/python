#!/usr/bin/env python
# coding=UTF-8

var1 = 10

def soma():
    global var1 # it define a global variable
    a = 10
    var1 += a

soma()
print var1
