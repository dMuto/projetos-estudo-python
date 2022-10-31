def incluirNovoNome(dicionario, nome, numero):

    dicionario[nome] = [numero]

def incluirNovoNumero(dicionario, nome, numero):

    if dicionario.get(nome) is not None:

        dicionario[nome] += [numero]

    else:
        resposta = input("Este nome não existe na lista, gostaria de adiciona-lo?(y = sim / n = nao) ").upper()

        if resposta == "Y":

            incluirNovoNome(dicionario, nome, numero)

        elif resposta == "N":

            print("Numero ignorado")

        else:

            print("Responda como y ou n")

def excluirTelefone(dicionario, nome):

    del dicionario[nome][-1]
    r = dicionario[nome]

    if len(r) == 0:
        dicionario.pop(nome)

def excluirPessoa(dicionario, nome):

    dicionario.pop(nome)

def consultarTelefones(dicionario, nome):

    return print(dicionario.get(nome))

def listarNumeros(dicionario):

    return print(dicionario)


