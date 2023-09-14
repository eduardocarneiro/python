#!/usr/bin/env python
# coding=UTF-8

def soma(*lista):
    total_soma = 0
    print(total_soma)
    for num in lista:
        total_soma += num
    return total_soma

print(soma(1,2,3,4))
