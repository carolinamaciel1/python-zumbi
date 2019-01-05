min = int(input("Digite a qtd de minutos:"))
if min < 200:
    valor = min * 0.20
    print("O valor da conta a pagar é: %.2f" %valor)
else:
    if min <=400:
        valor = min * 0.18
        print("O valor da conta a pagar é: %.2f" %valor)
    if min > 400:
        valor = min * 0.15
        print("O valor da conta a pagar é: %.2f" %valor)
