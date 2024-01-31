
def main():
    """ ( ) --> NoneType
    ... complete ...
    """
    
    print('\nEsse programa executa as transformações (descritas pela operação: listar) em matrizes compostas por números naturais.')
    transform = 0
    
    while transform != 'finalizar':
        print('\n-----------------------------------------------------------------------')
        transform = input('Digite o nome de uma operação: ')
        
        
        if transform == 'listar':
            listar_operacoes()
            
        if transform == 'rebateV':
            matriz = le_arq_cria_matriz()
            imprime_matriz(matriz)
            matrizB = rebate_vertical(matriz)
            print()
            print('Transformação realizada: rebater na vertical')
            imprime_matriz(matrizB)            
        
        if transform  == 'rotaciona':
            matriz = le_arq_cria_matriz()
            imprime_matriz(matriz)
            matrizB = rotaciona(matriz)
            print()
            print('Transformação realizada: rotacionar 90 graus no sentido horário')
            imprime_matriz(matrizB)
        
        if transform == 'submatriz':   
            matriz = le_arq_cria_matriz()
            imprime_matriz(matriz)
            nlin = len(matriz)
            ncol = len(matriz[0])
            
            linSup = int(input('Digite o índice de linha do canto superior esquerdo: '))
            colSup = int(input('Digite o índice de coluna do canto superior esquerdo: '))
            linInf = int(input('Digite o índice de linha do canto inferior direito: '))
            colInf = int(input('Digite o índice de coluna do canto inferior direito: '))
            
            nlinB = linInf - linSup + 1
            ncolB = colInf - colSup + 1
            if nlinB <= nlin and ncolB <= ncol:
                matrizB = submatriz(matriz, linSup, colSup, linInf, colInf)
                print()
                print('\nTransformação realizada: extrair uma submatriz de (',linSup,',',colSup,') a (',linInf,',',colInf, ')', sep='')
                imprime_matriz(matrizB)
                
            else:
                print('\nA posição indicada pelos índices digitados não existe na matriz')
        
        if transform == 'mediaViz':
            matriz = le_arq_cria_matriz()
            imprime_matriz(matriz)
            print()
            print('\nTransformação realizada: obter a matriz da média de vizinhos')
            matrizB = media_vizinhos(matriz)
            imprime_matriz(matrizB)
            
        
        
        if transform == 'somaMed':
            matriz = le_arq_cria_matriz()
            print()
            imprime_matriz(matriz)
            seq=[]
            nlin = len(matriz)
            ncol = len(matriz[0])
            
            for n in range (0, nlin, 1):
                for m in range (0, ncol, 1):        
                    seq.append(matriz[n][m])
            
            matrizb = soma_mediana(matriz)
            print('\nTransformação realizada: construir a matriz somando a mediana')
            imprime_matriz(matrizb)
    print('\n-----------------------------------------------------------------------')
        
    
def cria_matriz(nlinhas, ncolunas, valor):
    
    ''' (int, int, tipo do valor) --> matriz (ou seja, tipo list) 
    Cria uma matriz com nlinhas linhas e ncolunas colunas,
    sendo que cada elemento é igual a valor.
    Retorna a matriz criada.
    '''
    
    matriz = []
    for i in range(0, nlinhas, 1):
      
        linha = []
        for j in range(0, ncolunas, 1):
            linha.append(valor)
    
        matriz.append(linha)
   
    return matriz

def le_arq_cria_matriz():
    """ ( ) --> matriz
    Lê o nome de um arquivo texto contendo as informações de uma matriz
    (ou seja, cada linha do arquivo contêm os elementos da linha
    correspondente da matriz).
    A função abre esse arquivo e ao mesmo tempo que lê os elementos da
    matriz, vai criando a matriz com os números lidos; fecha o arquivo
    e retorna a matriz criada.
    Obs.: Os elementos da matriz são números inteiros não negativos.
    """
    nomeArqEntrada = input("Digite o nome de um arquivo de entrada: ")
    arqEntra = open(nomeArqEntrada, 'r')
    linha = arqEntra.readline()    
    lista_strings = linha.split()
                                  
    nlin = int(lista_strings[0])
    ncol = int(lista_strings[1])    
    matrizA = cria_matriz(nlin, ncol, 0)
    
    for i in range(0, nlin, 1):
        linha = arqEntra.readline()
        lista_strings = linha.split()
      
        for j in range(0, ncol, 1):
            matrizA[i][j] = int(lista_strings[j])      
    arqEntra.close()
    
    return matrizA
              
def imprime_matriz(matriz):
    ''' (matriz) --> NoneType

    Recebe uma matriz de inteiros e imprime-a no formato
    bidimensional de matriz e ajustada nas colunas.
    '''   
    nlin = len(matriz)
    ncol = len(matriz[0]) 
    print("\nMatriz com %d linhas e %d colunas\n" %(nlin, ncol))
        
    for i in range(0, nlin, 1):
        
        for j in range(0, ncol, 1):
            print("%6d" %(matriz[i][j]), end='')
        print()
    print()
    
def rebate_vertical(a):
    """ (matriz) --> matriz
    Recebe uma matriz de inteiros a e constrói a matriz b
    resultante da aplicação da transformação correspondente em a.
    Retorna a matriz b.
    """
    b = [[]]
    nlin = len(a)
    ncol = len(a[0])  
    for i in range (0, nlin, 1):     
        b = b + [[]]
        for k in range (ncol-1, -1, -1):
            b[i].append(a[i][k])
                       
    del b[i+1]
    return b
    
def rotaciona(a):
    """ (matriz) --> matriz
    Recebe uma matriz de inteiros a e constrói a matriz b
    resultante da aplicação da transformação correspondente em a.
    Retorna a matriz b.
    """
    nlin = len(a)
    ncol = len(a[0])
    valor = 0
    
    b = cria_matriz(ncol, nlin, valor)
    nlinB = len(b)
    ncolB =len(b[0])

    ultimaLinhaA = nlin -1 
    primeiraColunaA = 0
       
    for i in range (0, nlinB, 1):       
        for j in range (0, ncolB, 1):    
            b[i][j] = a[ultimaLinhaA][primeiraColunaA]         
            ultimaLinhaA -= 1
        ultimaLinhaA = nlin - 1
        primeiraColunaA += 1
    return b
    
def submatriz(a, linSup, colSup, linInf, colInf):
    """ (matriz, int, int, int, int) --> matriz
    Recebe uma matriz de inteiros a e quatro inteiros:
    linSup e colSup que são os índices de linha e de coluna da posição
    no canto superior esquerdo da submatriz desejada;
    linInf e colInf que são os índices de linha e de coluna da posição
    no canto inferior direito da submatriz desejada.
    A função supõe que existe uma submatriz de a definida por esses
    dois índices; constrói a matriz b resultante da aplicação da
    transformação correspondente em a e retorna a matriz b.
    """

    nlinB = linInf - linSup + 1
    ncolB = colInf - colSup + 1
    valor = 0
    
    contLinhas = linSup
    contColunas = colSup
    b = cria_matriz(nlinB, ncolB, valor)
    
    for i in range (0, nlinB, 1):        
        for j in range (0, ncolB, 1):
            b[i][j] = a[contLinhas][contColunas]
            contColunas += 1      
        contColunas = colSup
        contLinhas += 1
        
    return b
    
def media_vizinhos(a):
    """ (matriz) --> matriz
    Recebe uma matriz de inteiros a. A função supõe que a tem
    pelo menos 3 linhas e pelo menos 3 colunas.
    A função constrói a matriz b resultante da aplicação da
    transformação correspondente em a e retorna a matriz b.
    """
    nlinA = len(a)
    ncolA = len(a[0])
    valorMedio = 0
    a_inicial = a
    valor = 0
    b = cria_matriz(nlinA, ncolA, valor)
        
    for i in range (1, nlinA-1, 1):
        for j in range (1, ncolA-1, 1):
            valorVertical = a_inicial[i][j-1] + a_inicial[i][j+1]
            valorHorizontal = a_inicial[i-1][j] + a_inicial[i+1][j] 
                
            valorMedio = int((valorVertical+ valorHorizontal)/4)
            b[i][j] = valorMedio
    
    b[0] = a[0]
    b[nlinA-1] = a[nlinA-1]
    for q in range (0, nlinA, 1):
        b[q][0] = a [q][0]
        
    for s in range (1, nlinA, 1):
        b[s][ncolA-1] = a[s][ncolA-1]
         
    return b
    
def mediana(seq):
    """ (list) --> int
    Recebe uma lista de inteiros seq.
    Determina e retorna a mediana de seq.
    """
    
    tamanho = len(seq)    
    for i in range(1, tamanho, 1):
        item = seq[i]
        j = i-1
        while j >= 0 and seq[j] > item:
            seq[j+1] = seq[j]
            j -= 1
        seq[j+1] = item  
        
        posicao = (len(seq)+1)//2
        mediana = seq[posicao]
        
    
    seq2=[] 
    trava = True
    
    for k in range(0, tamanho):   
        if k == tamanho-1:
            seq2.append(seq[k])
            trava = False
        
        if trava == True:
            if seq[k] != seq[k+1]:
                num = seq[k]            
                seq2.append(num) 
                
    if len(seq2)%2 == 0:        
        posicao = (len(seq)+1)//2
        valormedio1 = seq[posicao]
        valormedio2 = seq[posicao-1]
        mediana = (valormedio1+valormedio2)//2

        return mediana        
    
    else:   
        
        posicao = (len(seq)+1)//2
        mediana = seq[posicao]
        
        return mediana
    
def soma_mediana(a):
    """ (matriz) --> matriz
    Recebe uma matriz de inteiros a.
    A função constrói a matriz b resultante da aplicação da
    transformação correspondente em a e retorna a matriz b.
    """
    nlinA = len(a)
    ncolA = len(a[0])
    nlinB = nlinA+2
    ncolB = ncolA+2
    valor = 0
    b = cria_matriz(nlinB, ncolB, valor)
    
    for i in range (0, nlinA, 1):
        for j in range (0, ncolA, 1):
            b[i+1][j+1] = a[i][j] + 6
    
    for w in range (0, ncolB, 1):
        b[0][w]=6
        
    for w in range (0, ncolB, 1):
        b[nlinB-1][w]=6
    
    for w in range (0, nlinB, 1):
        b[w][0] = 6
        
    for w in range (0, nlinB, 1):
        b[w][ncolB-1] = 6
    
    return b
     
def listar_operacoes():
    """ ( ) --> NoneType
    Escreve na tela os nomes e os significados das operações que um
    usuário pode escolher.
    """
    print('\nLista dos nomes e das respectivas operações:')
    
    print(f"\n{'rebateV': <12}", end='')
    print('- rebater uma matriz na vertical')
    
    print(f"{'rotaciona': <12}", end='')
    print('- rotacionar uma matriz 90 graus')
    
    print(f"{'submatriz': <12}", end='')
    print('- extrair uma submatriz de uma matriz')
    
    print(f"{'mediaViz': <12}", end='')
    print('- obter a matriz da média de vizinhos')
    
    print(f"{'somaMed': <12}", end='')
    print('- construir a matriz somando a mediana')
    
    print(f"{'listar': <12}", end='')
    print('- listar todas as operações com os seus nomes')
    
    print(f"{'finalizar': <12}", end='')
    print('- finalizar a interação com o usuário')
    

main()