

def calcularGorjeta(valorDaConta, porcentagemGorjeta):
    
    gorjeta = (valorDaConta * (porcentagemGorjeta / 100))
    return print(f"O Valor de gorjeta pago foi: {gorjeta}" )




valor_conta = int(input("Digite o valor da conta"))
porcentagemGorjeta = int(input("Quantos % voce quer pagar de Gorjeta?"))

calcularGorjeta(valor_conta, porcentagemGorjeta)


