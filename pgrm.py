# Faça um programa para manipulação de matriz. O programa deve ter um menu principal onde o usuário deverá escolher o que será executado.

# Menu principal:

# Preencher a matriz. (Nessa opção o usuário deverá definir o tamanho da matriz e a popular.
# Exibir a matriz formatada na tela (desing de matriz, linha x coluna).
# Calcular e mostrar a soma de todos os elementos da matriz;
# Calcular e mostrar o maior e o menor elemento da matriz, e também suas respectivas posições.
# Procurar por um elemento na Matriz. Se encontrar, retornar a posição do mesmo. Caso exista mais de um elemento igual, mostrar as posições de todos.
# Calcular e exibir a matriz transposta (Trocar linhas por colunas). Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.
# Multiplicar a matriz por um fator escalar. - Multiplique todos os elementos da matriz por esse escalar e mostrar a matriz depois.
# Multiplicação entre duas matrizes. Caso o usuário escolha esse opção, ele deverá popular a segunda matriz e o programa realizar a multiplicação entre a primeira e a segunda matriz. 
# Verificar se é possível realizar a operação.



linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o valor para a posição: {[i]} {[j]}: '))
        linha.append(valor)
    matriz.append(linha)


print("Matriz criada:")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end=" ")
    print()


print()

print("Escolha a função que deve ser feita: ")
print("1- Calcular e mostrar a soma de todos os elementos da matriz;")
print("2- Calcular e mostrar o maior e o menor elemento da matriz, e também suas respectivas posições.")
print("3- Procurar por um elemento na Matriz. Se encontrar, retornar a posição do mesmo. Caso exista mais de um elemento igual, mostrar as posições de todos.")
print("4- Calcular e exibir a matriz transposta (Trocar linhas por colunas). Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.")
print("5- Multiplicar a matriz por um fator escalar. - Multiplique todos os elementos da matriz por esse escalar e mostrar a matriz depois.")
print("6- Multiplicação entre duas matrizes. Caso o usuário escolha esse opção, ele deverá popular a segunda matriz e o programa realizar a multiplicação entre a primeira e a segunda matriz.")

print()

escolha = int(input(f"Digite o número da função desejada: "))

# if escolha == 1:
#     soma = 0
#     for i in range (len(linha)):
#         soma = linha[i] + linha[j]
#     print(soma)

if escolha == 6:
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

        print("Resultado da multiplicação Matriz 1 x Matriz 2:")
        for i in range(len(resultado)):
            for j in range(len(resultado[0])):
                print(resultado[i][j], end=" ")
            print()
