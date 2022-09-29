from Listas.PercorrendoDicionarioFuncoes import *

usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":

        inserir(usuarios)

    elif opcao == "P":

        pesquisar(input("Escreva a chave que deseja pesquisar: ").upper(), usuarios)

    elif opcao == "E":

        excluir(usuarios, input("Escreva a chave que deseja excluir: ").upper())

    elif opcao == "L":

        listar(usuarios)

    opcao = perguntar()
