from functools import reduce


#Lambada
def valor(num):
    return lambda: num * 3

def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    result = valor(num)()
    print(result)

print(funcao_quadratica(1, 2, 3)(2))


print(list(map(lambda num: num * 2, numeros)))
####

#Filter()
print(list(filter(lambda num: num > 3, numeros)))

usuarios = [
    {"username": "Neto", "tweets": ["seis são uns zé ruela", "Lucas lima não tem gol"]},
    {"username": "Neymar", "tweets": ["te amo bruninha"]},
    {"username": "Luxa", "tweets": []},
    {"username": "Renata Fan", "tweets": []},
    {"username": "Fred12", "tweets": ["Vou chorar"]},
    {"username": "Bolivia", "tweets": []}
]

print(usuarios[0])

for usuario in usuarios:
    if usuario['username'] == 'Fred12':
        print(usuario)


user = usuarios[5]
boleano = user['tweets']
if not boleano:
    print(boleano)

inativos = list(filter(lambda user: not user['tweets'], usuarios))
print(inativos)
###

#Reduce
print(reduce(lambda x, y: x * y, numeros))
####

#Sorted
print(sorted(numeros, reverse=True))

print(sorted(usuarios, key=len))

###

#MAX e MIN
"""
max1 = int(input('Coloca um numero ai'))
max2 = int(input('Coloca outro numero ai'))

print(max(max1, max2))
"""


musicas = [
    {"Cantor": "Gabriel Elias", "Musica": "Guarde com voce", "Tocou": 10},
    {"Cantor": "Ivo Mozart", "Musica": "A gente so precisa acreditar", "Tocou": 8},
    {"Cantor": "Gustavo Mioto", "Musica": "Com ou sem mim", "Tocou": 2},
    {"Cantor": "Tiago Iorc", "Musica": "Pode se achegar", "Tocou": 6},
    {"Cantor": "Forfun", "Musica": "Morada", "Tocou": 3}
]

print(max(musicas, key=lambda musica: musica['Tocou'])['Musica'])
print(min(musicas, key=lambda musica: musica['Tocou'])['Musica'])

max = 0
min = 100

for musica in musicas:
    if musica['Tocou'] > max:
        max = musica['Tocou']
    elif musica['Tocou'] < min:
        min = musica['Tocou']


print(max)
print(min)

###

