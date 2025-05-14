import customtkinter as ctk
from spotify_api import buscar

class BarraBusqueda(ctk.CTkFrame):
    def __init__(self, master, on_resultado):
        super().__init__(master)
        self.on_resultado = on_resultado

        self.entry = ctk.CTkEntry(self, placeholder_text="Buscar en Spotify...")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", lambda e: self.buscar())

        self.boton = ctk.CTkButton(self, text="Buscar", command=self.buscar)
        self.boton.pack(side="left")

    def buscar(self):
        query = self.entry.get()
        if query.strip():
            resultados = buscar(query)
            self.on_resultado(resultados)