
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metro: '))

imc = peso / (altura ** 2)

print(f'O seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com o peso normal')
else:
    print('Você está acima do peso')
