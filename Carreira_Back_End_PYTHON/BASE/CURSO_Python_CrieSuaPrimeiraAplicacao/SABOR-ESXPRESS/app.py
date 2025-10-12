import os

restaurantes = [{'nome': 'pisadao', 'categoria': 'Brasileiro', 'ativo': False}]



def finalizar_app():
    '''fecha o aplicativo'''
    exibir_subtitulo('Encerrando o programa')


def voltar_ao_menu_principal():
    input('Aperte enter ')
    main()


def exibir_subtitulo(texto):
    '''Exibe um subtitulo para cada função principal'''
    os.system('cls') # limpa o terminal
    linha = '-' * (len(texto))
    print(f'{linha}\n{texto}\n{linha}')


def opcao_invalida():
    '''Exibe a mensagem de que a opção escolhida é invalida'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_nome_programa():
      '''Exibe o nome do programa sem precisar repetir vaarias vezes quando nescessario'''
      print('''
      -=-=- Sabor Express -=-=-
            \n''')
      
def exibir_opcoes():
    '''Exibe as opções usadas no código'''
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurante')

    print('3. Alternar estado do restaurante')
    print('4. Sair')


def cadastrar_novo_restaurante():
    '''Cadastra um novo restaurante guardando dados como
    o nome do restaurante e a sua categoria
    
    Input:
    - Categoria
    - Nome do restaurante
    
    Output: 
    - dados do restaurante 
    - mensagem do cadastro'''
    exibir_subtitulo('Cadastrar Novo Restaurante')
    nome_do_restaurante = input('Digite o nome: ')
    categoria = input('Digite a Categoria: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 
                            'categoria': categoria,
                            'ativo': False}
    
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante}\nCadastrado com sucessos')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Exibe a lista de restaurantes já cadastrados 
    
    Output: 
    - Restaurantes já cadastrados'''
    exibir_subtitulo('Listar Restaurante')
    
    print(f'{'Nome Do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for r in restaurantes:
        ativo = 'Ativado' if r['ativo'] else 'Desativado'
        print(f'- {r['nome'].ljust(20)} | {r['categoria'].ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()


def alternar_estado_do_restaurante():
    '''Muda o estado de desativado para ativado e vice-versa
    
    Input:
    - nome do restaurante desejado
    
    Output:
    - o valor booleano do restaurante é mudado para False ou para True'''
    exibir_subtitulo('Alternar Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
            print(mensagem) 
    if not restaurante_encontrado:
        print('Não foi encontrado')
    voltar_ao_menu_principal()


def escolher_opcao():
    '''Pede para escolher uma opção e de acordo com a escolhida, 
    e usada a função
    
    Input: 
    - Escolha de opção
    
    Output:
    - ativa a função desejada'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except Exception as e:
        print(e)
        opcao_invalida()

def main():
    '''É a função principal do programa, 
    sendo a primeira a ser usada no programa inteiro'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__': # se torna a parte principal do programa
    main()
