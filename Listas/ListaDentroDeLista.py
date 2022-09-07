#Depreciacao e exclussao

inventario = []
resposta = "S"

while resposta == "S":
    equipamentos = [input("Equipamento: "),
                    float(input("Valor: ")),
                    int(input("Numero Serial: ")),
                    input("Departamento: ")]

    inventario.append(equipamentos)
    resposta = input("Digite \"s\" para continuar: ").upper()

for elemento in inventario:
    print("Nome.........:", elemento[0])
    print("Valor........:", elemento[1])
    print("Serial.......:", elemento[2])
    print("Departamento.:", elemento[3])

busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento1 in inventario:
    if busca == elemento[0]:
        print("Valor..: ", elemento1[1])
        print("Serial.: ", elemento1[2])

depreciacao = input("\nDigite o nome do equipamento que sera depreciado: ")
for elemento2 in inventario:
    if depreciacao == elemento2[0]:
        print("Valor antigo: ", elemento2[1])
        elemento2[1] = elemento2[1] * 0.9
        print("Novo valor: ", elemento2[1])

serial = int(input("\nDigite o serial de equipamento que seta excluido: "))
for elemento3 in inventario:
    if elemento3[2] == serial:
        inventario.remove(elemento3)

for elemento4 in inventario:
    print("Nome.........: ", elemento4[0])
    print("Valor........: ", elemento4[1])
    print("Serial.......: ", elemento4[2])
    print("Departamento.: ", elemento4[3])

valores = []
for elemento5 in inventario:
    valores.append(elemento5[1])

if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))