x = float(input('valor de x: '))
y = float(input('valor de y: '))

if x > 0 and y > 0:
    print('Primeiro Quadrante: ')
elif x < 0 and y > 0:
    print('Segundo Quadrante: ')
elif x < 0 and y < 0:
    print('Terceiro Quadrante: ')
elif x > 0 and y < 0:
    print('Quarto Quadrante: ')
else:
    print('ponto está localizado no eixo ou origem')
