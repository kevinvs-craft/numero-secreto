
total_value = 0
initial_value = float(input('Valor da despesa? '))
total_value += initial_value
if initial_value != 0:
    while True:
        new_value = float(input("Valor da despesa? "))
        if new_value == 0:
            break
        total_value += new_value

print(f'Despesas totais: -{str(total_value)}')



