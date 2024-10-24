import random
import Grafo as G
import Carrocinha as CR
import CarrodeLixo as CL


def main():
    graph = G(16)

    # Pesos definidos manualmente
    weights = [5, 10, 3, 15, 20, 7, 8, 4, 9, 12, 6, 11, 2, 13, 14]

    # Conectando vértices
    graph.add_edge(0, 1, weights[0])
    graph.add_edge(1, 3, weights[1])
    graph.add_edge(1, 2, weights[2])
    graph.add_edge(2, 5, weights[3])
    graph.add_edge(3, 6, weights[4])
    graph.add_edge(4, 7, weights[5])
    graph.add_edge(5, 9, weights[6])
    graph.add_edge(6, 8, weights[7])
    graph.add_edge(7, 10, weights[8])
    graph.add_edge(8, 11, weights[9])
    graph.add_edge(9, 12, weights[10])
    graph.add_edge(10, 13, weights[11])
    graph.add_edge(11, 14, weights[12])
    graph.add_edge(12, 15, weights[13])
    graph.add_edge(0, 15, weights[14])

    # Gerar informações aleatórias para os vértices
    graph.gerar_informacoes_aleatorias()

    # Imprimir o grafo
    graph.print_graph()

    # Criar um carro de lixo e exibir suas informações
    carro1 = CL(100, 3, 5)  # Carro com 100 unidades de lixo, 3 funcionários, no vértice 6
    carro1.print_info()

    # Criar três objetos da Carrocinha e exibir suas informações
    carrocinha1 = CR(0, 14)  # 5 animais no vértice 3
    carrocinha2 = CR(0, 14)  # 3 animais no vértice 9
    carrocinha3 = CR(0, 14)  # 7 animais no vértice 15

    # Exibir as informações das carrocinhas
    carrocinha1.print_info()
    carrocinha2.print_info()
    carrocinha3.print_info()


if __name__ == "__main__":
    main()
