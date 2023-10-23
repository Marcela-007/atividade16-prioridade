# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
print("1.Idoso")
print("2.Gestante")
print("3.Cadeirante")
print("4.Deficiente")
print("5.Nenhum destes")
resposta = int(input("Insira o número que você se aplica: "))
if (resposta==1) or (resposta==2) or (resposta==3) or (resposta==4):
    print("Você tem direito a fila preferencial ")
else:
    print("Você não tem direito a fila preferencial")