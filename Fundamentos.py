'''
nome = input('Quao e seu nome?')
print('É um prazer te conhecer, {}!'.format(nome))
'''
#todo/ int(7,-4,0,9875) float(4.5,0.076,-15.223,7.0) bool(True,False) str('Olá','7.5','')
'''
n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo número: '))
s=n1+n2
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
print('A soma entre',n1,'é',n2,'vale:',s)
'''
'''
n=input('Digite algo: ')
print(n.isalnum())
'''
'''
a = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
print('So tem espaços? ',a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabetico? ',a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Está em maiusculas? ',a.isupper())
print('Está em minusculas? ',a.islower())
print('Está capitalizada? ',a.istitle())
'''
#todo/ ** Potência //Divisão Inteira %Resto da Divisão (%2 par = 0 impar = 1)
# 5+2=7 5-2=3 5*2=10 5/2=2.5 5**2=25 5//2=2 5%2=1
# Orden de Presedencia 1(), 2**, 3* / // %, 4+ -
'''
nome=input('Quao seu nome ')
print('Prazer em te conhecer {:=^20}'.format(nome))
print('Prazer em te conhecer {:<20}'.format(nome))
print('Prazer em te conhecer {:>20}'.format(nome))
print('Prazer em te conhecer {:^20}'.format(nome))
'''
'''
n1=int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma e {},\n A multiplicação e {}, A divisão e {:.3f}'.format(s,m,d),end=' >>> ')
print('A Divisão inteira e {}, A potencia e {}'.format(di,e))
'''
#Que leia um número inteiro e mostre na tela o seu SUCESSOR e seu ANTECESSOR
'''
n=int(input('Digite um número '))
s=n+1
r=n-1
print('O número é {}, Seu antecessor e {}, Seu sucessor e {}'.format(n,r,s))
print('Analisando o valor {}, Seu antecessor é {}, E o sucessor é {}'.format(n,(n-1),(n+1)))
'''
#Crie um algoritmo que leia um número e mostre o SEU DOBRO, TRIPLO e RAIZ QUADRADA.
'''
n=int(input('Digite um número '))
d=n*2
t=n*3
r=n**(1/2)
print('O número digitado e {}, \nSeu dobro e {}, \nSeu triplo e {}'.format(n,d,t),end=' ')
print('\nSua raiz quadrada é {:.2f}'.format(r))
print('O dobro de {} vale {},'.format(n,(n*2)))
print('O triplo de {} vale {}, \nA raiz quadrada de {} é igual a {:.2f}'.format(n,(n*3),n,n**(1/2)))
'''
#Que leia as DUAS NOTAS de um aluno, calcule e mostre a sua MÉDIA
'''
n1=float(input('Insira a primeira nota '))
n2=float(input('Insira a segunda nota '))
m=(n1+n2)/2
print('A media do aluno e {:.1f}'.format(m))
'''
#Que leia um valor em METROS e o exiba convertido em CENTIMETROS e MILÍMETROS.
'''
m=float(input('Insira os metros '))
c=m*100
mm=m*1000
print('Os metros sao {}, Em centimetros e {}, Em milimetros e {}'.format(m,c,mm))
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(m,(m*100),(m*1000)))
'''
#Que leia um número inteiro qualquer e mostre na tela a sua TABUADA
'''
n=int(input('Insira um número '))
print('A tabuada de {} é:'.format(n))
print('-'*17)
print('{} x {:2} = {}'.format(n,1,n*1))
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print('{} x {:2} = {}'.format(n,4,n*4))
print('{} x {} = {}'.format(n,10,n*10))
print('-'*17)
'''
#Que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos DÓLARES ela pode COMPRAR1=3,27
'''
r=float(input('Quanto dinheiro você tem na sua carteira? R$ '))
d=r/3.27
b=r*1.32
e=r*0.16
print('Com {:.2f} R$ \nVocê pode comprar:'.format(r))
print('{:.2f} US$'.format(d))
print('{:.2f} Bs'.format(b))
print('{:.2f} Eu'.format(e))
'''
#Que leia a LARGURA e a ALTURA de uma parede em metros, calcule a sua ÁREA e a quantidade de tinta
#necessária para pintá-la,sabendo que cada litro de tinta,pinta uma área de 2m2.
'''
l=float(input('Digite a largura '))
a=float(input('Digite a altura '))
area=a*l
litro=area/2
print('A area e de {} metros, A quantidade de tinta necessaria e {:.1f} litros'.format(area,litro))
'''
#Que leia o PREÇO de um produto e mostre seu NOVO PREÇO,com 5% de desconto
'''
p=float(input('Digite o preço do produto '))
n=p-(p*5/100)
print('O preço do produto com desconto del 5% e {:.2f} R$'.format(n))
'''
#Que leia o salário de um funcionário e mostre seu NOVO SALÁRIO, com 15% de AUMENTO
'''
s=float(input('Quão e seu salario? R$ '))
n=s+(s*15/100)
print('Seu novo salario com aumento del 15% e {:.2f} R$'.format(n))
'''
#Preço de um produto a VISTA menos 10% e PARCELADO mas 7%
'''
p=float(input('Quão o preço do produto que deseja comprar? R$ '))
v=p-(p*10/100)
c=p+(p*7/100)
print('O produto a vista custa {:.2f}, e parcelado vale {:.2f}'.format(v,c))
'''
#Programa que CONVERTA UMA TEMPERATURA digitada em ºC e converta para ºF
'''
c=float(input('Informe a temperatura em ºC '))
f=(c*1.8)+32
f=((9*c)/5)+32
print('A temperatura em {}ºC corresponde a {}ºF'.format(c,f))
'''
#Que pergunte a quantidade de Km PERCORRIDOS POR UM CARRO ALUGADO e quantidade de dias pelos quais
#ele foi alugado.Calcule o PREÇO A PAGAR,sabendo que o carro custa 60 por dia e 15 por Km rodado
'''
dias=int(input('Quantos dias o carro foi alugado? '))
km=float(input('Quao e a quantidade de Km rodados? '))
pago=(dias*60)+(km*0.15)
print('O preço total a pagar é de R${}'.format(pago))
'''
#todo/ Biblioteca math(ceil=arredonda pra cima,floor=arredonda pra baixo,
# trunc=elimina da virgula prar frente,
# pow=potencia **,sqrt=raiz quadrada,factorial)
# import math = importa toda a biblioteca
# from math import sqrt = importa só un caracter
'''
from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} e igual a {:.2f}'.format(num, floor(raiz)))
'''
'''
import random
num=random.randint(1, 10)
print(num)
'''
#Que leia um número REAL qualquer pelo teclado e mostre na tela a sua PORÇÃO INTEIRA 6.127 = 6
'''
#from math import floor
#from math import trunc
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,floor(num)))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,trunc(num)))
num=float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))
'''
#Que leia o COMPRIMENTO DO CATETO OPOSTO e do CATETO ADJACENTE de um TRIÂNGULO retângulo, calcule
#e mostre o comprimento da HIPOTENUSA.
'''
from math import hypot
co=float(input('Digite o comprimento do cateto oposto: '))
ca=float(input('Digite o comprimento do cateto adjacente: '))
#hi=(co**2+ca**2)**(1/2)
#print('O comprimento da hipotenusa é {:.2f}'.format(hi))
hi=hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''
#Que leia um ÂNGULO qualquer e mostre na tela o valor do SENO,COSSENO e TANGENTE desse ângulo.
'''
from math import radians,sin,cos,tan
ang=float(input('Digite o angulo que você deseja: '))
print('O angulo de {} tem o seno de: {:.2f}'.format(ang,sin(radians(ang))))
print('O angulo de {} tem o cosseno de: {:.2f}'.format(ang,cos(radians(ang))))
print('O angulo de {} tem a tangente de: {:.2f}'.format(ang,tan(radians(ang))))
'''
#Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que
#ajude ele,lendo o NOME deles e escrevendo o NOME DO ESCOLHIDO.
'''
from random import choice
al1=str(input('Digite o nome do primeiro aluno: '))
al2=str(input('Digite o nome do segundo aluno: '))
al3=str(input('Digite o nome do terceiro aluno: '))
al4=str(input('Digite o nome do quarto aluno: '))
lista=[al1,al2,al3,al4]
sort=choice(lista)
print('O aluno escolhido foi {}'.format(sort))
'''
#Sortear a ORDEM de APRESENTAÇÃO de trabalhos dos alunos.Que leia o nome dos 4 e mostre a ordem
'''
from random import shuffle
a1=str(input('Primeiro aluno: '))
a2=str(input('Segundo aluno: '))
a3=str(input('Terceiro aluno: '))
a4=str(input('Quarto aluno: '))
lista=[a1,a2,a3,a4]
shuffle(lista)
print('A ordem de apresentação será \n{} '.format(lista))
'''
#Programa que abra e reproduza o áudio de um arquivo MP3.
'''
import pygame
pygame.init()
pygame.mixer.music.load('pol.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''
#todo/ frase='Curso em Video Python' 20 caracteres-1
# FATIAMENTO frase[9],frase[9:14]=ultimo não entra,frase[9:21:2] salta de dos em dos,
# frace[:5]vai de 0 ate 4,frase[15:]conta do 15 ate o final,frase[9::3]comça no 9 pula de 3 em 3,
# frace[::2]começa do principio pula de dos em dos
# ANALISE len(frase)e o total de caracteres, frase.count('o') Conta as veces que tem o
# frase.count('o,0,13') procura o entre 0 e 13, frase.find('deo') procura donde começa a palabra
# frase.find('Android')se nao existe mostra -1,'Curso'in frase Escreve True se existe a palabra
# TRANSFORMAÇÃO frase.replace('Python','Android') Substitui a palabra
# frase.upper()troca as letras minusculas por maiusculas
# frase.lower()troca as letras maiusculas por minusculas
# frase.capitalize()so a primera letra fica maiuscula e o resto minuscula
# frase.title()Coloca o começo de cada palabra em maiuscula
# frase.strip()remove os espaços vacios no começo e no final
# frase.rstrip()remove so os ultimos espaços der
# frase.lstrip()remove os espaços do começo izq
# DIVISÃO frase.split()divide em pedaços nos espaços da frase primera palabra 0-1-2...
# JUNÇÃO '-'.join(frase)coloca guion en los espaços da frase
#todo/
# print('''FATIAMENTO frase[9],frase[9:14]=ultimo não entra,frase[9:21:2] salta de dos em dos,
# frace[:5]vai ate a 4,frase[15:]conta do 15 ate o final,frase[9::3]comça no 9 pula de 3 em 3,
# ANALISE len[frase]e o total de caracteres, frase.count('o') Conta as veces que tem o
# frase.count('o,0,13') procura o entre 0 e 13, frase.find('deo') procura donde começa a palabra
# frase.find('Android')se nao existe mostra -1,'Curso'in frase Escreve True se existe a palabra''')
'''
frase='Curso em Vídeo Python'
print(frase[::2])
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python','Android'))
print(frase[0])
frase=frase.replace('Python','Android')
print(frase)
print('Curso'in frase)
print(frase.find('Vídeo'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido=frase.split()
print(dividido[0])
print(dividido[2][3])
'''
#Que leia o nome completo de uma pessoa e mostre: NOME todas as letras em MAIÚSCULA, NOME com todas
# as letras em MINÚSCULA,QUANTAS LETRAS ao todo sem espaço, é O PRIMEIRO NOME
'''
nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúscula é: {}'.format(nome.upper()))
print('Seu nome em minúscula e: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primero nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()
print('Seu primero nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
'''
#Que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Digite um número: 1834 -> Unidade: 4, Dezena: 3, Centena: 8, Milhar: 1
'''
num=int(input('Digite um número de 0 a 9999: '))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''
#Crie um programa que leia o nome de uma cidade e diga SE ela COMEÇA ou não com o nome SANTO.
'''
nome=str(input('Digite o nome de sua cidade: ')).strip()
print(nome[:5].upper()=='SANTO')
'''
#Que leia o nome de uma pessoa e DIGA se ela TEM SILVA no nome.
'''
nome=str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva? R: {}'.format('silva'in nome.lower()))
'''
#Que leia uma frase: Quantas vezes aparece a letra A, Em que posição aparece a primeira vez
# Em que posição ela aparece a última vez.
'''
frase=str(input('Digite a frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra "A" apareceu na posição: {}'.format(frase.rfind('A')+1))
'''
#Que leia o nome completo de uma pessoa, mostrando em seguida o PRIMEIRO e o ÚLTIMO nome separado
#Ex:Ana Maria de Souza Primeiro=Ana Último=Souza
'''
nome=str(input('Digite o seu nome completo: ')).strip()
separa=nome.title().split()
print('Prazer em te conhecer!!!')
print('Seu primeiro nome é: {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[len(separa)-1]))
'''
#todo/ CONDIÇÕES
# se carro.esquerdo()  bloco _V_   senão  bloco _F_
# if carro.esquerda(): _bloco True else: _bloco False
'''
tempo=int(input('Quantos anos tem seu carro? '))
print('carro novo'if tempo<=3 else'carro velho')
#if tempo<=3:
#    print('\033[32m''Carro novo')
#else:
#    print('\033[31m''Carro velho')
print('--FIM--')
'''
#Que leia duas NOTAS e calcule a MEDIA com uma mensagem foi boa o foi ruim.
'''
n1=float(input('\033[34m''Digite a primeira nota: '))
n2=float(input('\033[34m''Digite a segunda nota: '))
m=(n1+n2)/2
print('A sua média foi: {:.1f}'.format(m))
#if m>=6.0:
#    print('\033[32m''Sua média foi boa! Parabens!')
#else:
#    print('\033[31m''Sua média foi ruim! Estude mais!')
print('\033[32m''Sua média foi boa! Parabéns!'if m>=6 else '\033[31m''Sua média foi ruim! Estude mais!')
'''
#Que faça o computador PENSAR em um número inteiro entre 0 e 5 e peça para o usuario tentar desco
#brir qual foi o número. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('\033[36m''=-' * 20, '\033[m')
print('\033[1;34m''Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[036m''=-' * 20, '\033[m')
jogador = int(input('Em que número pensei? '))
print('\033[1;34m''Processando...')
sleep(3)
if computador == jogador:
    print('\033[32m''Parabéns! Você conseguiu me vencer!')
else:
    print('\033[31m''Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
'''
#Que leia a VELOCIDADE de um carro.Se ultrapassar 80Km/h,mostre a mensagem dizendo que ele foi
#multado. A multa vai custar 7R$ por cada Km acima do limite.
'''
velocidade=float(input('Qual é a velocidade atual do seu carro? '))
if velocidade>80:
    print('\033[31m''Multado! Você excedeu o limite permitido que é de 80Km/h')
    multa=(velocidade-80)*7
    print('\033[31m''Você deve pagar uma multa de R${}{:.2f}!'.format('\033[1m',multa))
print('\033[1;32m''Tenha um bom dia! Dirija com segurança!')
'''
#Que leia umm número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
numero=int(input('Digite um número: '))
#if numero%2==0:
resultado=numero%2
if resultado==0:
    print('\033[32m''O número {}{} é PAR'.format('\033[1m',numero))
else:
    print('\033[31m''O número {}{} é ÍMPAR''\033[m'.format('\033[1m',numero))
'''
#Que pergunte a distância de uma viagem em Km Calcule o preço da passagem,cobrando 0.50R$ por Km
#para viagens de até 200Km e 0,45R$ para viagens mais longos
'''
distancia=float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
preço=distancia*0.50if distancia<=200else distancia *0.45
##if distancia<200:
#    print('E o preço da sua passagem será de R${:.2f}'.format(distancia*0.50))
##    preço=distancia*0.50
##else:
##    preço=distancia*0.45
#    print('E o preço da sua passagem será de R${:.2f}'.format(distancia*0.45))
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
from datetime import date
ano=int(input('\033[36m''Que ano você quer analisar? ''\033[m'))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('\033[32m''O ano {} e Bissexto'.format(ano))
else:
    print('\033[31m''O ano {} não e Bissexto'.format(ano))
'''
#Faça um programa que leia TRÊS números e mostre qual é o MAIOR e qual é o MENOR.
'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
'''
#Que pergunte o salário de um funcionário e CALCULE o valor do seu aumento. Para salários supe
#riores a 1.250.00,calcule um aumento de 10% Para inferiores ou iguais, o aumento é de 15%
'''
salario=float(input('Quão é o salário do funcionario? R$ '))
if salario>=1250:
    novo=salario+(salario*10/100)
else:
    novo=salario+(salario*15/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,novo))
'''
#Desenvolva um programa que leia o comprimento de TRÊS RETAS e diga ao usuário se elas podem ou
# não formar UM TRIÂNGULO
'''
print('\033[32m''-=' * 20,'\033[m')
print('\033[1;42m''Analisador de Triângulo', '\033[m')
print('\033[32m''-=' * 20,'\033[m')
r1 = float(input('Digite o comprimento do 1er segmento: '))
r2 = float(input('Digite o comprimento do 2do segmento: '))
r3 = float(input('Digite o comprimento do 3er segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32m''Os segmentos acima podem formar um triangulo!')
else:
    print('\033[31m''Os segmentos acima não podem formar um triangulo!')
'''

#todo/ Padrão ANSI \033[style(0=SemEstilo,negrito,sublinhado)text(CorDoTexto)back(CorDoFundo)m
# Style=0Nada,1Negrito,4Sublinhado,7Inverter
# Text=30Branco,31Vermelho,32Verde,33Amarelo,34Azul,35Magenta,36Ciano,37Cinza
# Back=40Branco,41Vermelho,42Verde,43Amarelo,44Azul,45Magenta,46Ciano,47Cinza
# \033[0;30;44m
# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
# nome='Marco Antonio'
# print('Olá muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))
# nome = 'Marco Antonio'
# cores = {'limpa': '\033[m',
#         'azul': '\033[34m',
#         'amarelo': '\033[33m',
#         'pretobranco': '\033[7;30m'}
# print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
