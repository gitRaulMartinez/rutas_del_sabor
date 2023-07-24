import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent

        self.load_fonts()

        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.label_title = ctk.CTkLabel(self, text="Bienvenido", padx=5, pady=5, fg_color="transparent", text_color="#607D8B", font=self.title_font)
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def load_fonts(self):
        self.title_font = font.title_font()