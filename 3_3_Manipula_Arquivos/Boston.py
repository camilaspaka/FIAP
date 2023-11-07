with open("economic-indicators.csv","r") as boston:
    total=0
    for linha in boston.readlines()[1:-1]:
        total=total+float(linha.split(",")[3])
    print("O total de voos é: ", total)