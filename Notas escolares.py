nota = float(input('Qual é a sua primerira nota?'))
nota2 = float(input('Qual é a sua segunda média? '))
média = (nota + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota, nota2, s))
if média < 5:
    print('reprovado')
elif 7 > média >= 5:
    print('recuperação')
elif média< 7.0:
    print('Aprovado')
