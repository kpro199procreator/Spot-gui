import customtkinter as ctk
from PIL import Image, ImageTk
import urllib.request, io
from spotdl_control import descargar

class ListaResultados(ctk.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.resultados_widgets = []

    def mostrar(self, data):
        for widget in self.resultados_widgets:
            widget.destroy()
        self.resultados_widgets.clear()

        for categoria in data.values():
            for item in categoria:
                frame = ctk.CTkFrame(self)
                frame.pack(fill="x", padx=5, pady=5)

                if item.get("imagen"):
                    try:
                        with urllib.request.urlopen(item["imagen"]) as u:
                            raw_data = u.read()
                        im = Image.open(io.BytesIO(raw_data)).resize((64, 64))
                        imagen = ctk.CTkImage(light_image=im, dark_image=im, size=(64, 64))
                        img_label = ctk.CTkLabel(frame, image=imagen, text="")
                        img_label.image = imagen
                        img_label.pack(side="left", padx=10)
                    except:
                        pass

                texto = f'{item["tipo"].title()}: {item["titulo"]}\n{item["artista"]}'
                lbl = ctk.CTkLabel(frame, text=texto, justify="left")
                lbl.pack(side="left", padx=5)

                btn = ctk.CTkButton(frame, text="Descargar", command=lambda url=item["url"]: descargar(url))
                btn.pack(side="right", padx=5)

                self.resultados_widgets.append(frame)
