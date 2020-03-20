def cont_num(max_value):
    cont = 1
    while cont <= max_value:
        yield cont
        cont = cont + 1
        
gen = cont_num(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(type(gen))

print(sum(num for num in range (200)))

def fib_gen(max):
    current, nextNum, cont = 0, 1, 0
    while cont < max:
        current, nextNum = nextNum, current + nextNum
        yield current
        cont = cont + 1
    
for n in fib_gen(10):
    print(n)