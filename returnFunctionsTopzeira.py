from random import  random


def cara_ou_coroa():
    valor = random()
    if valor > 0.5:
        return 'cara'
    return 'coroa'


print(cara_ou_coroa())


def soma(num1, num2):
    return num1.__add__(num2)


print(soma('a', 'b'))


def soma_sem_parametro(num1, num2=2):
    return num1.__add__(num2)


print(soma_sem_parametro(5))
print(soma_sem_parametro(5, 7))


