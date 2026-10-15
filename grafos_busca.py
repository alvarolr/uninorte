# Importa a estrutura de dados 'deque' (fila otimizada) do módulo nativo 'collections'
from collections import deque


# Define a classe do grafo
class Grafo:

  # Método construtor para inicializar o dicionário do grafo
  def __init__(self):
    self.grafo = {}

  # Adiciona um vértice se ele ainda não estiver presente
  def adicionar_vertice(self, vertice):
    if vertice not in self.grafo:
      self.grafo[vertice] = []

  # Adiciona uma aresta bidirecional entre dois vértices
  def adicionar_aresta(self, v1, v2):
    self.adicionar_vertice(v1)
    self.adicionar_vertice(v2)
    self.grafo[v1].append(v2)
    self.grafo[v2].append(v1)


# Cria uma instância do grafo para simular uma rede de pessoas
rede = Grafo()

# Conecta as pessoas formando uma rede de relacionamentos
rede.adicionar_aresta("Ana", "Bruno")
rede.adicionar_aresta("Ana", "Carla")
rede.adicionar_aresta("Bruno", "Daniel")

# Executa a BFS partindo da "Ana" e imprime a ordem de visitação
print("Ordem de visita (BFS):", rede.bfs("Ana"))

# Executa a DFS partindo da "Ana" e imprime a ordem de visitação
print("Ordem de visita (DFS):", rede.dfs("Ana"))
