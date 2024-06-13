#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:07:36 2024

@author: douglast
"""
#importação de bibliotecas

import numpy as np


entrada = np.array([1, 7, 5])

#criando uma lista de peso!
peso = np.array([0.8, 0.1, 0])

#Função soma
def soma(e, p):
    """
OB: Dot sendo usado, retira a necessidade de utilizarmos um " 
def soma(e,p):    
    s = 0
 for i in range(3):
     #print(entrada[i])
     #print(peso[i])
     #vai receber o proprio "s", mais o resultado da multiplicação!
     s += e[i] * p[i]
 return s"    
todo processo e feito de forma automatica, pela biblioteca "e.dot"
    """
    #dot product / produto escalar!
    return e.dot(p)

s = soma(entrada, peso)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0
r = stepFunction(s)