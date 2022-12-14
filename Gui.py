from Lectura import *
from Limpiar import *
from Convertir import *
from Grafo import *
from tkinter import *
from tkinter import filedialog

class Gui:
    def __init__(self):
        self.contenido = ""

    def inicar_ventana(self):
        self.ventana = Tk()
        self.ventana.geometry("350x120")
        self.ventana.title("Grafos")
        self.iniciar_Componentes()
        self.ventana.mainloop()

    def iniciar_Componentes(self):
        self.lbl_title = Label(self.ventana, text="Inserte la ruta del archivo")
        self.font_title = ("Arial", 10, "bold")
        self.lbl_title.configure(font=self.font_title)
        self.lbl_title.place(x=11, y=15, height=20, width=200)

        self.entry_ruta = Entry(self.ventana)
        self.entry_ruta.place(x=17, y=50, height=25, width=220)

        self.btn_send = Button(self.ventana, text="Buscar", command=self.buscar_archivo)
        self.btn_send.place(x=250, y=45, height=28, width=80)

    def buscar_archivo(self):
        ruta = filedialog.askopenfilename(initialdir="Grafos",title="Select",filetypes = (
            ("text files", "*.txt"),
            ("All files", "*.*")))

        objLectura = Lectura()
        self.contenido = objLectura.read(ruta)
        self.control()
        self.mostrar_grafo()

    def mostrar_grafo(self):
        self.gui2 = Tk()
        self.gui2.title("Mostrando")
        self.gui2.geometry("500x550")
        self.inicar_Componentes_gui2()
        self.gui2.mainloop()

    def inicar_Componentes_gui2(self):
        self.font = ("Arial", 15, "bold")

        self.lbl_type = Label(self.gui2, text="Type")
        self.lbl_type.place(x=25, y=330 ,width=50 ,height=25)
        self.lbl_type.configure(font=self.font)

        self.lbl_vertex = Label(self.gui2, text="Vertex")
        self.lbl_vertex.place(x=17, y=410, width=60, height=25)
        self.lbl_vertex.configure(font=self.font)

        self.lbl_edges = Label(self.gui2, text="Edges")
        self.lbl_edges.place(x=17, y=480, width=60, height=25)
        self.lbl_edges.configure(font=self.font)

        self.entry_graph = Text(self.gui2,width=50, height=15)
        self.entry_graph.place(x=47, y=20)
        self.entry_graph.delete("1.0", "end")
        self.entry_graph.insert("insert", str(self.grafito))

        self.entry_info = Entry(self.gui2)
        self.entry_info.place(x=80, y=320, width=320, height=45)
        self.entry_info.delete(0, END)
        self.entry_info.insert(0, self.info)

        self.entry_vertex = Entry(self.gui2)
        self.entry_vertex.place(x=80, y=398, width=60, height=40)
        self.entry_vertex.delete(0, END)
        self.entry_vertex.insert(0, self.vertex)

        self.entry_edges = Entry(self.gui2)
        self.entry_edges.place(x=80, y=470, width=60, height=40)
        self.entry_edges.delete(0, END)
        self.entry_edges.insert(0, self.edge)

        self.btn_MA = Button(self.gui2, text="MA")
        self.btn_MA.place(x=200, y=397, width=80, height=42)
        self.btn_MA.configure(font=self.font)

        self.btn_MI = Button(self.gui2, text="MI")
        self.btn_MI.place(x=200, y=470, width=80, height=40)
        self.btn_MI.configure(font=self.font)

        self.btn_LA = Button(self.gui2, text="LA")
        self.btn_LA.place(x=350, y=397, width=80, height=40)
        self.btn_LA.configure(font=self.font)

        self.btn_salir = Button(self.gui2, text="Exit",command=self.close_window)
        self.btn_salir.place(x=350, y=470, width=80, height=40)
        self.btn_salir.configure(font=self.font)

    def control(self):
        objLimpiar = Limpiar()
        self.contenido_limpio = objLimpiar.clean_content(self.contenido)
        self.type_graph = self.contenido_limpio[0][0]
        self.contenido_limpio.pop(0)
        self.contenido_matriz = objLimpiar.for_matrix(self.contenido_limpio)
        self.objConvertir = Convertir(self.contenido_matriz, self.type_graph)
        self.grafito = []
        self.info = ""
        self.vertex = 0
        self.edge = 0
        self.objGrafo = Grafo()

        if self.contenido == "Error":
            print("Elige un grafo permitido")

        self.list_graph = ['GDLA', 'GDMA', 'GNLA', 'GNMI', 'GPMA', 'GNMA', 'NNNN']

        if self.type_graph == self.list_graph[0]:
           self.info = self.objGrafo.type_graph("GDLA")
           self.show_content = self.objConvertir.GDLA_f()
           self.grafito = self.objConvertir.view_graph_dict(self.show_content)
           self.vertex = self.objGrafo.list_adj(self.objConvertir.GDLA_f())[0]
           self.edge = self.objGrafo.list_adj(self.objConvertir.GDLA_f())[1]

        if self.type_graph == self.list_graph[1]:
           self.info = self.objGrafo.type_graph("GDMA")
           self.show_content = self.objConvertir.GDMA_f()
           self.grafito = self.objConvertir.view_graph_matrix(self.show_content)
           self.vertex = self.objGrafo.matrix_adj(self.objConvertir.GDMA_f())[0]
           self.edge = self.objGrafo.matrix_adj(self.objConvertir.GDMA_f())[1]
 
        if self.type_graph == self.list_graph[2]:
            self.info = self.objGrafo.type_graph("GNLA")
            self.show_content = self.objConvertir.GNLA_f()
            self.grafito = self.objConvertir.view_graph_dict(self.show_content)
            self.vertex = self.objGrafo.list_adj(self.objConvertir.GDLA_f())[0]
            self.edge = self.objGrafo.list_adj(self.objConvertir.GDLA_f())[1]
    
        if self.type_graph == self.list_graph[3]:
            self.info = self.objGrafo.type_graph("GNMI")
            self.show_content = self.objConvertir.GNMI_f()
            self.grafito = self.objConvertir.view_graph_matrix(self.show_content)
            self.vertex = self.objGrafo.matrix_inci(self.objConvertir.GNMI_f())[0]
            self.edge = self.objGrafo.matrix_inci(self.objConvertir.GNMI_f())[1]
    
        if self.type_graph == self.list_graph[4]:
            self.info = self.objGrafo.type_graph("GPMA")
            self.show_content = self.objConvertir.GPMA_f()
            self.grafito = self.objConvertir.view_graph_matrix(self.show_content)
            self.vertex = self.objGrafo.matrix_adj(self.objConvertir.GPMA_f())[0]
            self.edge = self.objGrafo.matrix_adj(self.objConvertir.GPMA_f())[1]
    
        if self.type_graph == self.list_graph[5]:
            self.info = self.objGrafo.type_graph("GNMA")
            self.show_content = self.objConvertir.GNMA_f()
            self.grafito = self.objConvertir.view_graph_matrix(self.show_content)
            self.vertex = self.objGrafo.matrix_adj(self.objConvertir.GNMA_f())[0]
            self.edge = self.objGrafo.matrix_adj(self.objConvertir.GNMA_f())[1]
    
        if self.type_graph == self.list_graph[6]:
           self.info = self.objGrafo.type_graph("NNN")
           self.grafito = 'NNNN'
           self.vertex = 'NNNN'
           self.edge = 'NNNN'

    def close_window(self):
       self.gui2.destroy()