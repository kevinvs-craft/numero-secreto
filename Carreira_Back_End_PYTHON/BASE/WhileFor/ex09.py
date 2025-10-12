
while True:
    nome = input('Nome: ')
    senha = input('Senha: ')
    if len(nome) < 5:
        print('O nome tem que ter mais de 5 caracteres!')
    elif len(senha) < 8:
        print('Senha tem que ter mais de 8 caracteres')
    else:
        print('Cadastro realizado com sucesso!')
        break

