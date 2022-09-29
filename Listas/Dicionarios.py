usuario = {}

usuario = {
            "chaves" : ["Chaves do 8", "24/12/2017", "Recep_01"],
            "quico" : ["Quico das Flores", "20/12/2017", "Raiox_03"]
}

print(usuario)

usuario["Florinda"] = ["Dona Florinda", "24/12/2017", "Raiox_01"]

print(usuario)

print("####-----####")
print(usuario.get("quico"))
