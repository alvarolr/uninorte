class Grafo:
  def __init__(self):
    self.grafo = {}

  def adicionar_vertice(self, vertice):
    if vertice not in self.grafo:
      self.grafo[vertice] = []

  def adicionar_arestas(self, v1, v2):
    self.adicionar_vertice(v1)
    self.adicionar_vertice(v2)
    self.grafo[v1].append(v2)
    self.grafo[v2].append(v1)

  def exibir(self):
    for vertice, vizinhos in self.grafo.items():
      print(f'{vertice}: {vizinhos}')


meu_grafo = Grafo()
meu_grafo.adicionar_arestas('A', 'B')
meu_grafo.adicionar_arestas('A', 'C')
meu_grafo.adicionar_arestas('B', 'D')
meu_grafo.adicionar_arestas('E', 'A')
meu_grafo.adicionar_arestas('E', 'B')
meu_grafo.adicionar_arestas('E', 'C')
meu_grafo.adicionar_arestas('E', 'D')
meu_grafo.adicionar_arestas('E', 'F')
meu_grafo.adicionar_arestas('T', 'U')

meu_grafo.exibir()





