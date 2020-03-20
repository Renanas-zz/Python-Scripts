def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y


def calc(num1, num2, function):
    return function(num1, num2)

print(calc(1, 2, sum))
print(calc(2, 3, sub))
print(calc(4, 2, div))
print(calc(4, 5, mult))
    

def be_polite(funcao):
    def being():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um bom dia!')
    return being

@be_polite        
def introducing():
    print('Meu nome é Renan')

introducing()