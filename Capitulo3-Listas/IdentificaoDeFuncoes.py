def preencherInventario(lista):
    def preencherInventario(lista):
        resp = "S"
        while resp == "S":
            equipamento = [input("Equipamento: "),
                           float(input("Valor: ")),
                           int(input("Número Serial: ")),
                           input("Departamento: ")]
            lista.append(equipamento)
            resp = input("Digite 'S' para continuar: ").upper()

    def exibirInventario(lista):
        for elemento in lista:
            print("Nome.........: ", elemento[0])
            print("Valor........: ", elemento[1])
            print("Serial.......: ", elemento[2])
            print("Departamento.: ", elemento[3])