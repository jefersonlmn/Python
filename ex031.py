distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar um viagem de {}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será se R${:.2f}'.format(preço))