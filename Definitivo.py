# Preencher a matriz. (Nessa opção o usuário deverá definir o tamanho da matriz e a popular.

linhas = int(input(f"Digite o tamanho da matriz (linhas): "))
colunas = int(input(f"Digite o tamanho da matriz (colunas): "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o valor para a posição: {[i]} {[j]}'))
        linha.append(valor)
    matriz.append(linha)

# Exibir a matriz formatada na tela (desing de matriz, linha x coluna).

print('Matriz:')
for linha in matriz:
    print(linha)

# #Menu principal:

print('Escolha o que será executado: ')
print()
print('(1) - A soma de todos os elementos da matriz')
print('(2) - O maior e o menor elemento da matriz (suas respectivas posições)')
print('(3) - Procurar por um elemento na Matriz')
print('(4) - Exibir a matriz transposta')
print('(5) - Multiplicar a matriz por um fator escalar')
print('(6) - Multiplicação entre duas matrizes')


opcao = int(input(f'Escolha: '))

# Calcular e mostrar a soma de todos os elementos da matriz;

if opcao == 1:

    print('\nVocê escolheu a soma de todos os elementos')
    soma_total = 0
    for i in range (linhas):
        for j in range (colunas):
            soma_total += matriz[i][j]


    print(f'\nA soma de todos os elementos da matriz é: {soma_total}')

# Calcular e mostrar o maior e o menor elemento da matriz, e também suas respectivas posições.

if opcao == 2:

    print('\nVocê quer saber o maior e o menor elemento da matriz')

    maior_i = 0
    maior_j = 0

    menor_i = 0
    menor_j = 0

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] > matriz[maior_i][maior_j]:
                maior_i = i
                maior_j = j

            if matriz[i][j] < matriz[menor_i][menor_j]:
                menor_i = i
                menor_j = j

    print(f'\nO maior elemento é: {matriz[maior_i][maior_j]}, na posição: [{maior_i}][{maior_j}]')
    print(f'O menor elemento é: {matriz[menor_i][menor_j]}, na posição: [{menor_i}][{menor_j}]')


# Procurar por um elemento na Matriz. Se encontrar, retornar a posição do mesmo. Caso exista mais de um elemento igual, mostrar as posições de todos.

if opcao == 3:
    
    elemento = int(input('\nQual elemento você procura? '))
    print()

    contador_elemento = 0
    for i in range (linhas):
        elementos = []
        for j in range (colunas):
            if matriz[i][j] == elemento:
                contador_elemento += 1
                print(f'Elemento encontrado na posição: [{i}][{j}]')
                

    if contador_elemento == 0:
        print('Elemento não encontrado')

# Calcular e exibir a matriz transposta (Trocar linhas por colunas). Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.

matriz_transposta = []
if opcao == 4:

    print('A matriz transposta: ')
    for i in range(colunas):
        linha = []
        for j in range(linhas):
            linha.append(matriz[j][i])
        matriz_transposta.append(linha)


    for i in range(colunas):
        for j in range(linhas):
            print(f'{matriz[j] [i]}', end=" ")
        print()

# Multiplicar a matriz por um fator escalar. 


if opcao == 5:
    x = int(input("\nDigite o fator escalar: "))
    for linha in matriz:
        for j in range(len(linha)):
            print(linha[j] * x, end=' ')

# Multiplicação entre duas matrizes.

if opcao == 6:
    matriz2 = []
    linhas2 = int(input("Digite o número de linhas: "))
    colunas2 = int(input("Digite o número de colunas: "))

    for i in range(linhas2):
        linha2 = []
        for j in range(colunas2):
            valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
            linha2.append(valor)
        matriz2.append(linha2)
    
    if colunas != linhas2:
        print("Multiplicação impossível: colunas de A ≠ linhas de B")

    else:
        resultado = []
        for i in range (linhas):
            resultado.append([0] * colunas2)

        for i in range(linhas):
            for j in range(colunas2):
                for k in range(colunas):
                    resultado[i][j] += matriz[i][k] * matriz2[k][j]

        print("\nResultado da multiplicação Matriz 1 x Matriz 2:")
        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                print(resultado[i][j], end=" ")
            print()
