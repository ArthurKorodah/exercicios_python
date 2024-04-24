import os
#----------------------------------------------------------------------------

#Exercício 1
#Crie uma lista para cada informação a seguir:
    #Lista de números de 1 a 10;
    #Lista com quatro nomes;
    #Lista com o ano que você nasceu e o ano atual.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Naim','Zeus','Faer','Eldrid']
ano = [2000,2024]

print(numeros)
print(nomes)
print(ano)
#Feito!

#Exercício 2
#Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
frutas = ['banana','maçã','abacate']
#O 'i' significa item
for i in frutas:
    print(i)
#Feito!

#Exercício 3
#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma = 0
for i in range(1,10,2):
    soma += i
print(soma)                                 
#Feito!

#Exercício 4
#Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
num_dec = [10,9,8,7,6,5,4,3,2,1]
for i in num_dec:
    print(i)
#Feito!

#Exercício 5
#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número,
#indo de 1 a 10.
n = int(input('Digite um número: \n'))
print(f'A tabuada de {n} é: ')
for i in range(1,11):
    print((f'{n} X {i} = '),n * i)
print('\n')
#Feito!

#Exercício 6
#Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.
#Utilize um bloco try-except para lidar com possíveis exceções.
# //Esse exercício força a criatividade a imaginar possíveis erros.
precos = [29.50,32,17.99,12]
soma_precos = 0
try:
    for i in precos:
        soma_precos += i
except:
    print('Algo de errado não está certo')
print(soma_precos)
print('\n')
#Feito!

#Exercício 7
#Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com
#a divisão por zero, caso a lista esteja vazia.
count = 0
somm = 0
list = [26,15,7,22,34,99,70]
#list = []
try:
    for i in list:
        somm += i
        count += 1
    if somm == 0:
        print('A lista esta vazia.')
    else: 
        print(f'A soma da lista é {somm}')
        media = (somm / count)
        print(f'A média da somatória é {media}\n')   
except:
    print('A lista esta vazia.')
#Feito!