ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite <S> para continuar: ").upper()
    print("Exibindo ip´s: ")
    for ip in ips.keys():
        print(ip[0] + "." + ip[1])