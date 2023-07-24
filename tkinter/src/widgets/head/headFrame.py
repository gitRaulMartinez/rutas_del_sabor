import customtkinter as ctk

import src.utils.fonts as font
import src.utils.colors as color

import src.services.users as user_service
from src.utils.session import get_token

from src.models.user import User

class HeadFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=color.BG_LIGHT,corner_radius=0)
        self.parent = parent

        self.load_fonts()
        self.load_data()
        self.grid_columnconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(self, text="Home", padx=5, pady=5, fg_color="transparent", text_color=color.TEXT, font=self.title_font, anchor="w")
        self.title_label.grid(row=0, column=0, padx=(15,10), pady=13)
        self.name_label = ctk.CTkLabel(self, text=self.user.name, padx=5, pady=5, fg_color="transparent", text_color=color.TEXT, font=self.text_font)
        self.name_label.grid(row=0, column=2, padx=(10,0), pady=14)
        self.lastname_label = ctk.CTkLabel(self, text=self.user.lastname, padx=5, pady=5, fg_color="transparent", text_color=color.TEXT, font=self.text_font)
        self.lastname_label.grid(row=0, column=3, padx=(0,15), pady=13)

    def load_fonts(self):
        self.title_font = font.title_font()
        self.text_font = font.text_normal_font()

    def load_data(self):
        token = get_token()
        result = user_service.get_my_user(token)
        if result is not None:
            self.user = User(**result)
            
