import random

class VerticeInfo:
    def __init__(self, quantidade_lixo=0, quantidade_cachorros=0, quantidade_gatos=0, quantidade_ratos=0):
        self.quantidade_lixo = quantidade_lixo
        self.quantidade_cachorros = quantidade_cachorros
        self.quantidade_gatos = quantidade_gatos
        self.quantidade_ratos = quantidade_ratos


class AdjListNode:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight
        self.next = None


class AdjList:
    def __init__(self):
        self.head = None

class Graph:
    def __init__(self, V):
        self.array = [AdjList() for _ in range(V)]
        self.vertices = [VerticeInfo() for _ in range(V)]

    def add_edge(self, src, dest, weight):
        new_node = AdjListNode(dest, weight)
        new_node.next = self.array[src].head
        self.array[src].head = new_node

        # Como o grafo é não direcionado, adiciona a aresta no outro sentido também
        new_node = AdjListNode(src, weight)
        new_node.next = self.array[dest].head
        self.array[dest].head = new_node

    def update_vertice_info(self, vertice, lixo, cachorros, gatos, ratos):
        self.vertices[vertice].quantidade_lixo = lixo
        self.vertices[vertice].quantidade_cachorros = cachorros
        self.vertices[vertice].quantidade_gatos = gatos
        self.vertices[vertice].quantidade_ratos = ratos

    def gerar_informacoes_aleatorias(self):
        for i in range(len(self.vertices)):
            # Definindo quantidade aleatória de lixo (entre 10 e 100, por exemplo)
            quantidade_lixo = random.randint(10, 100)

            # Definindo as probabilidades de presença de animais
            quantidade_cachorros = 1 if random.random() < 0.10 else 0  # 10% de chance de ter cachorro
            quantidade_gatos = 1 if random.random() < 0.25 else 0  # 25% de chance de ter gato
            quantidade_ratos = 1 if random.random() < 0.50 else 0  # 50% de chance de ter rato

            # Atualizando o vértice com as informações geradas aleatoriamente
            self.update_vertice_info(i, quantidade_lixo, quantidade_cachorros, quantidade_gatos, quantidade_ratos)

    def print_graph(self):
        for v in range(len(self.array)):
            print(f"\nLista de adjacencia do vertice {v + 1}")
            temp = self.array[v].head
            while temp:
                print(f" -> {temp.dest + 1} (peso: {temp.weight})", end="")
                temp = temp.next
            print()

            print(f"Informacoes do vertice {v + 1}:")
            print(f"Quantidade de Lixo: {self.vertices[v].quantidade_lixo}")
            print(f"Quantidade de Cachorros: {self.vertices[v].quantidade_cachorros}")
            print(f"Quantidade de Gatos: {self.vertices[v].quantidade_gatos}")
            print(f"Quantidade de Ratos: {self.vertices[v].quantidade_ratos}")