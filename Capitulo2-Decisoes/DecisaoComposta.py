nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado a sala Amarela - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa=="SIM":
    print("O paciente deve ser direcionado para a sala Amarela - SEM prioridade.")
elif idade >=65 and doenca_infectocontagiosa=="NAO":
    print("O paciente será direcionado para a sala Branca - COM prioridade ")
elif idade <65 and doenca_infectocontagiosa=="NAO":
    print("O paciente será direcionado para a sala Branca - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")