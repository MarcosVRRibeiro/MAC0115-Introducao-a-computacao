"""
     Nome do aluno:Marcos Vinícius Rodrigues Ribeiro
     Número USP:12558954
     Curso: Bacharelado em Física
     Disciplina: MAC0115  Introdução à Computação
     Turma: 21
     Exercício-Programa 2

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
    
    n = int(input('Digite um inteiro positivo para n: '))
    cont = 1
    print('\n--------------------------------------------------------------')
    while cont <= n:
        print('\nTripla', cont)
          
        m = int(input('\nDigite um inteiro positivo: '))
        p = int(input('\nDigite um inteiro positivo: '))
        o = int(input('\nDigite um inteiro positivo: '))
    
        if m >= p and p >= o and m < p+o:
            a=m
            b=p
            c=o                
        elif m >= o and o >= p and m < p+o:
            a=m
            b=o
            c=p
        elif p >= m and m >= o and p < m+o:
            a=p
            b=m
            c=o                  
        elif p >= o and o >= m and p < m+o:
            a=p
            b=o
            c=m                            
        elif o >= m and m >= p and o < m+p:
            a=o
            b=m
            c=p
        elif o >= p and p >= m and o < m+p:
            a=o
            b=p
            c=m 
    
        if a >= b and b >= c and a < b+c:
            s = (a+b+c)/2
            print ('\nOs inteiros ', a,', ', b, ' e ', c, ' formam os lados de um triângulo.', sep='')
            
            area = (s*(s-a)*(s-b)*(s-c))**(1/2)
            print ('\nA área desse triângulo é ', area,'.', sep='')
                
            if a == b == c:
                        print('\nClassificação quanto aos lados: triângulo equilátero.')
            elif a == b or a == c or b == c:
                        print('\nClassificação quanto aos lados: triângulo isósceles.')
            elif a != b != c:
                        print('\nClassificação quanto aos lados: triângulo escaleno.')
            
            if a**2 == b**2 + c**2:
                    print('\nClassificação quanto aos ângulos: triângulo retângulo.')
            elif a**2 > b**2 + c**2:
                    print('\nClassificação quanto aos ângulos: triângulo obstusângulo.')
            elif a**2 < b**2 + c**2:
                    print('\nClassificação quanto aos ângulos: triângulo acutângulo.')
                        
            import math
            alfa = math.acos(-(a**2 - b**2 - c**2)/(2*b*c)) #oposto ao a
            beta = math.acos(-(b**2 - a**2 - c**2)/(2*a*c)) #oposto ao b
            gama = math.acos(-(c**2 - a**2 - b**2)/(2*a*b)) #oposto ao c
            
            alfa = math.degrees(alfa)
            beta = math.degrees(beta)
            gama = math.degrees(gama)
    
            print('\nOs valores (em graus) dos ângulos desse triângulo são:',"\n", alfa,', ', beta,' e ', gama,'.', sep='')
            print('\n----------------------------------------------------')
            a=0
            b=0
            c=0            
        else:
            print('\nNão existe um triângulo com lados de comprimentos ', p,', ',o,' e ',m,'.',sep='')    
            print('\n----------------------------------------------------')
        cont=cont+1
main()             