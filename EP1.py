"""
     Nome do aluno:Marcos Vinícius Rodrigues Ribeiro
     Número USP:12558954
     Curso: Bacharelado em Física
     Disciplina: MAC0115  Introdução à Computação
     Turma: 21
     Exercício-Programa 1

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
#-----------------------------------------------------------------------------
def main():
    print('--------------------------------------------------------------------------')
    print('Este programa descreve o dia da Páscoa no intervalo de anos especificados')
    ano_inicial=int(input('Digite um inteiro (>= 1600) para o ano inicial: '))
    ano_final=int(input('Digite um inteiro (>= ano inicial) para o ano final: '))
    print()
    print('As datas dos Domingos de Pascoa de',ano_inicial,'a',ano_final,'estão listadas a seguir: ')
    print()
    ano=ano_inicial
    while ano<=ano_final:
        a = ano%19
        b = ano//100
        c = ano%100
        d = b//4
        e = b%4
        f = (b+8)//25
        g = (b-f+1)//3
        h = (19*a+b-d-g+15)%30
        i = c//4
        j = c%4
        k = (32+2*e+2*i-h-j)%7
        m = (a+11*h+22*k)//451
        n = h+k-7*m+114
        mes = n//31
        dia = 1+n%31
        print(ano,'- dia',dia,'do mês',mes)
        ano=ano+1  
    
    print('--------------------------------------------------------------------------')
main()
