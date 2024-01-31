"""
     Nome do aluno:Marcos Vinícius Rodrigues Ribeiro
     Número USP:12558954
     Curso: Bacharelado em Física
     Disciplina: MAC0115  Introdução à Computação
     Turma: 21
     Exercício-Programa 3

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
def main():   
    print('\nEste programa testa para n pares de números inteiros positivos,') 
    print('a e b, se a é um segmento de b.')
    n = int(input('Digite o número de pares de inteiros a serem testados: '))
    print('\n--------------------------------------------------------------')
    for i in range(1, n+1, 1):        
        a = int(input('Digite um inteiro positivo para a: '))
        b = int(input('Digite um inteiro positivo para b: '))        
        b_inicial = b
        a_inicial = a
          
        a_n_dig = 0
        while a > 0:
            a = a // 10
            a_n_dig = a_n_dig + 1
               
        test=1
        for p in range(0, a_n_dig, 1):
           test = test*10                             
           
        constante = 1
        if a_inicial == b_inicial:
            print('\n' ,a_inicial,' é um segmento de ', b_inicial, sep='')
        else:
            while b > 0 and constante == 1: 
               segm_b = b%test
               b = b//10           
               if segm_b == a_inicial:
                print('\n' ,a_inicial,' é um segmento de ' , b_inicial, sep='')
                constante = 0
            if constante == 1: 
                print('\n' ,a_inicial,' não é um segmento de ', b_inicial, sep='')
        print('\n--------------------------------------------------------------')
main()