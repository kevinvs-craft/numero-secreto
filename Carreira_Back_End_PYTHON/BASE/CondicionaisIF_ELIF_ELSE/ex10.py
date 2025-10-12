
renda = float(input('Renda mensal: '))
parcela = float(input('Valor da parcela: '))

if parcela <= renda / 3:
    print('Empréstimo aprovado')
else:
    print('Emprestimo negado: parcela acima de 30% da renda')
