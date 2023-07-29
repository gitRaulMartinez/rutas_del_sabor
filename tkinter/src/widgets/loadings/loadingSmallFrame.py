import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from PIL import Image
from src.utils.images import get_image_path

class LoadingSmallFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT,corner_radius=0)
        self.parent = parent

        self.load_fonts()   
        self.rowconfigure((0,3),weight=1)
        self.columnconfigure((0,2),weight=1)
        self.label_title = ctk.CTkLabel(self, text="Cargando...", padx=5, pady=5, fg_color="transparent", text_color="#607D8B", font=self.text_font)
        self.label_title.grid(row=1, column=1, padx=10, pady=10)
        self.progressbar = ctk.CTkProgressBar(self, width=250, height=10, corner_radius=100, fg_color=color.BG_LIGHT, progress_color=color.PRIMARY)
        self.progressbar.grid(row=2, column=1, padx=10, pady=10)
        self.progressbar.configure(mode="indeterminnate")
        self.progressbar.start()

    def load_fonts(self):
        self.text_font = font.text_hight_font()