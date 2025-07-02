#Nesse código o usuário vai tentar acertar o número sorteado.
numeroSorteado = 17
numero_usuario = int(input("Digite um número:"))

while numero_usuario != numeroSorteado:
    print("Número errado, tente de novo!")
    numero_usuario = int(input("Digite um número:"))

else:
    print("Parabéns, você acertou!!!")