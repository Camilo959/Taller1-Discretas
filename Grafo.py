class Grafo:

    def __init__(self) -> None:
        pass

    def type_graph(self,t_graph):
        """
        """
        GTYPE = {
            "GNMA":"Grafo no dirigido - Matriz de Adyacencia",
            "GNLA":"Grafo no dirigido - Lista de Adyacencia",
            "GNMI":"Grafo no dirigido - Matriz de Incidencia",
            "GDMA":"Grafo dirigido - Matriz de Adyacencia",
            "GDLA":"Grafo dirigido - Lista de Adyacencia",
            "GDMI":"Grafo dirigido - Matriz de Incidencia",
            "GPMA":"Grafo ponderado - Matriz de Adyacencia",
            "GPLA":"Grafo ponderado - Lista de Adyacencia",
            "GPMI":"Grafo ponderado - Matriz de Incidencia",
            "NNNN":"Grafo no identificado",
        }
        if not(t_graph in GTYPE):
            t_graph = "NNNN"
        return GTYPE[t_graph]

    def list_adj(self,graph_l):

        contador = 0
        for i in graph_l.keys():
            for j in graph_l[i]:
                contador += 1

        return len(graph_l), contador

    def matrix_adj(self, graph_a):

        contador = 0
        for i in graph_a:
            for j in i:
                if j != 0:
                    contador += 1

        return len(graph_a), contador

    def matrix_inci(self,graph_i):
        return len(graph_i), len(graph_i[0])