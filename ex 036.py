casa = float(input('Valor da casa: R$'))
salário = float(input('Quando você ganha: R$'))
anos = int(input('Quantos anos você quer pagar?'))
prestação = casa / (anos * 12)
mínimo = salário * 30/100
print('Para pagar uma casa de R${:.2} em {} anos'.format(casa, anos)(end=''))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação<=mínimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo Negado')