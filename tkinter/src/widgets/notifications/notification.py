import customtkinter as ctk

from PIL import Image

from src.assets.images import path_images

class Notification(ctk.CTkToplevel):
    def __init__(self,parent, message):
        super().__init__(fg_color="#607D8B")
        self.parent = parent

        self.head()
        self.position()
        self.structure()

        self.image_check = ctk.CTkImage(Image.open(path_images("check.png")),size=(25,25))

        self.label_image = ctk.CTkLabel(self,image=self.image_check, text="", fg_color="transparent")
        self.label_image.grid(row=0, column=0, padx=(20,10), pady=10)

        self.label_message = ctk.CTkLabel(self, text=message, padx=5, pady=5, fg_color="transparent", text_color="#EEEEEE", font=ctk.CTkFont(size=15,weight='bold'))
        self.label_message.grid(row=0, column=1, padx=(10,20), pady=10, sticky="ew")  

    def head(self):
        self.title("Notificacion")
        self.attributes("-topmost", True)  # Mostrar la ventana siempre en la parte superior
        self.overrideredirect(True)  # Eliminar bordes y barra de título

        time_to_live = 5  # Tiempo de vida en segundos
        self.after(int(time_to_live * 1000), self.close_window)

    def position(self):
        self.geometry("300x70+{}+{}".format(self.winfo_screenwidth() - 310, self.winfo_screenheight() - 110))

    def structure(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def close_window(self):
        self.destroy()