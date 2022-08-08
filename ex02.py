nome = str(input('Qual é o seu nome? '))
if nome == 'Luciano':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
   print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um Bom dia {}'.format(nome))

#EX 36
casa = float(input('Valor da casa R$:'))
salario = float(input('Qual o salario do comprador R$:'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos*12)
minimo = salario*30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

#ex37
num = int(input('Digite um numero inteiro: '))
print('''escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL ''')
opçao = int(input('Sua opção: '))
if opçao == 1 :
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2 :
    print('{}convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3 :
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção INVÁLIDA. Tente novamente!')


#EX 38
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
if n1 == n2:
    print('Os valores são iguais.')
elif n1 > n2:
    print('O primeiro valor é maior {}'.format(n1))
elif n1 < n2:
    print('O segundo valor é maior {}'.format(n2))


#EX 39
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade 
    print('Ainda faltam {} anos para o alistamento!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))



#EX 40
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2)/2
print('A Média do aluno foi de {}'.format(m))
if m < 5.0:
    print('O aluno está REPROVADO')
elif m >= 5.0 and m <= 6.9:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')

#EX 41
ano = int(input('Digite a idade do atleta: '))
if ano < 9:
    print('O atleta é da categoria MIRIM.')
elif ano > 9 and ano < 14:
  print('O atleta é da categoria INFANTIL.')
elif ano > 14 and ano < 19:
    print('O atleta é da categoria JUNIOR.')
elif ano == 20:
    print('O atleta é da categoria SÊNIOR.')
else: 
    print('O atleta é da categoria MASTER.')

#OUTRA MANEIRA DE FAZER EX 41
from datetime import date
atual = date.today().year   
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc 
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

#ex 42
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento:'))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO!', end=' ')
    if r1 == r2 and r2 == r3:
       print('EQUILÁTERO!')
    elif r1 !=r2 and r2 != r3 and r1!= r3:
       print('ESCALENO')
    else: 
        print('ISÓSCELES')
else: 
    print('Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO!')

#EX 43
peso = float(input('Digite seu peso? (KG)'))
altura = float(input('Digite a sua Altura? (M)'))
imc = peso/ (altura ** 2)
print('Seu IMC corresponde a {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está na classificação de MAGREZA!')
elif imc > 18.5 and imc <24.9:
   print('Seu IMC está na classificação de PESO IDEAL')
elif imc > 25.0 and imc < 29.9:
   print('Seu IMC está na classificção de SOBREPESO')
elif imc > 30.0 and imc < 39.9:
    print('Seu IMC está na classificação de OBESIDADE')
else:
    print('Seu IMC está na classificação de OBESIDADE GRAVE')


#EX 44
print('{:=^40}'.format(' Lojas GUANABARA '))
preço = float(input('Preços das Compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista Cartão 
[ 3 ] 2x no Cartão 
[ 4 ] 3x ou mais no Cartao''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço -(preço * 5 / 100)
elif opção == 3:
    total = preço 
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else: 
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))









