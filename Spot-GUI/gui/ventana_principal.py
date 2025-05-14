import customtkinter as ctk
from gui.componentes.barra_busqueda import BarraBusqueda
from gui.componentes.lista_resultados import ListaResultados
from gui.componentes.configuracion import Configuracion

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Spot-GUI")
        self.geometry("900x600")

        self.config = Configuracion(self)
        self.config.pack(pady=5, padx=10, fill="x")

        self.barra = BarraBusqueda(self, self.mostrar_resultados)
        self.barra.pack(pady=5, padx=10, fill="x")

        self.resultados = ListaResultados(self)
        self.resultados.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_resultados(self, data):
        self.resultados.mostrar(data)
