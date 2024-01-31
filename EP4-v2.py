"""
     Nome do aluno:Marcos Vinícius Rodrigues Ribeiro
     Número USP:12558954
     Curso: Bacharelado em Física
     Disciplina: MAC0115  Introdução à Computação
     Turma: 21
     Exercício-Programa 4

          DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
     TODAS AS PARTES ORIGINAIS DESTE EXERCÍCIO-PROGRAMA FORAM
     DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
     DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
     OU PLÁGIO.
         DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESTE
     PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
     ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA SERÃO
     TRATADOS SEGUNDO OS CRITÉRIOS DIVULGADOS NA PÁGINA DA DISCIPLINA.
  
     A seguir você pode descrever alguma ajuda que você recebeu para
     fazer este EP.  Com exceção do material didático de MAC0115, pode
     incluir qualquer ajuda recebida de outra pessoa ou de trecho de
     código (indicando a página ou a fonte) para que o seu programa
     não seja considerado plágio ou irregular.
"""

import random   

def main():  
    """ ( ) --> NoneType
    
    ... complete ...
    """
    
    print('\nEste programa testa limiares de 12 a 20 como estratégia para o jogo 21.')
    n=int(input('Quantos jogos deseja simular para cada limiar? '))  
    for i in range(12,21):
        print(impress(i, n), end='')


def simula_jogador(lim):
    """ (int) --> int
    Recebe um inteiro lim, representando um limiar entre 12 e 20.
    Simule uma jogada do jogador, sorteando as cartas que ele vai pegar.
    Calcula e retorna a soma dos pontos do jogador.
    """
    spontosjog = 0
    while lim > spontosjog:
        carta = random.randint(1, 13)
        if carta > 10:
            carta = 10
        spontosjog = spontosjog + carta
    return spontosjog

def simula_banca(spontosjog):    
    """ (int) --> int
    Recebe um inteiro spontosjog, representando a soma dos
    pontos do jogador.
    Simule uma jogada da banca, sorteando as cartas que ela vai pegar.
    Calcula e retorna a soma dos pontos da banca.
    """
    spontosbanc = 0
    while spontosjog >= spontosbanc:
        carta = random.randint(1, 13)
        if carta > 10:
            carta = 10
        spontosbanc = spontosbanc + carta       
    return spontosbanc

def simula_jogos(lim, nj):   
    """ (int, int) --> int
    Recebe dois inteiros lim e nj.
    O inteiro lim representa um limiar entre 12 e 20, e
    nj representa o número de jogos.
    Esta função deve simular nj jogos para o limiar lim.
    Calcula e retorna a quantidade de jogos que o jogador ganhou.
    """    
    jogvitoria = 0  
    for b in range(nj):
        spontosjog = simula_jogador(lim)
        spontosbanc = simula_banca(spontosjog)           
        if spontosbanc > 21 and spontosjog <= 21:
            jogvitoria = jogvitoria + 1          
    return jogvitoria

def impress(i, n):
    jvit = simula_jogos(i, n)
       
    porcent = float(jvit/n*100)
    asterisco = int(porcent)
    print()        
    print(" %-3s ( %-1.2f%1s) : "  %(i, porcent, '%'),end='')
    
    for p in range (asterisco-1):
        print('*', end='')
    return '*'

main()