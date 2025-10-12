
numeros = (10, 30, 22, 33, 10)
soma = 0
try:
    for n in numeros:
        soma += n
    print(soma)
except Exception as e:
    print(f'Erro! {e}')

