from grafo import Grafo
from arista import Arista, AristaNoDirigida
from nodo_grafo import Nodo_grafo

x = Nodo_grafo('X')
a = Nodo_grafo('A')
b = Nodo_grafo('B')
c = Nodo_grafo('C')
d = Nodo_grafo('D')
f = Nodo_grafo('F')
z = Nodo_grafo('Z')

arista = [AristaNoDirigida(x, a, 3),
AristaNoDirigida(x, b, 2),
AristaNoDirigida(a, b, 4),
AristaNoDirigida(a, c, 2),
AristaNoDirigida(b, d, 3),
AristaNoDirigida(c, d, 4),
AristaNoDirigida(c, f, 4),
AristaNoDirigida(c, z, 5),
AristaNoDirigida(d, f, 3),
AristaNoDirigida(f, z, 2)]

g = Grafo()
for i in arista:
    g.agregar_arista(i)

print(g)
g.print_ady()