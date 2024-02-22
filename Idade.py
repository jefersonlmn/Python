from datetime import date
atual = date.today().year
idade = int(input('Seu ano de nascimento?'))
ano = atual - idade
print('O atleta tem {} ano'.format(ano))
if ano<= 9:
    print('Clasificação:Mirim')
elif ano<= 14:
    print('Clasificação:Infantil')
elif ano<= 19:
    print('Clasificação:Junior')
elif ano<= 20:
    print('Clasificação:Sênior')
else:
    print('Clasificação:Master')
