Atividade 03 - Grafo de visibilidade de robô

# Problema:-------------------------------------------------
```
import numpy as np
```
Considere o problema de planejamento de caminho para veículos autônomos. Existem formas diferentes de representar o mapa em que o algoritmo de planejamento deve atuar. Em uma atividade anterior, nos preocupamos com mapas definidos por células, agora vamos trabalhar com uma representação topológica do ambiente (a versão mais à esquerda na figura abaixo).

![Screenshot](p1.png)

Podemos montar esse tipo de mapa, em um espaço poligonal, com uma técnica conhecida como Grafo de Visibilidade. A técnica pode ser observada no início do capítulo Roadmaps do livro Principles of Robot Motion. Em resumo, consideramos como vértices regiões de interesse, como a posição inicial e desejada do robô, além dos pontos de "quinas" dos obstáculos.

![Screenshot](p2.png)

```
# Considere que o arquivo esteja no formato a seguir:
# q_start_x, q_start_y
# q_goal_x, q_goal_y
# <numero de obstaculos>
# <numero de quinas>
# x_quina, y_quina
# ...

def lerVertices(arquivo):
  # escrever código
  return V
```
Dizemos que existe aresta entre dos vértices se houver visada direta entre eles, ou seja, se montamos uma linha reta entre os dois pontos, não há obstáculo, o robô se mantém no espaço de configurações livres de colisão. Podemos formalizar essa característica com a seguinte combinação convexa:

eij≠∅⇔svi+(1−s)vj∈cl(Qfree) 

Será preciso resolver um problema de Point-In-Polygon para saber se algum ponto no decorrer da combinação convexa está no interior de um dos obstáculos. Fica como dica a biblioteca shapely, mas se sintam livres para usar outras abordagens. Considere como custo da aresta a distância entre os vértices.

Gerando um grafo como o a seguir:

![Screenshot](p3.png)

```
def montarGrafoVisibilidade(V):
  # Escrever codigo
  return G
```

O grafo resultante serve como roadmap, não só para ir de  qstart  para  qgoal , mas permite planejar caminhos do veículo para outras regiões do mapa. Tudo isso usando técnicas de teoria dos grafos. Sabendo que o veículo sempre inicia em uma certa posição, podemos explorar algoritmos de busca ainda mais eficientes na estrutura de árvore. Pretende-se então descobrir qual a árvore que passa por todos os vértices e o custo total é mínimo. Esse problema pode ser trabalhado com os algoritmos de Kruskal e Prim, implemente ambos algoritmos.

```
def mstKruskal(G):
  # Escrever código
  return T

def mstPrim(G):
  # Escrever código
  return T
```

Caso o robô inicie em um local não contemplado com um vértice, podemos fazer um caminho até o vértice mais próximo e de lá seguir o roadmap para o local desejado. Portanto, precisamos de uma rotina que descubra qual o vértice do grafo mais próximo dado um ponto no plano.

```
def verticeMaisProximo(T, posicao):
  # Escrever código
  return vertice
```

Agora é possível encontrar o caminho de  qstart  para  qgoal . Para isso, pode ser usada uma técnica padrõa de busca de árvore, seja busca por lagura, profundidade ou mesmo A*.

```
def computarCaminho(T, pos_inicial, pos_final):
  v_inicial = verticeMaisProximo(pos_inicial)
  v_final = verticeMaisProximo(pos_final)
  # Escrever código
  return path

pos_inicial = np.array([1, 10])
pos_final = np.array([10, 1])
```

Da mesma forma, para um par de pontos aleatórios do mapa.

```
pos_inicial = ...
pos_final = ...

path = computarCaminho(T, pos_inicial, pos_final)
```

# Solução: ----------------------------------------------------------------
