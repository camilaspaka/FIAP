usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()