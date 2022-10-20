from difflib import ndiff
from email.charset import SHORTEST
import networkx as nx
import matplotlib.pyplot as plt


def agregar_arista(G, u, v, w=1):
    G.add_edge(u, v, weight=w)


if __name__ == "__main__":
    nInicio = input("Seleccione nodo inicio: \n")
    nFin = input("Seleccione nodo a buscar: \n")
    G = nx.Graph()
    G.add_node(nInicio)
    G.add_node(nFin)
    opc = 1

    while opc == 1:
        nodo = input("Ingrese nodo ")
        G.add_node(nodo)
        opc = int(input("Desea agregar otro nodo? 1 = Si, 2 = No: \n"))
    opc = 1
    while opc == 1:
        nodoA = input("Ingrese primer nodo de arista \n")
        nodoB = input("Ingrese segundo nodo de arista \n")
        peso = int(input("Ingrese valor arista \n"))
        agregar_arista(G, nodoA, nodoB, peso)
        opc = int(input("Desea agregar otra arista? 1 = Si, 2 = No: \n"))

    # agregar_arista(G, "X", "A", 3)
    # agregar_arista(G, "X", "B", 2)
    # agregar_arista(G, "A", "B", 4)
    # agregar_arista(G, "A", "C", 2)
    # agregar_arista(G, "B", "D", 3)
    # agregar_arista(G, "C", "D", 4)
    # agregar_arista(G, "C", "F", 4)
    # agregar_arista(G, "D", "F", 3)
    # agregar_arista(G, "F", "Z", 2)
    # agregar_arista(G, "C", "Z", 5)

    pos = nx.layout.shell_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    #StartNode = "B"
    plt.title("Grafo con NetworkX")
    plt.show()
    print(nx.astar_path(G, nInicio, nFin))  # Busqueda por A*
