
distancia = int(input('Distância: '))
valor = 0

if distancia <= 100:
    valor += 10
elif distancia > 200:
    valor += 30
else:
    valor += 20

print(f'Valor do pedágio: R$ {valor},00')
