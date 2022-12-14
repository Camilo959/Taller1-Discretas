# Recibe una matriz
class Convertir: 

    def __init__(self, list_g, type_graph):
        self.list_g = list_g
        self.type_graph = type_graph
        self.n_vertex = len(list_g)

    def matrix_to_list(self,list_gr,vertex):
        list_adj = {}
        posicion=0

        if not any(0 in sub for sub in list_gr):
            posicion = 1

        for i in range(vertex):
            list_adj.setdefault(i+posicion,list_gr[i])
        return list_adj
    
    def listadj_matrixadj(list_adj):

        n = len(list_adj)
        matriz = [[0 for i in range(n)] for j in range(n)]
        for i, vértice in enumerate(list_adj):
            for vecino in list_adj[vértice]:
                matriz[i][vecino] = 1

        return matriz

    def LA_MA(self,adj_list):

        vertices = []
        for vertex in adj_list:
            vertices.append(vertex)

        vertices.sort()

        adj_matrix = []
        for i in range(len(vertices)):
            adj_matrix.append([0] * len(vertices))

        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if vertices[j] in adj_list[vertices[i]]:
                    adj_matrix[i][j] = 1
        
        return adj_matrix 

    def matriz_diccionario(self, list_matrix): 

        adj_list = []

        for i in range(len(list_matrix)):
            adj_list.append([])
            for j in range(len(list_matrix[i])):
                if list_matrix[i][j] == 1:
                    adj_list[i].append(j)
        new_diccio = self.matrix_to_list(adj_list, len(adj_list))

        return new_diccio 

    def MA_MI(self,adj_matrix, vertex):

        '''
        # 4
        '''
        edges = 0
        for i in range(vertex):
            for j in range(vertex):
                if adj_matrix[i][j] == 1:
                    edges += 1
        incidence_matrix = [[0 for i in range(edges)] for j in range(vertex)]

        edge_index = 0
        for i in range(vertex):
            for j in range(vertex):
                if adj_matrix[i][j] == 1:
                    incidence_matrix[i][edge_index] = 1
                    incidence_matrix[j][edge_index] = 1
                    edge_index += 1
        
        return incidence_matrix 

    def GDLA_f(self):
        return self.matrix_to_list(self.list_g, self.n_vertex)

    def GDMA_f(self):
        list_matrix = self.list_g
        return list_matrix

    def GNLA_f(self):
        return self.matrix_to_list(self.list_g, self.n_vertex)

    def GNMI_f(self):
        list_matrix_mi = self.list_g
        return list_matrix_mi

    def GPMA_f(self):
        list_matrix = self.list_g
        return list_matrix

    def GNMA_f(self):
        list_matrix = self.list_g
        return list_matrix

    def view_graph_dict(self,my_dict={}):
       view_content = ''
       for key, value, in my_dict.items():
           view_content += "".join("{}: {}".format(key,value)) + '\n'
       return view_content
 
    def view_graph_matrix(self,my_matrix=[]):
       view_content = ""
       for row in my_matrix:
           view_content += "".join("{}".format(row)) + '\n'
       return view_content
