# #Faça um programa para manipulação de matriz. O programa deve ter um menu principal onde o usuário deverá escolher o que será executado.

# #Menu principal:

# Preencher a matriz. (Nessa opção o usuário deverá definir o tamanho da matriz e a popular.
# Exibir a matriz formatada na tela (desing de matriz, linha x coluna).
# Calcular e mostrar a soma de todos os elementos da matriz;
# Calcular e mostrar o maior e o menor elemento da matriz, e também suas respectivas posições.
# Procurar por um elemento na Matriz. Se encontrar, retornar a posição do mesmo. Caso exista mais de um elemento igual, mostrar as posições de todos.
# Calcular e exibir a matriz transposta (Trocar linhas por colunas). Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.
# Multiplicar a matriz por um fator escalar. - Multiplique todos os elementos da matriz por esse escalar e mostrar a matriz depois.
# Multiplicação entre duas matrizes. Caso o usuário escolha esse opção, ele deverá popular a segunda matriz e o programa realizar a multiplicação entre a primeira e a segunda matriz. Verificar se é possível realizar a operação.
# Dicas:

# Utilize laços de repetição (for ou while) para percorrer a matriz.
# Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.
# Teste diferentes entradas para validar seu programa.
# O programa deve manipular os elementos da matriz somente por índices.
# Observações:
# Pode usar o comando append() para adicionar os valores na Matriz. 
# Os elementos da Matriz devem ser acessados através do seus respectivos índices.

# Modelo matemático da multiplicação de matrizes

# print('Escolha o que será executado: ')
# print('(1) - A soma de todos os elementos da matriz')
# print('(2) - O maior e o menor elemento da matriz (suas respectivas posições)')
# print('(3) - Procurar por um elemento na Matriz')
# print('(4) - Exibir a matriz transposta')
# print('(5) - Multiplicar a matriz por um fator escalar')
# print('(6) - Multiplicação entre duas matrizes')









linhas = int(input(f"Digite o tamanho da matriz (linhas): "))
colunas = int(input(f"Digite o tamanho da matriz (colunas): "))


matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o valor para a posição: {[i]} {[j]}'))
        linha.append(valor)
    matriz.append(linha)

print('Matriz:')
for linha in matriz:
    print(linha)

soma_total = 0

for i in range (linhas):
    for j in range (colunas):
        soma_total += matriz[i][j]

print(soma_total)