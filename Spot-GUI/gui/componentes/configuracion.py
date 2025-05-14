import customtkinter as ctk

class Configuracion(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.ruta = ctk.CTkEntry(self, placeholder_text="Directorio de salida")
        self.ruta.pack(side="left", padx=5, fill="x", expand=True)

        self.bitrate = ctk.CTkOptionMenu(self, values=["320k", "256k", "128k"])
        self.bitrate.set("320k")
        self.bitrate.pack(side="left", padx=5)

        self.formato = ctk.CTkOptionMenu(self, values=["mp3", "m4a", "opus"])
        self.formato.set("mp3")
        self.formato.pack(side="left", padx=5)

        self.guardar = ctk.CTkButton(self, text="Guardar")
        self.guardar.pack(side="left", padx=5)
