from grafo import Grafo
from math import sqrt
from shapely.geometry import Point, Polygon


objetos = []

def peso(u,v):
    # Peso nas aretas
    peso = sqrt((v[0]-u[0])**2 + (v[1]-u[1])**2)
    return round(peso, 2)

def intersecao(x1,y1,x2,y2,x3,y3,x4,y4):
    #(ax,ay) ---> (bx,by)
    #(cx,cy) ---> (dx,dy)
    det =  ((y4 - y3)*(x2-x1)) - ((x4 - x3)*(y2-y1)) 
    if det == 0:
        return 0
    else:
        num_u = ((x4 - x3)*(y1-y3))-((y4-y3)*(x1-x3))
        num_v = ((x2 - x1)*(y1-y3))-((y2-y1)*(x1-x3))
        u = num_u/det
        v = num_v/det
        if 0<=u<=1 and 0<=v<=1:
            return 1
        else:
            return 0

def criar_arestas(G):
    # Irei pega os vertice e criar uma reta entre outros vertices, e vou verificar se existe intersecção com as aresta já criadas dos objetos
    arestas_obj = G.get_arestas()
    vertices = G.get_vertices()
    for v in vertices:
        for vj in vertices:
            if v != vj:
                cont = 0
                for a in arestas_obj:
                    if v != a[0] and v != a[1] and vj != a[0] and vj != a[1]:
                        if intersecao(v[0],v[1],vj[0],vj[1],a[0][0],a[0][1],a[1][0],a[1][1]) == 1:
                            cont = cont + 1
                if cont == 0:
                    # Evitar que crie aresta dentro do objeto
                    obj_v = G.obj_vertice(v)
                    obj_vj = G.obj_vertice(vj)
                    if obj_v.aux != obj_vj.aux:
                        G.set_aresta(v,vj,peso(v,vj))
                    else:
                        # Aresta entre o mesmo objeto
                        poly = Polygon(objetos[obj_v.aux])
                        pmx= (v[0]+vj[0])/2
                        pmy = (v[1]+vj[1])/2
                        pm = Point(pmx,pmy)
                        if poly.contains(pm) == False : 
                            G.set_aresta(v,vj,peso(v,vj))
                    
def criar_grafo(G,arq):
    # Criar o grafo de acordo com o arquivo recebido
    linhas = arq.readlines()
    qstart = linhas[0].strip('\n').split(",")
    qgoal = linhas[1].strip('\n').split(",")
    obj = linhas[2]
    G.set_vertice([float(qstart[0]),float(qstart[1])],int(obj)+1)
    G.set_vertice([float(qgoal[0]),float(qgoal[1])],int(obj)+2)
    linhas.pop(0)
    linhas.pop(0)
    linhas.pop(0)
    for i in range(int(obj)):
        quinas = linhas.pop(0)
        vertices = []
        for j in range(int(quinas)):
            # vertices do objeto
            atual=linhas[0].strip('\n').split(",")
            G.set_vertice([float(atual[0]),float(atual[1])],i)
            vertices.append((float(atual[0]),float(atual[1])))
            linhas.pop(0)
        objetos.append(vertices)
        # Aresta do objeto
        for j in range(len(vertices)):
            # Ligar o obejto
            if j+1 == len(vertices):
                G.set_aresta([vertices[j][0],vertices[j][1]],[vertices[0][0],vertices[0][1]],peso([vertices[j][0],vertices[j][1]],[vertices[0][0],vertices[0][1]]))
            else:
                G.set_aresta([vertices[j][0],vertices[j][1]],[vertices[j+1][0],vertices[j+1][1]],peso([vertices[j][0],vertices[j][1]],[vertices[j+1][0],vertices[j+1][1]]))

    return([float(qstart[0]),float(qstart[1])],[float(qgoal[0]),float(qgoal[1])])

def verticeMaisProximo(T, posicao):
    vertices = T.get_vertices()
    distancia = 9999.0
    proximo = '-'
    for v in vertices:
        p = peso(posicao,v)
        if p < distancia:
            distancia = p
            proximo = v
    return proximo

def main():
    # Grafo de visibilidade
    G = Grafo()
    arq = open("mapa.txt")
    qstart,qgoal = criar_grafo(G,arq)
    criar_arestas(G)
    print("Grafo de Visibilidade:")
    G.__str__()
    print('\n')

    #Arvore geradora minima
    G.Prim(qstart) # Pega o grafo original e criar um subgrafo(Arvóre geradora minima)
    T = Grafo() # Criar a arvore
    v,a,ord,size = G.copy()# Copiar os vertices e as aresta da subarvore gerados em prim()
    T.r_copy(v,a,ord,size)# Cola a subarvore
    print("Árvore Geradora Mínima:")
    T.__str__()
    print('\n')


    # Vertice mais proximo:
    qstart = verticeMaisProximo(T,qstart)
    qgoal = verticeMaisProximo(T,qgoal)
    print("Novo Qstrat: [1.0, 10.0] -> ",qstart)
    print("Novo Qgoal: [10.0, 1.0] -> ",qgoal)
    # Caminho
    print("Caminho Mínimo:")
    T.Busca_profundidade(qstart,qgoal)
    print('\n')

    # QStrat e QGoal aleátorio:
    T.limpar_visitados()
    qstart = verticeMaisProximo(T,[2.6,0.2])
    qgoal = verticeMaisProximo(T,[7.4,6.8])
    print("Novo Qstrat: [2.6,0.2] -> ",qstart)
    print("Novo Qgoal: [7.4,6.8] -> ",qgoal)
    print("Caminho Mínimo:")
    T.Busca_profundidade(qstart,qgoal)
    print('\n')

main()