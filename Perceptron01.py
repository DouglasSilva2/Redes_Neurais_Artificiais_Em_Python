#Criando uma lista de entrada

entrada = [1, 7, 5]

#criando uma lista de peso!
peso = [0.8, 0.1, 0]

#inicio da função para varer a lista!
def soma(e, p):
    s = 0
    for i in range(3):
        #print(entrada[i])
        #print(peso[i])
        #vai receber o proprio "s", mais o resultado da multiplicação!
        s += e[i] * p[i]
    return s
s = soma(entrada, peso)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0
r = stepFunction(s)