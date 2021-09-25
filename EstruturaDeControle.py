# todo/CONDIÇÕES ALINHADAS if carro.esquerda(): elif carro.direita(): +Opções elif(): else:
'''
nome = str(input('Qual seu nome? '))
if nome == 'Marco':
    print('Nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nome popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome e bem normal')
print('Tenha um bom dia, {}'.format(nome))
'''
# Para aprovar empréstimo bancário para a compra de uma casa.O programa vai perguntar o VALOR DA CASA
# o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. Calcule o valor da prestação mensal,sabendo
# que ela não pode exceder 30% do salário ou então o empréstimo será negado
'''
casa = float(input('Qual o valor da casa que pretende comprar? R$ '))
salario = float(input('Qual e seu salario? R$ '))
tempo = int(input('Em quantos anos você pretende pagar? '))
pago=casa/(tempo*12)
liquido=salario*30/100
#liquido = salario - (salario - (salario * 30 / 100))
#pago = (casa / tempo) / 12
if liquido >= pago:
    print('\033[1;32m''Empréstimo bancario APROVADO!')
    print('Para pagar uma casa de R$ {:.2f} em {}'.format(casa,tempo), end=' ')
    print('anos a prestação será de R${:.2f}'.format(pago))
else:
    print('\033[1;31m''Empréstimo NEGADO!')
    print('\033[31m''Para pagar uma casa de R$ {:.2f}'.format(casa), end=' ')
    print('em {} anos a prestação será de R${:.2f}!'.format(tempo, pago))
'''
# Que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO:
# 1 para BINÁRIO 2 para OCTAL 3 para HEXADECIMAL
'''
num=int(input('Digite um número inteiro: '))
print('\033[36m''ESCOLHA UMA DAS OPÇÕES ABAIXO''\033[m')
print('Digite 1 Para Binário ')
print('Digite 2 Para Octal ')
print('Digite 3 Para hexadecimal')
opção=int(input('\033[34m''Digite o númmero da Opção escolhida ''\033[m'))
if opção==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção==2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opção==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida! Tente novamente')
'''
# Que leia DOIS NÚMEROS inteiros e compare-os mostrando na tela uma mensagem: -O PRIMEIRO VALOR é
# MAIOR -O SEGUNDO VALOR é MAIOR - NÃO EXISTE valor maior,os dois são IGUAIS.
'''
primer = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
if primer > segundo:
    print('\033[32m''O PRIMEIRO valor é maior''\033[m')
elif segundo > primer:
    print('\033[33m''O SEGUNDO valor é maior''\033[m')
else:
    print('\033[1;31m''Não existe valor maior, os dois são IGUAIS')
'''
# Que leia o ano de nascimento de um jovem e informe,de acordo com sua idade: -Se ele AINDA VAI SE
# ALISTAR ao serviço militar.-Se é a HORA DE SE ALISTAR.-Se já PASSOU DO TEMPO do alistamento.
# também deverá mostrar o TEMPO que FALTA ou que PASSOU do PRAZO.
'''
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você naceu? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade==18:
    print('\033[1;33m''Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo=18-idade
    print('\033[1;32m''Ainda faltam {} anos para o alistamento'.format(saldo))
    ano=atual+saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18: # ou else:
    saldo=idade-18
    print('\033[1;31m''Você já deveria ter se alistado há {} anos'.format(saldo))
    ano=atual-saldo
    print('Seu alistamento foi em {}'.format(ano))
'''
# Que leia duas notas de um aluno e calcule sua média,mostrando uma mensagem no final,de acordo com
# a média atingida: -Média abaixo de 5.0 REPROVADO 5.0 e 6.9 RECUPERAÇÃO 7.0 APROVADO
'''
n1 = float(input('Digite a primera nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
if media < 5:
    print('\033[1;31m''O aluno esta REPROVADO!')
elif media >= 5 and media < 7:
    print('\033[1;33m''O aluno está de RECUPERAÇÃO!')
else:
    print('\033[1;32m''O aluno esta APROVADO!')
'''
# Que leia o ANO DE NASCIMENTO de um atleta e mostre sua categoria, de acordo com a idade: Até
# 9 anos MIRIM, 14 INFANTIL,19 JUNIOR,20 SÉNIOR, Acima:MASTER
'''
from datetime import date
atual=date.today().year
nascimento=int(input('Digite seu ano de nacimento: '))
idade=atual-nascimento
print('O atleta tem {} anos.'.format(idade))
if idade<=9:
    print('Sua categoria e MIRIM')
elif idade>9 and idade<=14: #ou idade <=14
    print('Sua categoria é INFANTIL')
elif idade>14 and idade<=19: #ou idade <=19
    print('Sua categoria é JUNIOR')
elif idade>20 and idade<=25: #ou idade <=25
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria e MASTER')
'''
# Dos TRIÂNGULOS,acrescentando o recurso de mostrar que tipo de triângulo será formado: EQUILÁTERO
# todos os lados iguais, ISÓSCELES:dosi lados iguais, ESCALENO:todos os lados diferentes
'''
print('\033[32m''-=' * 20,'\033[m')
print('\033[1;42m''Analisador de Triângulo', '\033[m')
print('\033[32m''-=' * 20,'\033[m')
r1 = float(input('Digite o comprimento do 1er segmento: '))
r2 = float(input('Digite o comprimento do 2do segmento: '))
r3 = float(input('Digite o comprimento do 3er segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32m''Os segmentos acima podem formar um triangulo! ',end='')
    if r1==r2 and r2==r3: # ou r1==r2==r3:
        print('EQUILATERO!')
    elif r1 != r2 and r2 != r3 and r3 != r1: # r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('\033[31m''Os segmentos acima não podem formar um triangulo!')
'''
# Que leia o PESO e a ALTURA de uma pessoa,calcule seu IMC e mostre seu status,de acordo com a tabela
# Abaixo de 18.5:ABAIXO DO PESO,18.5 e 25:PESO IDEAL,25 até 30:SOBREPESO, 30 até 40:OBESIDADE, acima
'''
peso=float(input('Qual e seu peso? (Kg) '))
altura=float(input('Qual e sua altura? (metros) '))
imc=peso/(altura*altura) #(altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print('\033[1;31m''Você está ABAIXO DO PESO normal'.format(imc))
elif imc>=18.5 and imc<25: #18.5<=imc<25:
    print('\033[1;32m''Parabens! Você está na faixa de PESO NORMAL')
elif imc>=25 and imc<30: #25<=imc<30:
    print('\033[1;33m''SOBREPESO')
elif imc>=30 and imc<=40: #30<=imc<40:
    print('\033[1;31m''Você está em OBESIDADE')
else:#elif imc >=40:
    print('\033[1;31m''Cuidado! Você está em OBESIDADE MÓRBIDA')
'''
# Que calcule o valor a ser PAGO por um produto,considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGO
# À VISTA dinheiro/cheque:10%desconto,cartão:5%desconto,2xno cartão:normal,3x ou mais 20% juros
# print('\033[1;36m''{:=^40}''\033[m'.format(' LOJAS TONNY '))
# preço = float(input('Qual o preço normal do produto? R$ '))
# print('\033[1;34m''''FORMAS DE PAGAMENTO
# [1] à vista dinheiro/cheque
# [2] à vista cartão
# [3] 2x no cartão
# [4] 3x ou mais no cartão\033[m''')
'''opçao = int(input('Qual é sua opção de pagamento? '))
if opçao == 1:
    total = preço - (preço * 10 / 100)
elif opçao == 2:
    total = preço - (preço * 5 / 100)
elif opçao == 3:
    total = preço
    parcela = total / 2
    print('\033[1;34m''Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opçao == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('\033[1;34m''Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preço
    print('\033[1;31m''OPÇÃO INVÁLIDA de pagamento!!! Tente novamente!')
print('\033[1;34m''Sua compra de R$ {:.2f} vai custar R${:.2f} no final'.format(preço, total))
'''
# Que faça o computador jogar JOKEMPÔ com você.
# from random import randint
# from time import sleep
# itens=('Pedra','Papel','Tesoura')
# computador=randint(0,2)
# print('\033[1;34m''''Suas opções:
# [0] PEDRA
# [1] PAPEL
# [2] TESOURA''''\033[m')
'''jogador=int(input('Qual é sua opção jogada? '))
print('\033[1;36m''JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('-='*12)
if jogador>=3:
    print('\033[1;31m''JOGADA INVALIDA!''\033[m')
else:
    print('\033[1;34m''Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
print('\033[1;36m''=-'*12)
if jogador==0: #PEDRA
    if computador==0:
        print('EMPATE')
    elif computador==1:
        print('COMPUTADOR VENCE')
    elif computador==2:
        print('JOGADOR VENCE')
elif jogador==1: #PAPEL
    if computador==0:
        print('JOGADOR VENCE')
    elif computador==1:
        print('EMPATE')
    elif computador==2:
        print('COMPUTADOR VENCE')
elif jogador==2: #TESOURA
    if computador==0:
        print('COMPUTADOR VENCE')
    elif computador==1:
        print('JOGADOR VENCE')
    elif computador==2:
        print('EMPATE')
'''
#todo/
# laço c no intervalo(1,10)   for c in range(1,10):    forcinrange(0,3):        forcinrange(0,3):
#     passo                       passo                passo                      ifmoeda:
#    pega                      pega                    pula                          pega
#                                                      passo                        passo
#                                                      pega                         pula
#                                                                                     passo
#                                                                                     pega
'''
for c in range(7,0,-1): #(1,7,2) conta de 1 ate 6 pulando de 2 em 2
                        #(7,1,-1) desconta de 7 ate 0 no imprime 0
    print(c)
print('FIM')
'''
'''
n=int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('FIM')
'''
'''
i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM')
'''
'''
s=0
for c in range(0,5):
    n=int(input('Digite um valor: ')) #pede valores 5 veces
    s+=n # soma todos os valores digitados
print('O somatório de todos os valores foi {}'.format(s))
print('Fim')
'''
# Que mostre na tela uma CONTAGEM REGRESIVA para o estouro de fogos, indo DE 10 ATÉ 0, PAUSA 1 SEG.
'''
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')
'''
# Que mostre na tela todos os NÚMEROS PARES que estão no INTERVALO entre 1 e 50
'''
for n in range(2,51,2):
#    print(n)
    print('.',end='')
#    if n%2==0:
    print(n, end=' ')
print('FIM')
'''
# Que CALCULE A SOMA entre todos os NÚMEROS ÍMPARES que são MÚLTIPLOS DE TRÊS no INTERVALO 1 até 500
'''
soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        contador = contador + 1  # Mais um que eu achei
        soma = soma + n  # Acumulando valores(soma,multiplica,etc)
#        soma +=n
#        contador += 1
print('A soma dos {} multiplos de três foi {}'.format(contador, soma))
'''
# Mostre a TABUADA de um número que o usuario escolher, utilizando LAÇO FOR
'''
numdigitado=int(input('Digite um número para ver sua tabuada: '))
for n in range(1,11):
        print('{} x {:2} = {}'.format(numdigitado,n,numdigitado*n))
'''
# Que leia 6 NÚMEROS INTEIROS e mostre a SOMA apenas dos PARES. Se o valor digitado for IMPAR descon
'''
contador=0
soma=0
for n in range(1,7):
    numdig=int(input('Digite um valor: ')) #pede valores 6 veces
    if numdig%2==0:
        soma += numdig
        contador += 1
print('Você informou {} números PARES é a soma foi {}'.format(contador,soma))
'''
# Que leia o PRIMERO TERMO e a RAZÃO de uma PA. No final,mostre os 10 PRIMEIROS TERMOS DESSA PROGRES
'''
primeiro=int(input('Digite o primero termo: '))
razao=int(input('Digite a razão '))
decimo=primeiro+(10)*razao
for c in range(primeiro,decimo,razao):
    print('{}'.format(c), end=' ')
'''
# Que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO (divisivel por 1 e por ele mesmo)
'''
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0 and num % 1 == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('\033[32mE por isso ele É PRIMO!')
else:
    print('\033[31mE por isso ele NÃO É PRIMO!')
'''
# Que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderendo os espaços.
'''
frase = str(input('Digite sua frase: ')).strip().upper() #elimina espaço antes,depois - maiuscula
palavras = frase.split() #gera lista palabras separadas (Vetor)
junto = ''.join(palavras) #junta espaço
#inverso = ''
inverso = junto[::-1]
#for letra in range(len(junto) - 1, -1, -1): #len(junto)total caracteres
#    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[32mTemos um PALÍNDROMO')
else:
    print('\033[31mA frase digitada NÃO É UM PALÍNDROMO')
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA
'''
# Que leia o ANO DE NASCIMENTO de SETE PESSOAS.No final,mostre quantas pessoas ainda não atingiram
# a MAIORIDADE e quantas já são MAIORES.
'''
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoas in range(1, 8):
    nascimento = int(input('Digite o ano a {}ª de nascimento: '.format(pessoas)))
    idade = atual - nascimento
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))
'''
# Que leia o PESO de CINCO PESSOAS.No final,mostre qual foi o MAIOR e o MENOR peso lidos.
'''
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))
'''
# Que leia o NOME,IDADE e SEXO de 4 PESSOAS. No final do programa mostre: A MEDIA DE IDADE do grupo
# Qual é o nome do homem MAIS VELHO, Quantas mulheres têm MENOS DE 20 anos.
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).strip()
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
'''
#todo/
# enquanto não maça     while not maça:     while not maça:
#   paso                    paso                if chao:
# pega                  pega                        passo
#                                               if buraco:
#                                                   pula
#                                               if moeda:
#                                                   pega
#                                            pega
'''
for c in range(1, 10):
    print(c)
print('Fim')
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')
'''
'''
for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')
n = 1
while n != 0: # não sai enquanto não digitar 0
    n = int(input('Digite um valor: '))
print('Fim')
'''
# Digite um número e pergunta se quer continuar digitando [S/N]
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).upper()#coloca em maiuscula
print('Fim')
'''
# Que leia quantos números PARES e INPARES foram digitados
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares'.format(par,impar))
'''
# Que leia o SEXO de uma pessoa, mas só aceite os valores 'M'ou'F'.Caso esteja errado, peça a digita
# ção novamente até ter um valor correto.
'''
sexo=str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('Dados inválidos.Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
'''
'''
sexo = 1
M = 0
F = 0
while sexo != 'S':
    sexo=str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
    if sexo != 'S':
        if sexo == 'M':
            M += 1
        elif sexo == 'F':
            F += 1
        else:
            print('Datos invalidos! Por favor, informe seu sexo novamente')
print('Masculino {}, Feminino {}'.format(M,F))
'''
# Onde o computador vai PENSAR em um NUMERO ENTRE 0 E 10. O jogador vai tentar adivinhar até acertar
# mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint
computador = randint(0, 10)
print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites=0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabens!'.format(palpites))
'''
# Que leia DOIS VALORES e mostre um MENU na tela. Seu programa deverá realizar a operação solicitada
# em cada caso.
'''
from time import sleep
primer=int(input('Digite o primeiro valor: '))
segundo=int(input('Digite o segundo valor: '))
opcao=0
while opcao != 5:
    print('''  # \033[36m    [ 1 ] Somar
#    [ 2 ] Multiplicar
#    [ 3 ] Maior
#    [ 4 ] Novos números
#    [ 5 ] Sair do programa\033[m''')
'''    opcao=int(input('Digite la Opção escolhida: '))
    if opcao == 1:
        soma=primer+segundo
        print('A soma entre {} + {} = {}'.format(primer,segundo,primer+segundo))
    elif opcao == 2:
        produto=primer*segundo
        print('Multiplicar {} * {} = {}'.format(primer,segundo,primer*segundo))
    elif opcao == 3:
        if primer > segundo:
            maior=primer
            print('{} é maior'.format(primer))
        else:
            maior=segundo
            print('{} maior'.format(segundo))
            #print('Entre {} e {} o maior valor é {}'.format(primer,segundo,maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        primer = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*10)
print('Fim do programa! Volte sempre!')
'''
# Que leia um NÚMERO qualquer e mostre o seu FATORIAL Ex.5!=5x4x3x2x1=120
'''
num = (int(input('Digite um número: ')))
contador = num
fatorial = 1
print('{}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x 'if contador > 1 else' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
'''
# PRIMERO TERMO e a RAZÃO de uma PA,mostrando os 10 PRIMEROS TERMOS da PROGRESSÃO usando WHILE
'''
primeiro = int(input('Digite o primero termo: '))
razao = int(input('Digite a razão '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} '.format(termo), end='')
    termo *= razao
    contador += 1
'''
# Pergunta para o Usuario se quer ver MAIS TERMOS, encerra quando disser que quer mostrar 0 termos
'''
primeiro = int(input('Digite o primero termo: '))
razao = int(input('Digite a razão '))
termo = primeiro
contador = 1
mais=10
total=0
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais=int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
'''
# Que leia um número n inteiro qualquer e mostre os n primeiros elementos de uma SEQUÊNCIA FIBONACCI
'''
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} {} '.format(t1, t2), end='')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print('{} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print('FIM')
'''
# Que LEIA VÁRIOS NÚMEROS INTEIROS pelo teclado. O programa SÓ VAI PARAR quando o usuário digitar
# o valor 999,que é a condição de parada. No final mostre QUANTOS NÚMEROS FORAM DIGITADOS e qual
# foi A SOMA ENTRE ELES (desconsiderando o flag)999
'''
contador=0
numero=0
soma = 0
numero=int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    contador +=1
    numero = int(input('Digite um número [999 para parar]: '))
print('total numeros digitados {} e a soma entre eles foi {}'.format(contador,soma))
'''
# Que leia VÁRIOS NÚMEROS INTEIROS pelo teclado. No final da execução, MOSTRE A MÉDIA entre todos
# os valores e qual foi O MAIOR E O MENOR valor lido. O programa deve perguntar ao usuário se ele
# quer ou não continuar a digitar valores.
'''
resp = 'S'
media = 0
soma = 0
quantidade = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} números, e a média foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
'''
#todo/
# enquanto Verdadeiro   while True:
#   se terra                if terra
#       passo                   passo
#   se buraco               if buraco
#       pula                    pula
#   se moeda                if moeda
#       pega                    pega
#   se trofeo               if trofeo
#       pula                    pula
#       interrompa              break
# pega                   pega
'''
num = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
#print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')
'''
'''
nome = 'Marco'
idade = 33
salario = 987.3
print(f'O {nome:^15} tem {idade} anos e ganha R${salario:.2f}.') #PYTHON 3.6
print('O {} tem {} anos.'.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos.'% (nome, idade)) #PYTHON 2
'''
# Que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual
# foi a SOMA entre eles(desconsiderando o flag).
'''
soma = 0
contador = 0
while True:
    numero = int(input('Digite um número: [999 para parar] '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'A soma dos {contador} números digitados é {soma}')
'''
# Que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário.
# O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.
'''
while True:
    numero=int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    for contador in range(1,11):
        print(f'{numero} * {contador:>2} = {numero*contador}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
'''
# Que jogue PAR OU ÍMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o TOTAL de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}.Total de {total}.', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes')
'''
# Que leia a IDADE e o SEXO de VÁRIAS PESSOAS. A cada pessoa cadastrada,o programa deverá perguntar
# se o USUÁRIO quer ou não continuar. No final mostre: A)quantas pessoas tem mais de 18 anos,
# B)Quantos HOMENS foram cadastrados,C)Quantas MULHERES tem menos de 20 ANOS.
'''
tot18 = totH = totM = 0
while True:
    idade=int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F':
        totM += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM} mulheres com menos de 20 anos.')
'''
# Que leia o NOME e o PREÇO de VARIOS PRODUTOS.O programa deverá perguntar se o USUÁRIO vai continuar
# No final mostre: A)Qual é o TOTAL GASTO na compra.B)Quantos produtos custam MAIS de R$1000
# C) Qual é o NOME do produto mais BARATO.
'''
total = totmil = menor = contador = 0
barato = ' '
while True:
    produto=str(input('Nome do Produto: '))
    preço=int(input('Preço: R$ '))
    contador += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
#    else:
#        if preço < menor:
#            menor = preço
#            barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'O total de compras foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
'''
# Que simule o funcionamento de um CAIXA ELETRÔNICO. No início,pergunte ao usuário qual será o VALOR
# A SER SACADO (número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão
# entregues OBS: Considere que o caixa possui cédulas de R$50,20,10 e 1.
'''
valor=int(input('Que valor você quer sacar? R$ '))
total = valor
bilhete = 50
totbilhete = 0
while True:
    if total >= bilhete:
        total -= bilhete
        totbilhete += 1
    else:
        if totbilhete > 0:
            print(f'Total de {totbilhete} cédulas de R${bilhete}')
        if bilhete == 50:
            bilhete = 20
        elif bilhete == 20:
            bilhete = 10
        elif bilhete == 10:
            bilhete = 5
        elif bilhete == 5:
            bilhete = 2
        elif bilhete == 2:
            bilhete = 1
        totbilhete = 0
        if total == 0:
            break
print('Volte sempre ao BANCO UNION! Tenha um bom dia!')
'''
