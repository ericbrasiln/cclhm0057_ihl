'''
Exemplos básicos de python para o curso Ferramentas Digitais e a pesquisa em Humanidades.
https://colab.research.google.com/drive/1kECS91jQHiFXnHt1-LSli_N_jespG3-a?usp=sharing

Autor: Eric Brasil profericbrasil@unilab.edu.br
'''
# print: imprime na tela a informação solicitada
print('Olá, mundo!')

#variável: objeto que recebe um valor
professor = 'Eric'

print(professor)

print(f'Olá, {professor}!')

#input: o usuário insere um valor numa variável
nome = str(input('Qual seu primeiro nome?'))
print('Ok, ',nome,',boa noite')

# números com python

2 + 2

print('Média aritmérica')
n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
m = (n1 + n2)/2
print(f'Sua média final é {m:.1f}')
if m >= 7.0:
    print('Parabéns pela nota, vc está aprovado esse semestre.')
else:
    print('Infelizmente vc terá que fazer a prova final')

#Laço de repetição ou de Iteração#

for c in range(0,7):
    print(c)
print('FIM')

for c in range(6, 0, -1): #o último dado é a iteração: o que o algorítimo vai fazer. Nesse caso, vai reduzir na contagem.
    print(c)
print('FIM')

for c in range (0, 7, 2):
    print(c)
print('Fim')

n = int(input("Digite um número: "))
for c in range(1, n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
p = int(input('Passo: '))
f = int(input('Fim: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')


print('Sorteio numa lista')
import random
# Ou posso usar import random e então depois random.choice(lista)
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))

lista =[al1, al2,al3,al4]

escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}. Parabéns!')

print('Mostrar a ordem de sorteio')
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

"""Ler frase e mostas quantas vezes aparece a letra A, em que posição ela aparece primeiro e em que posição ela aparece em último"""
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

print('--------------------------')



