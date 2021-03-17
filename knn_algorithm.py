from math import sqrt


# Calcula a Distancia das linhas de teste para cada linha de treino
def distancia_euclidiana(linha1, linha2):
    distancia = 0.0
    for i in range(len(linha1) - 1):
        distancia += (linha1[i] - linha2[i]) ** 2
    return sqrt(distancia)


# Procura os vizinhos mais proximos, k é a quantidade de vizinhos que vai ser ordenado
def retorna_vizinhos(treino, linha_teste, k):
    distancias = list()
    for linha_treino in treino:
        dist = distancia_euclidiana(linha_teste, linha_treino)
        distancias.append((linha_treino, dist))
    distancias.sort(key=lambda tup: tup[1])
    vizinhos = list()
    for i in range(k):
        vizinhos.append(distancias[i][0])
    return vizinhos


# Calcula classe conforme as bases informadas
def retorna_clase(treino, linha_teste, k):
    vizinhos = retorna_vizinhos(treino, linha_teste, k)
    valor_retorno = [linha[-1] for linha in vizinhos]
    classe = max(set(valor_retorno), key=valor_retorno.count)
    return classe


dataset = [
  [1, 10, 200, 1],
  [2, 20, 230, 1],
  [6, 25, 150, 1],
  [7, 45, 100, 1],
  [10, 50, 125, 1],
  [3, 24, 111, 1],
  [100, 4, 10, 2],
  [250, 7, 50, 2],
  [243, 5, 68, 2],
  [210, 2, 90, 2],
  [200, 1, 95, 2],
  [215, 0, 68, 2],
  [56, 200, 1, 3],
  [79, 234, 3, 3],
  [80, 210, 8, 3],
  [95, 200, 10, 3],
  [80, 210, 4, 3],
  [49, 207, 1, 3],
]

datasetTeste = [
  [1, 2, 100],
  [10, 20, 30],
  [8, 5, 20],
  [237, 45, 100],
  [1, 50, 101],
  [67, 121, 12],
]
print('K = 3')
for linha_treino in datasetTeste:
    classe = retorna_clase(dataset, linha_treino, 3)
    print('%s - %d' % (linha_treino, classe))
print('-'*20)
print('K = 5')
for linha_treino in datasetTeste:
    classe = retorna_clase(dataset, linha_treino, 5)
    print('%s - %d' % (linha_treino, classe))
print('-'*20)
print('K = 7')
for linha_treino in datasetTeste:
    classe = retorna_clase(dataset, linha_treino, 7)
    print('%s - %d' % (linha_treino, classe))

