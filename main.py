from grafo import Grafo
from arista import Arista, AristaNoDirigida
from nodo_grafo import Nodo_grafo
from arbol import Arbol
x = Nodo_grafo('X')
a = Nodo_grafo('A')
b = Nodo_grafo('B')
c = Nodo_grafo('C')
d = Nodo_grafo('D')
f = Nodo_grafo('F')
z = Nodo_grafo('Z')

arista = [AristaNoDirigida(x.dato, a.dato, 3),
AristaNoDirigida(a.dato, c.dato, 2),
AristaNoDirigida(c.dato, z.dato, 5),
AristaNoDirigida(x.dato, b.dato, 2),
AristaNoDirigida(b.dato, d.dato, 3),
AristaNoDirigida(d.dato, f.dato, 3),
AristaNoDirigida(f.dato, z.dato, 2),
AristaNoDirigida(a.dato, b.dato, 4),
AristaNoDirigida(c.dato, d.dato, 4),
AristaNoDirigida(c.dato, f.dato,4)]

########### Creando el grafo #############
g = Grafo()
for i in arista:
    g.agregar_arista(i)
########### Creando el arbol #############
arbol = Arbol(arista[0].get_par()[0],arista[0].peso)  
for i in range(1,len(arista)):
    arbol.agregar(arista[i].get_par()[1],arista[i].peso)
    arbol.agregar(arista[i].get_par()[0],arista[i].peso)
for i in arista:
    print(i)    
#print(g)
g.print_ady()
#arbol.inorden()

