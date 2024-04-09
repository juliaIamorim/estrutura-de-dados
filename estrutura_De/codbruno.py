import numpy as np
import os

RED, RESET = "\033[1;31m", "\033[0;0m"

f, r, TAMANHO = 0, 0, 5

fila = np.zeros(TAMANHO) 

# Tela principal
def main(valor=""):
    os.system("cls")
    # Mostrará o retorno para o usuário
    if valor != '':
        print(RED + valor + RESET, '\n')

    print(f'A fila circular é: {fila}, F={f}, R={r} \n')

    match input("Digite uma opção:    1-inserir   2-Remover   3-Consultar\n"):
        case "1":
            inserir()
        case "2":
            remover()
        case "3":
            consultar()

def filaCheia():
    return ((f == 0 or f == 1) and r == TAMANHO) or ((r+1) == f)
        
    
def filaVazia():
    return f == r

# verifica, ao inserir novo dado, se a fila está vazia, para setar a frente e a ré para 0
def verificadorFilaVazia():
    global r, f
    if r == f:
        r, f = 0, 0

def inserir():
    verificadorFilaVazia()
    global r
    if filaCheia():
        return main('A fila está cheia. Overflow')
    else:
        valor = int(input('\nEscreva o valor inteiro que você quer adicionar: '))
        if (r+1) > TAMANHO:
            r = 1
        else:
            r+=1
        fila[r-1] = valor
        return main()
    
def remover():
    global f
    if filaVazia():
        return main('A fila está vazia. Underflow')
    else:
        if (f+1) > TAMANHO:
            f = 1
        else:
            f+=1
        fila[f-1] = 0
        return main()
    
def consultar():
    valor = int(input('\nDigite um número para consultar na fila:  '))
    for x in range(len(fila)):
        if valor == fila[x]:
            return main(f'O valor {valor} está contido no índice {x} da fila.')
    return main('O valor pesquisado não está contido na fila.')

main()
