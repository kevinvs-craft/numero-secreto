
def idade(ano_nascimento, ano_atual):
    return f'A idade é {ano_atual - ano_nascimento} anos.'


nascimento = int(input('Ano de nascimento: '))
atual = int(input('Ano atual: '))

print(idade(nascimento, atual))

