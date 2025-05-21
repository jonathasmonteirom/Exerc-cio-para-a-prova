def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")
    pass


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """
    from math import ceil
    texto = input("Digite o texto: ")
    tamanho = len(texto)
    meio = ceil(len(texto)/2)
    print(texto[meio:tamanho])
    pass

def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    num = int(input("Digite um número: "))
    for i in range(1, 11):
        print(num * i, end=' ')
    print()
    pass


def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
    preposicoes = {"da", "de", "do", "das", "dos", "e", "em", "no", "na", "nos", "nas", "a", "o"}
    nome = input("Digite seu nome em letras minúsculas: ")
    partes = nome.split()
    resultado = []
    for parte in partes:
        if parte in preposicoes:
            resultado.append(parte)
        else:
            resultado.append(parte[:1].upper() + parte[1:])
    print(" ".join(resultado))
    pass

def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    lados = input("Digite os três lados do triângulo (ex: 3 3 3): ").split()
    if len(lados) != 3:
        print("Entrada inválida.")
        return
    a, b, c = map(int, lados)
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("equilátero")
        elif a == b or b == c or a == c:
            print("isósceles")
        else:
            print("escaleno")
    else:
        print("Não é um triângulo")
    pass

def q6():
    """
Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças.
Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade
(intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses
desta vacina, sabendo que são 4(quatro) doses ao total.

"""
    anoInicial = int(input("Ano da 1ª dose: "))
    intervalo = int(input("Periodicidade (em anos): "))
    for i in range(1, 4):
        print(f"{i+1}ª dose: {anoInicial + i * intervalo}")
    pass

def q7():
    
    """
Faça um programa que leia uma sequencia de números e indique se eles são primos ou não.
Você deve parar ao ler o número -1.

"""
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    numero = int(input("Digite um número (-1 para sair): "))  
    if numero == -1:
        print("Encerrando o programa.")
        break
    if primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")
    pass

def q8():
    """
Valquíria trabalha em uma padaria e foi roubada ontem.
Seus clientes ficaram com pena e resolveram organizar uma vaquinha para comprar um novo celular para ela.
Escreva um programa que receba como entrada o valor doado por cada cliente,
até que seja informado um valor negativo, e exiba o total arrecadado e o valor médio doado por eles.

"""
    total = 0
    quantidade = 0
    while True:
        valor = float(input("Digite o valor doado (negativo para encerrar): "))
        if valor < 0:
            break
        total += valor
        quantidade += 1
    if quantidade == 0:
        print("Nenhuma doação recebida.")
    else:
        media = total / quantidade
        print(f"Total arrecadado: {total:.2f}")
        print(f"Valor médio doado: {media:.2f}")
    pass

def q9():
    """
A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária,
o cliente pode alugar um carro de passeio. Para cada diária,
o cliente recebe uma cota de quilometragem de 100 Km.
Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um
cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais.

"""
    dias = int(input("Quantidade de dias: "))
    km = float(input("Quilometragem total rodada: "))

    diaria = 90
    cotaKm = 100 * dias
    extraKm = max(0, km - cotaKm)
    valor_total = dias * diaria + extraKm * 12
    print(f"{valor_total:.2f}")
    pass

def q10():
    """
Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo
usuário para as outras escalas de medida.

Se o usuário fornecer uma temperatura em graus Celsius,
imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit,
imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin,
imprima a mesma temperatura em Fahrenheit e Celsius

"""
    valor = float(input("Digite o valor da temperatura: "))
    escala = input("Digite a escala (C para Celsius, F para Fahrenheit, K para Kelvin): ").strip().upper()

    if escala == "C":
        f = valor * 9/5 + 32
        k = valor + 273.15
        print(f"Fahrenheit: {f:.2f}")
        print(f"Kelvin: {k:.2f}")
    elif escala == "F":
        c = (valor - 32) * 5/9
        k = c + 273.15
        print(f"Celsius: {c:.2f}")
        print(f"Kelvin: {k:.2f}")
    elif escala == "K":
        c = valor - 273.15
        f = c * 9/5 + 32
        print(f"Celsius: {c:.2f}")
        print(f"Fahrenheit: {f:.2f}")
    else:
        print("Escala inválida.")
    pass


if __name__ == "__main__":
 q6()