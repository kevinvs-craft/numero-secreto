estoque = 5
for l in range(estoque):
    estoque -= 1
    print(f'Venda realizada! Estoque restante: {estoque}')
    if estoque == 0:
        print('Estoque esgotado')
    