import random
n1 = str(int(input('Primeiro aluno: ')))
n2 = str(int(input('Segundo aluno: ')))
n3 = str(int(input('Terceiro aluno: ')))
n4 = str(int(input('Quarto aluno: ')))
num = random.randint(1,4)
num = random.randint(1,4)
num = random.randint(1,4)
num = random.randint(1,4)
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {} número {}'.format(escolhido, num1))
print('O aluno escolhido foi {} número {}'.format(escolhido, num2))
print('O aluno escolhido foi {} número {}'.format(escolhido, num3,))
print('O aluno escolhido foi {} número {}'.format(escolhido, num4))