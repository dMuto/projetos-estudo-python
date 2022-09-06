# INVENTARIO
inventario = []
resposta = "S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()  # O * \"S\" * é para imprimir as "" no console e
                                                              # não para que seja interpretado no codigo


for elemento in inventario:
    print(elemento)
