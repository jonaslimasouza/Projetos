n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
operacao = input("Escolha uma operação +,-,*,/:")

if operacao == "+":
    resultado = n1+n2
    print(f'O resultado é {resultado}')

elif operacao == "-":
    resultado = n1-n2
    print(f'O resultado é {resultado}')

elif operacao == "*":
    resultado = n1-n2
    print(f'O resultado é {resultado}')

elif operacao == "/":
    resultado = n1//n2
    print(f'O resultado é {resultado}')
    
else:
    print("Operação inválida!")