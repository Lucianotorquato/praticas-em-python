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