
numero = int(input('\n\nDigite um número: '))
print('A tabuada desse número é:')
for n in range(1, 11):
    print(f'- {n} x {numero} = {numero * n}')
