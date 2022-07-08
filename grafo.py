
import  numpy as np

class Aresta():

    def __init__(self,origem,destino,peso = 0,origem_sec =0,destino_sec=0):
        self.origem = origem
        self.destino = destino
        self.peso = peso
        self.origem_sec = origem_sec
        self.destino_sec = destino_sec
				
    def get_origem(self):
        return self.origem
        
    def get_Destino(self):
        return self.destino

    def set_peso(self,peso):
        self.peso = peso
        
    def	get_Peso(self):
        return self.peso
        
    def set_Origem(self,vertice):
        self.origem = vertice
        
    def set_Destino(self,vertice):
        self.destino = vertice

class Vertice():
    def __init__(self, id, sec = 0,aux=0, visitado = 0):
        self.id = id
        self.id_sec = sec
        self.estimativa = 999999
        self.anterior = "-"
        self.vizinhos = []
        # Vai guarda a que objeto pertece para evitar que crier aresta dentro do objeto
        self.aux = aux
        self.visitado = visitado # Marca de vertice foi visitado, 0: não visitado, 1:visitado

    def set_visitado(self):
        self.visitado = 1

    def get_visitado(self):
        return self.visitado

    def set_vizinho(self,u):
        self.vizinhos.append(u)

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setEstimativa(self, estimativa):
        self.estimativa = estimativa

    def getEstimativa(self):
        return self.estimativa
	
class Grafo():
    def __init__(self, orientado = False, lenV = 0, lenA = 0,lenTA =0  ) -> None:
        self.v = [] # Lista de vertices existente no grafo
        self.a = [] # Lista de aresta existente no grafo
        self.madj = [] # Matriz de adjecencia 
        self.orientado = orientado # Grafo orintado? True or False
        self.ord = lenV # Quantidade de vertices
        self.size = lenA # Quantide de aresta
        # Floyd --------------------------
        self.D = []
        self.A = []
        # Prim --------------------------
        self.T = []
        self.AT = []
        self.ordT = len(self.T)
        self.sizeT = lenTA
        # Busca
        self.caminho = []

    def refazer_vizinhos(self):
        for v in self.v:
            v.vizinhos = [] 
        for a in self.a:
            uobj = self.obj_vertice(a.origem)
            vobj = self.obj_vertice(a.destino)
            uobj.set_vizinho(vobj)

    def r_copy(self,T,AT,ordT,sizeT):
        # Irá torcar a lista de vertices e de aresta pela da subgrafo(arvore geradora minima, gerada por Prim())
        self.v = T
        self.a = AT
        self.ord = ordT
        self.size = sizeT
        self.refazer_vizinhos()

    def copy(self):
        # Retorna os dados da arvore geradora minima criada do grafo por Prim()
        return (self.T,self.AT,len(self.T),len(self.AT))

    def set_orientado(self):
        # Definir de grafo é orintado
        self.orientado = True

    def get_direcionado(self):
        # Grafo orientado
        return self.orientado

    def get_ord(self):
        #Quantidade de vertices
        return len(self.v)
    
    def get_size(self):
        #Quantidade de aresta
        return len(self.a)

    def set_vertice(self,u,aux=0):
        #Adicionar um vertice no grafo
        k = self.existe_vertice(u)
        if k == False:
            # Aux usado no grafo de visibilidade
            u = Vertice(u)
            u.aux = aux
            u.id_sec = self.ord
            self.v.append(u)
            self.ord = self.ord + 1
        else:
            print("Vertice já pertece ao Grafo")

    def existe_vertice(self, u):
        #Verificar se vertice está no grafo
        for i in self.v:
            if i.id == u:
                return True
        return False

    def get_vertices(self):
        #Retorna um lista de vertice presente no grafo
        vertices = []
        for i in self.v:
            vertices.append(i.id)
        return vertices

    def obj_vertice(self,v):
        for i in self.v:
            if i.id == v:
                return i

    def set_aresta(self,u,v,peso):
        if self.existe_aresta(u,v) == False:
            uobj = self.obj_vertice(u)
            vobj = self.obj_vertice(v)
            
            # Adiciona uma aresta com orinetação
            aresta = Aresta(u,v,peso,uobj.id_sec,vobj.id_sec)
            self.a.append(aresta)
            uobj.set_vizinho(vobj)
            self.size = self.size + 1
            if self.orientado == False:
                # Adiciona uma aresta
                aresta = Aresta(v,u,peso,vobj.id_sec,uobj.id_sec)
                self.a.append(aresta)
                vobj.set_vizinho(uobj)
                self.size = self.size + 1
   
    def get_arestas(self):
        # Retorna uma lista com as aresta
        p = []
        for i in self.a: 
            k  = []
            k.append(i.origem)
            k.append(i.destino)
            k.append(i.peso)
            p.append(k)
        return p

    def existe_aresta(self,u,v):
        #Veriificar se existe a aresta
        for i in self.a:
            if i.origem == u and i.destino == v:
                return True 
        return False

    def matriz_adj(self):
        self.madj = np.zeros((len(self.v),len(self.v)))
        for i in self.a:
            self.madj[i.origem-1][i.destino-1] = i.peso
        return self.madj

    def __str__(self) -> str:
        #imprimir grafo
        print("Quantidade de Vertices: {}".format(self.ord))
        print("Quantidade de Arestas: {}".format(self.size))
        print("Vertices: ")
        print(self.get_vertices())
        print("Arestas: ")
        print(self.get_arestas())

# Melhor visualização de grafo com nomes diferentes -------------------------------------------------
    
    def get_arestas_sec(self):
        # Retorna uma lista com as aresta
        p = []
        for i in self.a: 
            k  = []
            k.append(i.origem_sec)
            k.append(i.destino_sec)
            k.append(i.peso)
            p.append(k)
        return p

    def get_vertices_sec(self):
        #Retorna um lista de vertice presente no grafo
        vertices = []
        for i in self.v:
            vertices.append(i.id_sec)
        return vertices

    def str_sec(self):
        #imprimir grafo
        print("Quantidade de Vertices: {}".format(self.ord))
        print("Quantidade de Arestas: {}".format(self.size))
        print("Vertices: ")
        print(self.get_vertices_sec())
        print("Arestas: ")
        print(self.get_arestas_sec())

# Dijkstra --------------------------------------------------------------------
    def get_peso(self,u,v):
        for i in self.a:
            if i.origem == u and i.destino == v:
                return i.peso

    def inicia_vertices(self,u):
        for i in self.v:
            i.estimativa = 99999
            i.anterior = '-'
            if u == i.id:
                i.estimativa = 0
                i.anterior = '-'

    def menor_estimativa(self,lista_vertices):
        dmenor = 99999
        for i in lista_vertices:
            if i.estimativa <= dmenor:
                dmenor = i.estimativa
                v = i
        return v
    
    def print_Dijkstra(self):
        print("Vertices:\t",end="\t")
        for i in self.v:
            print(i.id,end="\t")
        print("\nDistancia:\t",end="\t")
        for i in self.v:
            print("{:.2f}".format(i.estimativa),end="\t")
        print("\nAnteriores:\t", end="\t")
        for i in self.v:
            print(i.anterior,end="\t")
    
    def caminho_minimo(self,u,v):
        cam = []
        iv = self.obj_vertice(v)
        while v != u:
            cam.append(v)
            v = iv.anterior
            iv = self.obj_vertice(v)
        cam.append(v)
        cam1 = list(reversed(cam))
        return cam1

    def Dijkstra(self,u):
        lista_vertices = self.v.copy()
        self.inicia_vertices(u)
        while len(lista_vertices)!= 0:
            v = self.menor_estimativa(lista_vertices)
            lista_vertices.remove(v)
            for i in v.vizinhos:
                peso = self.get_peso((v.id),(i.id))
                nova_estimativa = v.estimativa + peso
                if nova_estimativa < i.estimativa:
                    i.estimativa = nova_estimativa
                    i.anterior = v.id

# Floyd ----------------------------------------------------------------------
    def iniciar_matriz(self):
        self.matriz_adj()
        self.D = self.madj.copy()
        self.A = np.zeros((len(self.v),len(self.v)))
        for l in range(len(self.v)):
            for c in range(len(self.v)):
                if l != c and self.D[l][c] == 0:
                    self.D[l][c] = np.inf
                    self.A[l][c] = 0
                else:
                    self.A[l][c] = c

    def floyd(self):
        self.iniciar_matriz()
        for k in range(len(self.v)):
            for i in range(len(self.v)):
                for j in range(len(self.v)):
                    if self.D[i][j] > self.D[i][k] + self.D[k][j]:
                        self.D[i][j] =  self.D[i][k] + self.D[k][j]
                        self.A[i][j] = self.A[i][k]
        #print(self.D)
        #print(self.A)
        return self.D

# Prim ------------------------------------------------------------------------
    
    def aresta_Prim(self):
        for u in self.T:
            if u.anterior != '-':
                v = u.anterior
                peso = u.estimativa
                
                # Adiciona uma aresta com orientação
                aresta = Aresta(v.id,u.id,peso,v.id_sec,u.id_sec)
                self.AT.append(aresta)
                u.set_vizinho(v)
                self.sizeT = self.sizeT + 1
                aresta = Aresta(u.id,v.id,peso,u.id_sec,v.id_sec)
                self.AT.append(aresta)
                v.set_vizinho(u)
                self.sizeT = self.sizeT + 1
        
    def vizinhos_pertence(self,lista_vertices,viz):
        for i in lista_vertices:
            if i == viz:
                return 1
        return 0

    def Prim(self,u):
        self.inicia_vertices(u)
        lista_vertices = self.v.copy()
        while len(self.T) != self.ord:
            v = self.menor_estimativa(lista_vertices)
            lista_vertices.remove(v)
            self.T.append(v)
            for viz in v.vizinhos:
                if self.vizinhos_pertence(lista_vertices,viz) == 1:
                    peso = self.get_peso((v.id),(viz.id))
                    if peso < viz.estimativa:
                        viz.estimativa = peso
                        viz.anterior = v
        self.aresta_Prim()

#Buscas em arvore -----------------------------------------------------------
    def limpar_visitados(self):
        for v in self.v:
            v.visitado = 0
        self.caminho = []

    def Busca_largura(self,qstart,qgoal):
        F =[]
        b = []
        raiz = self.obj_vertice(qstart)
        raiz.set_visitado()
        F.append(raiz)
        while len(F)!= 0:
            v = F.pop(0)
            b.append(v.id_sec)
            if v.id == qgoal:
                return b
            for viz in v.vizinhos:
                if viz.visitado != 1:
                    viz.set_visitado()
                    F.append(viz)
    
    def Busca_profundidade(self,qstart,qgoal):
        raiz = self.obj_vertice(qstart)
        self.caminho.append(raiz.id)
        raiz.set_visitado()
        for viz in raiz.vizinhos:
            if viz.visitado != 1:
                if qstart != qgoal:
                    self.Busca_profundidade(viz.id,qgoal)
                    self.caminho.remove(viz.id)
                else:
                    print(self.caminho)