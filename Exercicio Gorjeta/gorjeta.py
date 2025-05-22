

def calcularGorjeta(valorDaConta, porcentagemGorjeta):
    
    gorjeta = (valorDaConta * (porcentagemGorjeta / 100))
    return print(f"O Valor de gorjeta pago foi: {gorjeta:.2f}" )




valor_conta = float(input("Digite o valor da conta "))
porcentagemGorjeta = float(input("Quantos % voce quer pagar de Gorjeta? "))

calcularGorjeta(valor_conta, porcentagemGorjeta)


