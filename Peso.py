peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m)'))
imc = peso /  (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de Peso Normal')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBRSIDADE!')
elif imc >= 40:
    print('Você está em OBESIDADE MORBIDA.cuidado!')
