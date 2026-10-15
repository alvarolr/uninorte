from collections import deque
import matplotlib.pyplot as plt
import networkx as nx
import ipywidgets as widgets
from IPython.display import display, clear_output

adj = {'Ana':['Bruno','Carla'], 'Bruno':['Ana','Daniel'], 'Carla':['Ana'], 'Daniel':['Bruno']}
G=nx.Graph()
for v,ns in adj.items():
    G.add_node(v)
    for u in ns: G.add_edge(v,u)
pos={'Ana':(0,1),'Bruno':(-1,0),'Carla':(1,0),'Daniel':(-1,-1)}

def trace_bfs():
    visited=set(); q=deque(['Ana']); visited.add('Ana'); order=[]
    steps=[]
    def snap(line,detail,current=None): steps.append((line,detail,current,list(q),set(visited),list(order)))
    snap('fila = deque([inicio]); visitados.add(inicio)','Ana é colocada na fila e marcada como descoberta.')
    while q:
        cur=q.popleft();snap('vertice_atual = fila.popleft()',f'Retiramos {cur} do início da fila.',cur)
        order.append(cur);snap('ordem_visita.append(vertice_atual)',f'Registramos {cur} na ordem de visita.',cur)
        for neighbor in adj[cur]:
            snap('for vizinho in self.grafo[vertice_atual]',f'Analisando vizinho {neighbor} de {cur}.',cur)
            if neighbor not in visited:
                visited.add(neighbor);q.append(neighbor)
                snap('visitados.add(vizinho); fila.append(vizinho)',f'{neighbor} descoberto e inserido no fim da fila.',cur)
            else: snap('if vizinho not in visitados',f'{neighbor} já descoberto; ignorado.',cur)
    snap('return ordem_visita','A fila ficou vazia. Busca encerrada.')
    return steps

def trace_dfs():
    visited=set(); stack=['Ana']; order=[];steps=[]
    def snap(line,detail,current=None):steps.append((line,detail,current,list(stack),set(visited),list(order)))
    snap('pilha = [inicio]','Ana é colocada na pilha (ainda não visitada).')
    while stack:
        cur=stack.pop();snap('vertice_atual = pilha.pop()',f'Retiramos {cur} do topo da pilha.',cur)
        if cur not in visited:
            visited.add(cur);order.append(cur)
            snap('visitados.add(vertice_atual); ordem_visita.append(vertice_atual)',f'{cur} é marcado e registrado.',cur)
            for neighbor in reversed(adj[cur]):
                snap('for vizinho in reversed(...)',f'Analisando {neighbor} entre os vizinhos de {cur}.',cur)
                if neighbor not in visited:
                    stack.append(neighbor)
                    snap('pilha.append(vizinho)',f'Empilhamos {neighbor} no topo.',cur)
                else:snap('if vizinho not in visitados',f'{neighbor} já foi visitado; ignorado.',cur)
        else:snap('if vertice_atual not in visitados',f'{cur} já visitado; ignorado.',cur)
    snap('return ordem_visita','A pilha ficou vazia. Busca encerrada.')
    return steps

mode=widgets.ToggleButtons(options=[('BFS · Fila','BFS'),('DFS · Pilha','DFS')],description='Algoritmo:')
prev=widgets.Button(description='◀ Anterior'); nxt=widgets.Button(description='Próximo ▶',button_style='primary');reset=widgets.Button(description='↺ Reiniciar')
out=widgets.Output(); state={'index':0}
def render(*args):
    steps=trace_bfs() if mode.value=='BFS' else trace_dfs()
    state['index']=max(0,min(state['index'],len(steps)-1))
    line,detail,cur,container,visited,order=steps[state['index']]
    with out:
        clear_output(wait=True)
        print(f'ETAPA {state["index"]+1} / {len(steps)} | {mode.value}')
        print('INSTRUÇÃO:',line,'\n',detail)
        print('Vértice atual:',cur or '—')
        print(('Fila (início → fim)' if mode.value=='BFS' else 'Pilha (base → topo)')+':',container)
        print('visitados:',sorted(visited),' | ordem_visita:',order)
        colors=['#f59e0b' if v==cur else '#22c55e' if v in order else '#93c5fd' if v in visited else '#e5e7eb' for v in G.nodes]
        fig,ax=plt.subplots(figsize=(7,3.2));nx.draw(G,pos,ax=ax,with_labels=True,node_color=colors,node_size=1700,font_size=11,font_weight='bold',edge_color='#64748b');ax.set_xlim(-1.6,1.6);ax.set_ylim(-1.5,1.5);plt.show()
def move(delta):state['index']+=delta;render()
prev.on_click(lambda _:move(-1));nxt.on_click(lambda _:move(1));reset.on_click(lambda _: (state.update(index=0),render()))
def change(change):state['index']=0;render()
mode.observe(change,names='value')
display(mode,widgets.HBox([prev,nxt,reset]),out);render()
