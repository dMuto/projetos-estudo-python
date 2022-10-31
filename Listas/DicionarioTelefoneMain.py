from Listas.DicionarioTelefones import *

agenda = {}

incluirNovoNome(agenda, input("Nome: ").upper(), input("Numero: "))
#incluirNovoNome(agenda)
#incluirNovoNome(agenda)

incluirNovoNumero(agenda, input("Nome do contato: ").upper(), input("numero: "))
incluirNovoNumero(agenda, input("Nome do contato: ").upper(), input("numero: "))

excluirTelefone(agenda, input("Nome do contato para excluir ultimo telefone: ").upper())
excluirPessoa(agenda, input("Nome do contato para excluir pessoa: ").upper())

consultarTelefones(agenda, input("Nome do contato para consultar telefones: ").upper())
listarNumeros(agenda)