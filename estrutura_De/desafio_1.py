# Trabalhar com fila ou seja:
    # Entradas pela ré
    # Saídas pela frente
# Inserir um novo elemento
# Remover um elemento
# Exibir um elemento
# Encontrar elemento no array
# DESAFIO: fazer o controle do false overflow (fila circular)

import numpy as np

array = np.zeros(5) #Criar um array de 5 posições e preenchê-lo com zeros
tam_array = 5 #Tamanho do array
re = 0 #Inicializando a variável r para controle de inserção de elementos no array (r = ré)
frente = 0 #Inicializando a variável f para controle de remoção de elementos no array (f = frente)


#INSERINDO NOVO ELEMENTO:

# Função para primeiro verificar se a fila está vazia
def fila_vazia(): 
    if re == frente: #Verifica se a ré e a frente estão na mesma posição
        print('Fila vazia')
    elif re == tam_array:
        print(f'Fila cheia OVERFLOW,\n{array}')
    elif 
    
    else:
        print('Fila cheia')
   




def inserir_elemento(elemento):
    global tam_array
    global re_insercao




#Função para remover elemento
#Função para consultar elemento


while True:
    opcao = 0
    print(int(input('Menu:\n0- SAIR\n1- Inserir novo elemento\n2- Remover elemento\n3- Exibir elemento\n4- Encontrar elemento\n\nEscolha uma das opções acima: ')))

    if opcao == 0:
        break

    elif opcao == 1: #Inserir novo elemento 
        inserir_elemento()

    elif opcao == 2: #Remover elemento
        if len(array) == 0:
            print('UNDERFLOW... Fila vazia\n')
        else:
            remover_elemento()

    elif opcao == 3: #Exibir os elementos 
        print(array)
        print()

    elif opcao == 4: #Procurar elemento
        procura = int(input('Digite o elemento que você quer procurar no array: '))
        consultar_elemento(procura)

    else:
        print('Esta não é uma opção válida!')
        
        



    

