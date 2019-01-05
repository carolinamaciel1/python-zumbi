km = int(input("Digite a velocidade atual do seu carro:"))
if km > 110:
    calc = km - 110
    multa = calc * 5
    print("Você foi multado e terá que pagar %.2f reais." %multa)
