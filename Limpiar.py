from Lectura import Lectura

class Limpiar:

    def __init__(self):
        pass

    def clean_content(self, contenido):
        graph = []
        for i in contenido:
            if not i.startswith('#'):
                graph.append(i.split())
        return graph

    def for_matrix(self, contenido):
        grafo_4 = []
        for i in contenido:
            try:
                grafo_4.append([int(x) for x in i])
            except ValueError:
                try:
                    grafo_4.append([float(x) for x in i])
                except ValueError:
                    grafo_4.append([str(x) for x in i])
        return grafo_4
