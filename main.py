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

arista = [Arista(x, a, 3),
Arista(x, b, 2),
Arista(a, b, 4),
Arista(a, c, 2),
Arista(b, d, 3),
Arista(c, d, 4),
Arista(c, f, 4),
Arista(c, z, 5),
Arista(d, f, 3),
Arista(f, z, 2)]

g = Grafo()
for i in arista:
    g.agregar_arista(i)

print(g)
print(g.get_lista_ady())