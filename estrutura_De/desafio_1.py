# Trabalhar com fila ou seja:
    # Entradas pela ré
    # Saídas pela frente
# Inserir um novo elemento
# Remover um elemento
# Exibir um elemento
# Encontrar elemento no array
# DESAFIO: fazer o controle do false overflow (fila circular)

import numpy as np

array = [None] * 5 #Criar um array de 5 posições e preenchê-lo com nada
tam_array = 5 #Tamanho do array
re = 0 #Inicializando a variável r para controle de inserção de elementos no array (r = ré)
frente = 0 #Inicializando a variável f para controle de remoção de elementos no array (f = frente)


#INSERINDO NOVO ELEMENTO:

# Função para primeiro verificar se a fila está vazia
def inserir(elemento): 
    global re
    global frente

    print(f'Ré {re}')
    print(f'Frente {frente}')
    

    #Verificando se tem 2 espaços ou mais vazios para voltar a ré
    qtd = 0
    for i in range(tam_array):
        if array[i] == None:
            qtd = qtd +  1

        if qtd >= 2 and re == tam_array:
            re = 0
    
    if re == frente:
        re = 0
        frente = 0


    if re == tam_array:
            print(f'\nFila cheia = OVERFLOW\n')
    elif re + 1 == frente:
        print(f'Falso Overflow!')
    elif re + 1 != frente:
        array[re] = elemento
        re = re + 1
    
    print(array) 
    print(f'Ré {re}')
    print(f'Frente {frente}')

#Função para remover elemento
def remover():
    global frente
    global re

    print(re)
    print(frente)
    
    if  frente - 1 == re:
        frente = 0

    if re == frente:
        print('Fila vazia = UNDERFLOW\n')

    else:
        array[frente] = None
        frente = frente + 1
    print(array)
    print(re)
    print(frente)
    





#Função para consultar elemento


while True:
    opcao = int(input('Menu:\n0- SAIR\n1- Inserir novo elemento\n2- Remover elemento\n3- Exibir elemento\n4- Encontrar elemento\n\nEscolha uma das opções acima: '))

    if opcao == 0:
        break

    elif opcao == 1: #Inserir novo elemento 
        elemento = int(input('Digite o elemento que quer adicionar: '))
        inserir(elemento)

    elif opcao == 2: #Remover elemento
            remover()

    elif opcao == 3: #Exibir os elementos 
        print(array)
        print()

    elif opcao == 4: #Procurar elemento
        procura = int(input('Digite o elemento que você quer procurar no array: '))
        consultar_elemento(procura)

    else:
        print('Esta não é uma opção válida!')
        
        



    

