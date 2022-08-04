# praticas
msg = 'Ola, mundo'
print(msg)

#ex 1 
nome =input('Digite o seu nome: ')
print('É um prazer te conhecer,', nome)

#ex2
n1 = int (input('Digite um numero: '))
n2 = int (input('Digite o segundo numero: '))
s = n1+n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

#ex 3 
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
print('Só tm espaços? ', a.isspace())
print('É um numero? ', a.isalnum())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Esta em maiusculas? ', a.isupper())
print('Esta em minusculas? ', a.islower())
print('Esta capitalizada? ', a.istitle())

#ex 4
n1 = int (input('Um valor: '))
n2 = int (input('Outro valor: '))
s = n1 + n2
m = n1 * n2
su = n1 - n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {},\n O produto é {},\n A subtração é {}, A divisão é {:.3f}'.format(s, m, su, d))
print('Divisao inteira {}, E a potencia é {}'.format(di, e))

#ex 5 
n = int(input('Digite um valor: '))
print('Analisando o valor {}, O antecessor é {} , e o sucessor é {}'.format(n, (n-1), (n+1)))

#ex 6 
n = int(input('Digite um valor: '))
print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n,(1/2))))

#ex 7 
b = float(input('Escreva primeira nota: '))
c = float(input('Escreva segunda nota: '))
m = (b+c)/2
print('A media do aluno foi: {:.1f}'.format(m))

#ex8
a = int(input('Quantos metros: '))
c = a*100
m = a*1000
print('A quantidade de centimentros são {}, e milimetros são {}'.format(c, m))

#ex 9 
num = int(input("Digite um numero para ver a tabuada: "))
print('-'* 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-'*12)

#ex 10
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/5.39
print('Com R${:.2f} você pode comrpar US${:.2f}'.format(real, dolar))

#ex 11
a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
area = a*l
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(a, l, area))
tinta = area/2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

#ex 12
preço = float(input("O preço do produto é de R$: "))
novo = preço - (preço*5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))

#ex 13
salario = float(input('Digite o salario do funcionario R$: '))
novo = salario + (salario *15/100)
print('O funcionario que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, novo))

#ex 14
c = float(input('Informe a temperatura em "C: '))
f = 9 * c /5 + 32
print('A temperatura de {}"C corresponde a {}"F'.format(c, f))

#ex 15
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km foram rodados? '))
pago = (dias* 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))

from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(' A raiz de {} é igual a {:.2f}'. format(num, (raiz)))

#ex 16
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parção inteira é {}'.format(num, trunc(num)))

#Duas formas de fazer o exercicio acima
num = float(input('Digite um valor: '))
print('O valor digitado foi {}, e sua porção inteira é {}'.format(num, int(num)))

#EX 17 
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

# Segunda maneira de fazer o exercicio acima
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


#EX 18
import math
ângulo = float(input('Digite o angulo que voce deseja? '))
seno = math.sin(math.radians(ângulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

#Seguunda maneira de fazer o exercicio acima
from math import radians, sin, cos, tan
ângulo = float(input('Digite o angulo que voce deseja? '))
seno = sin(radians(ângulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

#EX 19
import random
n1 = input('Primeiro Aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))

#Segunda maneira de fazer o exercicio acima 
from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#EX 20
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação sera ')
print(lista)

#Segunda maneira de fazer exercicio acima 
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle = (lista)
print('A ordem de apresentação sera')
print(lista)

#EX 21
nome = str (input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#EX 22
num =int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#EX23
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

#EX 24
nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva {}'.format('silva' in nome.lower()))

#EX 25
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

#EX 26
n = str(input('Digite seu nome Inteiro: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))


#EX 27
nome = str(input('Qual seu nome? '))
if nome == 'Luciano':
    print('Que Lindo nome você tem!')
else: 
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))



n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
m = (n1 + n2)/2
print('A 3.5sua Média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Asua média foi boa! PARAbÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#EX 28
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente Adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei o número {} e não no {}!'.format(computador, jogador))


#EX 29
velocidade = float(input("Qual é a Velocidade atual do carro? "))
if velocidade > 80:
    print('MULTADO! Você execedeu o limite de permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um Bom dia!Dirija com segurança!')


#EX 30
numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {} é PAR!'.format(numero))
else:
    print('O numero {} é IMPAR'.format(numero))


#EX31
distancia = int(input('Qual a Quilometragem da viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('O valor da sua passagem sera de R${:.2f}'.format(preço))

#EX 32
from datetime import date
ano = int(input('Que eu quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano {} é BISSEXTO'.format(ano))
else: 
    print('O ano {} NÃO É BISSEXTO'.format(ano))

#EX 33
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o Segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a
if b<b and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c 
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

#EX 34
salario =float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario +(salario * 10/100)
print('Quem ganhava R${:.2f} passa receber R${:.2f} agora.'.format(salario, novo))


#ex 35
print('-=-' * 15)
print('Analisando Triângulos')
print('-=-'*15)
a = float(input('Digite o primeiro Segmento: '))
b = float(input('Digite o segundo Segmento: '))
c = float(input('Digite o terceiro Segmento: '))
if a < b+c and b < a+c and c < a+b:
    print('Os segmentos acima PODEM FORMAR UM TRIÂNGULO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO!')