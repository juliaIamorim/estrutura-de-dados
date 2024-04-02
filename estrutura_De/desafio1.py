import numpy as np


#Declarando o array de 5 posições e preencher com zeros
array = np.zeros(5)
f = 0
r = 0
tam = 5

# Função para inserir um elemento no array, conferindo se a lista está vazia para receber.
def inserir(elemento):
    global r
    global tam

    i = r
    for i in range(5):
        if r < tam:
            array[i] = elemento
            r = r+1
            i = i+1
            return
    print(f'Ré:{r}')    

# Consultar elementos no array
def consulta(array):
    for i in range(5):
         print(array[i])
  

inserir(2)
inserir(3)
consulta(array)

