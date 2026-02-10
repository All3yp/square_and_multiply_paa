import sys
import numpy as np
from matplotlib import pyplot as plt

sys.set_int_max_str_digits(0)

# computa a potencia da base elevada a n (base^n) usando o algoritmo square and multiply
def square_and_multiply(base, n): 
    global count
    # se a base for 1 ou potencia for 0, retorna 1
    if (base == 1 or n == 0):
        return 1
    # se a potencia for 1, retorna a base (base da recursao, condicao de parada)
    if (n == 1):
        return base
    # divisao e conquista
    # se negativo
    if (n < 0):
        # reescrevendo a potencia de forma que n seja um numero positivo
        return square_and_multiply(1//base, -1 * n)
    # se par
    if (n%2 == 0):
        # conta uma multiplicacao
        count += 1
        # chamada recursiva passando como entrada o quadrado da base (base) e metade da potencia (n)
        return square_and_multiply(base**2, n//2)
    # se impar
    else:
        # conta duas multiplicacoes
        count += 2
        # chamada recursiva passando como entrada o quadrado da base (base) e metade da potencia (n) 
        # O resultado deve ser multiplicado pela base da iteracao, por isso o `* base` no fim da linha
        return square_and_multiply(base**2, n//2) * base

# contador da quantidade de multiplicacoes por execucao
count = 0

# main
def main():
    global count

    # Valida chamada do codigo
    # Exemplo válido: 
    #   `python main.py 2 10`
    #   Nesse caso, a funcao square_and_multiply será chamada para 2^1, 2^2, 2^3, ..., 2^10. 
    #   O resultado e a quantidade de multiplicacoes feitas será armazenado apos cada iteracao
    #   O resultado será printado
    #   A quantidade de multiplicacoes feitas para calcular a potenciacao com algoritmo sera plotada em vermelho
    #   A quantidade de multiplicacoes que seriam feitas para calcular a potenciacao sem o algoritmo sera plotada em azul
    if (len(sys.argv) != 3):
        print('usage: python main.py <base> <max-power>')
        exit(1)

    # Base da potenciacao
    base = int(sys.argv[1])

    # Potencia maxima que sera calculada no exeperimento
    max = int(sys.argv[2])

    # array para armazenar quantas multiplicacoes foram feitas em cada iteracao
    r = np.zeros(abs(max))

    # Para cada i de 1 até a potenciacao maxima, calcula potencia de base^i
    range_positivo = range(1,max+1)
    range_negativo = range(max,0)
    for i in (range_negativo if max < 0 else range_positivo):
        # chama square_and_multiply passando como entrada a base da potenciacao, e a potencia i da iteracao (base^i)
        result = square_and_multiply(base,i)
        
        # printa resultado da potenciacao
        print(f'{base}^{i} | RESULT: {result} | COUNT: {count}')

        # armazena quantas multiplicacoes foram feitas para calcular potenciacao da iteracao
        r[abs(i)-1] = count

        # zera contador de multiplicacoes para ser usado na proxima iteracao
        count = 0

    # plota grafico comparando quantidade de multiplicacoes feitas para pontenciacoes feitas no experimento com o algoritmo vs sem o algoritmo
    x = np.array(range(1,abs(max)+1))
    y = x - 1
    plt.autoscale(tight = True)
    plt.plot(x,y)
    plt.plot(x,r,c='r')
    plt.show()

if __name__ == '__main__':
    main()
