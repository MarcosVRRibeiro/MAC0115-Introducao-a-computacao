
cores = ['NENHUMA','VERDE','AMARELO','AZUL','BRANCO']
coresPaises = []

def main():
    """ () --> NoneType
    ... complete ...
    """
    #input('Digite o nome do arquivo de entrada:')
    listaViz = le_cria_listas_vizinhos()
    n = len(listaViz)
    coresPaises = [0]*n
    coresPaises[0]=1
    coresP = coresPaises
    print('cores dos países', coresPaises)
    print()
    
    cont = 1
    c = 1
    colorido = False
    
    while cont < n and colorido == False:
        lViz = listaViz[cont]
        print('\n Esse é o contador e país atual:', cont, '\n E esse deveria ser os vizinhos do país', listaViz[cont])
        p = cont
        
        while c <= 4 and colorido == False:            
            colorido = tentaColorirPais(p, c, lViz, coresP)
            print('coresP atualizada,', coresP, 'cor sendo testada', c)                
            c += 1
        
        if colorido:
            colorido = False
            cont += 1
            c = 1
            
        else:
            cont -= 1
            c = coresP[cont]
            
      
            
        print()
        print('Esse é o país,', cont, 'e esse é o seu colorido', colorido)
        print('CoresP', coresP)
        print('cont', cont)                     
    print('--------------------------------------------------------')
    i=0
    while i < n:
        print('\n', i)
        ncor = coresP[i]
        print('essa é a ncor: ', ncor)
        cor = cores[ncor]
        print('O país é', i, 'sua cor é', cor)
        i += 1
    print('\n', coresP)
        
def le_cria_listas_vizinhos():
    """ () --> list
    Esta função lê todos os dados de um arquivo (conforme descrito no item
    (a)), cujo nome deve ser fornecido pelo usuário.
    A função cria e retorna uma lista, onde o elemento na posição de índice
    i faz referência a uma lista com os números dos países vizinhos do país
    i, com número menor do que i.
    """
    nomeArqEntrada = input('Digite o nome do arquivo de entrada: ')  
    arqEntra = open(nomeArqEntrada, 'r')
    linha = arqEntra.readline() 
    lista = linha.split()
    
    #n = int(lista[0]) 
    #print()
    #print('> linha:', linha)
    #print('> lista:', lista)
    #print('\nnum paises =', n)
    
    
    listaViz = []
    i=0
    for linha in arqEntra:
        lista = linha.split()
        #print('\n> linha: ,', linha)
        #print('> lista:', lista)
        for j in range(0, len(lista), 1):
            lista[j] = int(lista[j])
            
        #print('> lista de vizinhos do país %d: %s' %(i, lista))
        listaViz.append(lista)
        i += 1
    print('\n> lista com a lista de vizinhos para cada país: \n', listaViz)
    arqEntra.close()
    
    return listaViz    
    
def podeColorir(c, lViz, coresP):
    """ (int, list, list) --> bool
    Recebe um inteiro c (entre 1 e 4), uma lista lViz (com os
    vizinhos de algum país p, de número menor do que p) e uma
    lista coresP com as cores já atribuídas aos países de número
    menor do que p.
    Esta função retorna True, se o país p puder ser colorido com
    a cor c; em caso contrário, retorna False.
    """
  
    girar = True
    i = 0
    
    while i < len(lViz):
    #for i in range(1, len(lViz)+1):  
        if girar == True:
            print('DENTRO DA *podeCOLORIR*, qual país', i)
            paisViz = lViz[i]
            corPaisViz = coresP[paisViz]
            print('cor dos países vizinhos:', corPaisViz)
            if corPaisViz == 0:
                return False
            elif c == corPaisViz:
                return False
                girar = False
            i += 1
            
    if girar == True:
        return True
      
def tentaColorirPais(p, c, lViz, coresP):

    """ (int, int, list, list) --> bool
    Recebe dois inteiros, p e c, p representa um país e c uma cor.
    Recebe ainda duas listas, lViz e coresP, lViz é a lista de
    países vizinhos de p com número menor do que p e coresP contém
    as cores já atribuídas aos países de número menor do que p.
    Esta função determina, se possível, o valor da menor cor (>= c e
    <= 4) com a qual é possível colorir o país p.
    Se for possível, atualiza a lista coresP atribuindo a nova cor
    ao país p e retorna True.
    Se não for possível colorir o país p (com uma cor >= c e <= 4),
    retorna False.
    Obs.: Esta função utiliza a função podeColorir.
    """  
    
    colore = podeColorir(c, lViz, coresP)
    print('valor da colore dentro da tenta colorir', colore)
    
    if colore:
        coresP[p] = c        
        return True
    
    
    elif c == 4 and colore == False and coresP[p-1] != 4:        
        coresP[p] = 0
        coresP[p-1] += 1 
        p = p-1
        return False
    elif c == 4 and colore == False:
        coresP[p] = 0
        coresP[p-1] = 0
        coresP[p-2] += 1
        p = p-1
        return False
    
    #elif coresP[p-1]== 4:

    else:
        
        return False
        
     
        
        
    
    
main()