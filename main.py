import random

def gera_nove_numeros():
    numeros = []
    for _ in range(9):
        numeros.append(random.randint(1, 9))
    return numeros

def soma_multiplica_digitos(lista, tamanho):
    resultado = 0
    contador = tamanho
    for digito in lista:
        resultado += digito * contador
        contador -= 1
    return resultado

def retorna_digito(soma):
    if (soma * 10) % 11 <= 9:
        return (soma * 10) % 11
    return 0

def saida_formatada(entrada):
    cpf = []
    for indice, valor in enumerate(entrada):
        if indice in [2, 5]:
            cpf.append(f'{valor}.')
        elif indice == 8:
            cpf.append(f'{valor}-')
        else:
            cpf.append(valor)
    return cpf

cpf = gera_nove_numeros()
cpf.append(retorna_digito(soma_multiplica_digitos(cpf, 10)))
cpf.append(retorna_digito(soma_multiplica_digitos(cpf, 11)))

for digito in saida_formatada(cpf):
    print(digito, end='')