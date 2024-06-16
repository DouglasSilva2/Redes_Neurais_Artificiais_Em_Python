#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:45:55 2024

@author: douglast
"""

import numpy as np

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0,0,0,1])

"""Pessos para nosso treinamento"""
pesos = np.array([0.0, 0.0])
"""Taxa de aprendizagem que nosso modelo"""
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

"""Vai receber como parametro os registro, depois vai fazer o samatorio e passar 
para stepFunction o resultado!!
"""
def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    """Inicar um loop em 1"""
    while (erroTotal != 0): #enquanto meu erro for diferente de "0"
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asanyarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))
        

        
treinar()