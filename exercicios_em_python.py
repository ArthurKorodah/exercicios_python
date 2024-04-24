import os

def atividade_alura():
    print('Python na Escola de Programação Alura\n')
    meu_nome = 'Arthur Korodah'
    minha_idade = 23
    print(f'O meu nome é {meu_nome}, e eu tenho {minha_idade} anos.\n')
    print(' A\n L\n U\n R\n A\n')
    #print('A','L','U','R','A',sep='\n')
    #print('''A
    #L
    #U
    #R
    #A''')
    #Aplicação do instrutor ^

    pi = 3.14159
    print(f'O valor de pi é: {pi:.2f}')
atividade_alura()

#def classificar_musica(genero_favorito, genero_musica):
#    if genero_favorito == genero_musica:
#        return 'recomendada'
#    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
#        return 'neutra'
#    else:
#        return 'não recomendada'

#resultado = classificar_musica('Rock', 'Pop')
#print(resultado)


#Exercício 1
print('Escolha um núnero...')
print('Escolhe vai!')
escolha_numero = int(input('Me dá um número, me dá:\n'))
def par_ou_impar():
    if escolha_numero % 2 == 0:
        print('É par!')
    else:
        print('Ímpar aaahhrr!')
par_ou_impar()
#Feito

#Exercício 2
def idade_pessoa():
    idade = int(input('Qual a sua idade? \n'))
    if 0 < idade <= 12:
        print('Você é criançaaa!')
    elif 12 < idade <= 18:
        print('Você é adorrmenscente.')
    elif idade > 18:
        print('Você é adultero... Ops! Adulto.')
    else:
        print('Sinistro...') 
idade_pessoa()
#Feito!

#Exercício 3
nome_usuario = 'batman'
senha_usuario = 'bat2000'
def login():
    nome_digitado = input('Digite o nome de usuário: \n')
    senha_digitada = input('Digite a senha: \n')
    if nome_digitado == nome_usuario and senha_digitada == senha_usuario:
        os.system('clear')
        print('Login Efetuado Com Sucesso!\n')
    else:
        print('O nome de usuário e/ou senha estão incorretos.\n')
login()
#Feito!

#Exercício 4
print('\n')
print('Vamos brincar de nuke bomb! \nMe dê as coordenadas X e Y do local onde iremos brincar!\n')
def jogo_nuke_bomb():
    coordenada_x = float(input('Digite a coordenada X: \n'))
    coordenada_y = float(input('Digite a coordenada Y: \n'))
    print('Certo! Vamos lá!')
    if coordenada_x > 0 and coordenada_y > 0:
        os.system('clear')
        print('Oh! O primeiro quadrante? Pode ser divertido...')
    elif coordenada_x < 0 and coordenada_y > 0:
        os.system('clear')
        print('O segundo quadrante costuma revidar, mas nós daremos conta!')
    elif coordenada_x < 0 and coordenada_y < 0:
        os.system('clear')
        print('KAABUUUM! AAHAHAHA O TERCEIRO SEMPRE É DIVERTIDO!')
    elif coordenada_x > 0 and coordenada_y < 0:
        os.system('clear')
        print('Hmmm... O quarto quadrante tem bastante água em volta, pode ser interessante.')
    else:
        os.system('clear')
        print('Nããão! O eixo é nossa própria localização! AAAAAAAHH!')
jogo_nuke_bomb()
#Feito!

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