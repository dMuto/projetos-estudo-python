def perguntar():

    return input("O que deseja realizar?\n" +
              "<I> - Para inserir um usuário\n" +
              "<P> - Para pesquisar um usuario\n" +
              "<E> - Para excluir um usuario\n" +
              "<L> - Para Listar um usuario: ").upper()

def inserir(dicionario):

    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                   input("Digite a ultima data de acesso: ").upper(),
                                                   input("Qual a ultima estação acessada: ").upper()]

def pesquisar(chave, dicionario):

    return print(dicionario.get(chave))

def excluir(dicionario, chave):

    dicionario.pop(chave)

def listar(dicionario):
    return print(dicionario)