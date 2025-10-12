
a = int(input('Informe os dias para a atividade A: '))
b = int(input('Informe os dias para a atividade B: '))
c = int(input('Informe os dias para a atividade C: '))

if a < 0 or b < 0 or c < 0:
    print('Erro! Não pode haver números negativos!')
else:
    print(f'O tempo total de trabalho é {a + b + c}')
