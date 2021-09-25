'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #[]lista {}dicionario
print(lanche) #('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) #Suco
print(lanche[-2]) #Pizza
print(lanche[1:3]) #'Suco','Pizza'
print(lanche[2:]) #('Pizza', 'Pudim')
print(lanche[:2]) #('Hambúrguer', 'Suco')
print(lanche[-2:]) #('Pizza', 'Pudim')
print(len(lanche)) # 4
print(sorted(lanche))# Organizado, Em ordem = ['Hambúrguer', 'Pizza', 'Pudim', 'Suco']
for comida in lanche:
    print(f'Eu vou comer {comida}') #faz com os 4 items
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #faz com os 4 items com posição
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]} na posição {contador}') #faz com os 4 items com posição
    print(contador) #printa 0123
    print(lanche[contador]) #printa todos os items
print('Comi pra caramba!')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) # (2, 5, 4, 5, 8, 1, 2) b + a = inversa
print(len(c)) # 7 So conta a quantidade de elementos
print(c.count(5)) # 2 Quantas veces aparece 5
print(c.index(8)) # 1 Em que posição esta o 8 (5, 1) Procura 5 depois da posição 1
pessoa = ('Gustavo', 39, 'M', 99.88) # Aceita tanto números como letras
del(pessoa) # Deleta a lista de cima por inteiro
print(pessoa) # ('Gustavo', 39, 'M', 99.88)
'''
#Que tenha uma TUPLA totalmente preenchida com uma contagem por extenso,de ZERO até VINTE. Seu
#programa deverá ler um número pelo teclado (ENTRE 0 E 20) e mostrá-lo por EXTENSO.
'''
contagem=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze',
        'doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
#ndigitado=int(input('Digite um número entre 0 e 20: '))
#while ndigitado > 20 or ndigitado < 0:
#    ndigitado=int(input('Tente novamente. Digite um número entre 0 e 20: '))
#else:
#    print(f'Você digitou o número {contagem[ndigitado]}')
while True:
    ndigitado=int(input('Digite um número entre 0 e 20: '))
    if 0 <= ndigitado <= 20:
        break
    print('Tente novamente: ', end='')
print(f'Você digitou o número {contagem[ndigitado]}')
'''
#Crie uma TUPLA preenchida com os 20 primeiros da Tabela do CAMPEONATO BRASILEIRO DE FUTEBOL,
#na ordem de colocação.Depois mostre:A)Apenas os 5 PRIMEIROS colocados.B)Os ULTIMOS 4 colocados
#C)Uma lista com os times em ORDEM ALFABÉTICA.D)Em que POSIÇÃO na tabela esta o CHAPECOENSE
'''
Flia=('Marco','Fernanda','Gladys','Jose','Juan','Veronica',
      'Patty','Claudia','Daynor','Micky','Yashel')
#for f in Flia:
#    print(f) #Outra forma de imprimir a lista
print(f'Lista da Familia: {Flia}')
print(f'Os cinco primeiros são {Flia[:5]}')
print(f'Os 4 últimos são {Flia[-4:]}')
print(f'Familia em ordem alfabética: {sorted(Flia)}')
print(f'A Patty está na {Flia.index("Patty")+1}ª posição')
'''
#Que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA.Depois disso,mostre a LISTAGEM DE
# NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla.
'''
from random import randint
sorteo = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
contador = sorteo
print('Os valores sorteados foram: ', end='')
for s in sorteo:
    print(f'{s}', end=' ')
print(f'\nO maior valor sorteado foi {max(sorteo)}')
print(f'O menor valor sorteado foi {min(sorteo)}')
'''
#Que leia QUATRO VALORES pelo teclado e aguarde-os em uma TUPLA.No final mostre:A)Quantas veces
#apareceu o valor 9.B)Em que posição foi digitado o primeiro 3.C)Quais foram os números PARES
'''
valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
'''
#Que tenha uma TUPLA única com NOMBRES DE PRODUTOS e seus respectivos PREÇOS, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma TABULAR.
'''
listagem = ('Lápiz', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
'''
#Que tenha uma TUPLA com VÁRIAS PALAVRAS (não usar acentos). Depois disso, você deve mostrar,para
#cada palavra, quais são as suas VOGAIS.
'''
palavras = ('aprender', 'programar', 'linguagem', 'pythom', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos => ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': #para adicionar palavras acentuadas adiciona aqui áàâ...
            print(letra, end=' ')
'''
#todo/
# lanche = ['hamburguer','suco','pizza','pudim']
# lanche[3]='picole' substitui a posição 3 da lista
# lanche.append('picole') adiciona un item na lista no final
# lanche.insert(0,'suco') adiciona na posição 0
# del lanche[3] Eliminar el 3
# lanche.pop(3) E pra eliminar o ultimo elemento mais se tem() elimina o que estiver dentro
# lanche.remove('pizza') Você indica o valor que quer eliminar
# if 'pizza' in lanche:   lanche.remove('pizza') So remove se estiver dentro da lista
# valores=list(range(4,11)) 4 5 6 7 8 9 10 Ordenado valores=[8,2,5,4,9,3,0] Desordenado
# valores.sort() Ordena os valores ascendente valores.sort(reverse=True) Ordem inverso
# len(valores) 7 Total de valores contando 0
'''
num=[2, 5, 9, 1]
num[2]=3 #[2, 5, 3, 1]
num.append(7) #[2, 5, 3, 1, 7]
num.sort(reverse=True) #[7, 5, 3, 2, 1]
num.insert(2,0) #[7, 5, 0, 3, 2, 1]
num.pop() #[7, 5, 0, 3, 2] se adiciona (2) a posição vai ser eliminada
num.insert(2, 2) #[7, 5, 2, 3, 2]
num.remove(2) #[7, 5, 3, 2]
if 4 in num: #Só remove se achar o 4
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos') # 5 elementos
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='') #5...9...4...
numeros = list()
for cont in range(0, 5):
    numeros.append(int(input('\nDigite um valor: ')))
for c,n in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {n}!')
a = [2, 3, 4, 7]
b = a # b = a[:] b recebe uma copia dos valores de a e substitui 8 só na lista b
b[2]=8
print(a) 
print(b) # [2, 3, 8, 7] Substitui a posição 2 nas duas listas
'''
#Que leia 5 VALORES NUMÉRICOS e guardeos em uma LISTA. No final,mostre qual foi o MAIOR e o MENOR
#valor digitado e as suas respetivas POSIÇÕES na lista.
'''
maior = 0
menor = 0
listanum = list()
for contador in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {contador}: ')))
    if contador == 0:
        maior = menor = listanum[contador]
    else:
        if listanum[contador] > maior:
            maior = listanum[contador]
        if listanum[contador] < menor:
            menor = listanum[contador]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...',end='')
'''
# Onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os um uma LISTA. Caso o número
# já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final,serão exibidos todos os VALORES ÚNICOS
# digitados em ORDEM CRESCENTE
'''
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
'''
#Onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma LISTA, JÁ NA POSIÇÃO
# CORRETA de inserção (sem usar o sort()) No final,mostre a LISTA ORDENADA na tela.
'''
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
'''
#Que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA. Depois disso,mostre:A)QUANTOS números foram
#digitados.B)A lista de valores,ordenada de forma DECRESCENTE.C)Se o valor 5 está ou não na LISTA
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista')
'''
#Que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA. Depois disso,crie DUAS LISTAS EXTRAS que vão
#conter apenas os valores PARES e os valores IMPARES digitados, respectivamente. Ao final,mostre
#o conteúdo das TRÊS LISTAS geradas.
'''
numeros = list()
pares = list()
impares = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'A lista cpmpleta é {numeros}')
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
'''
#Onde o usuário digite uma EXPRESSÃO qualquer que use PARÊNTESES.Seu aplicativo deverá analisar
#se a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA.
'''
expressao = str(input('Digite a expressão: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está válida!')
else:
    print('Sua expressão está errada!')
'''
# LISTAS DENTRO DAS LISTAS
'''
dados = list()
dados.append('Tonny')
dados.append(32)
print(dados) #[Tonny, 32]
galera = list()
galera.append(dados[:])
dados[0] = 'Fernanda'
dados[1] = 30
galera.append(dados[:]) #[['Tonny', 32], ['Fernanda', 30]] Cria e modifica uma copia
print(galera) #[['Tonny', 32]]
print(dados[0]) #Tonny muda para Fernanda
print(dados[1]) #32 muda para 30
'''
'''
pessoas = [['Pedro',25],['Tonny',32],['Fernanda',30],['Eloa',3]]
for p in pessoas:
    print(p) #imprime a toda a lista
    print(p[0]) # imprime toda a lista so de nomes
    print(f'{p[0]} tem {p[1]} anos de idade') #imprime toda a lista
print(pessoas[0][0]) #Pedro
print(pessoas[1][1]) #32
print(pessoas[1]) #['Tonny',32]
'''
'''
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera) #[['Marco', 32], ['Eloa', 3], ['Fernanda', 29]]
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
'''
#Qe leia NOME E PESO de VARIAS PESSOAS, guardando tudo em uma LISTA.No final mostre:A)QUANTAS
# pessoas foram cadastradas.B)Uma listagem com as pessoas mais PESADAS.C)Uma listagem com as
# pessoas mais LEVES.
'''
temporario = []
principal = []
maipeso = menpeso = 0
while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maipeso = menpeso = temporario[1]
    else:
        if temporario[1] > maipeso:
            maipeso = temporario[1]
        if temporario[1] < menpeso:
            menpeso = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maipeso}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maipeso:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi de {menpeso}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menpeso:
        print(f'{p[0]}', end=' ')
print()
'''
#85 Onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA q mantenha
#separados os valores PARES e ÍMPARES.No final,mostre os valores pares e ímpares em ordem CRESCENTE
'''
número = [[], []]
valor = 0
for contador in range(1,8):
    valor = int(input(f'Digite o {contador}o. valor: '))
    if valor % 2 == 0:
        número[0].append(valor)
    elif valor % 2 == 1:
        número[1].append(valor)
número[0].sort()
número[1].sort()
print(f'Os valores pares digitados foram: {número[0]}')
print(f'Os valores ímpares digitados foram: {número[1]}')
'''
#86 Q crie uma MATRIZ de DIMENSÃO 3x3 e preencha com valores lidos pelo teclado. No final,mostre a
# MATRIZ na tela,com a formatação correta.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
'''
#87 Aprimore o DESAFIO ANTERIOR,mostrando no final:A)A SOMA de todos os VALORES PARES digitados.
#B)A SOMA dos valores da TERCEIRA COLUNA.C)O MAIOR valor da SEGUNDA LINHA.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')
'''
#88 Q ajude um jogador da MEGA SENA a criar PALPITES.O programa vai perguntar QUANTOS JOGOS serão
#gerados e vai sortear 6 NÚMEROS ENTRE 1 E 60 pra cada jogo,cadastrando tudo em uma LISTA COMPOSTA
'''
from time import sleep
from random import randint
lista = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f' SORTEANDO {quant} JOGO ', '-=' * 3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)
'''
#89 Q leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA.No final,mostre
#um BOLETIM contendo a MÉDIA de cada um e permita que o usuário possa mostrar as NOTAS de cada
#aluno individualmente.
'''
ficha = list()
nome = list()
nota1 = list()
nota2 = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) #[aluno0,[aluno1],aluno2]
    resposta=str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 inperrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
'''