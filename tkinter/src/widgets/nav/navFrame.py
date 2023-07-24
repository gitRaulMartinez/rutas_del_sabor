import customtkinter as ctk

from PIL import Image
from src.utils.images import get_image_path

import src.utils.colors as color
import src.utils.fonts as font

class NavFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color=color.NAV)
        self.parent = parent
        self.load_fonts()
        self.load_images()
        self.current_frame = "home"

        self.head()
        self.buttons_nav()
        self.actions()

    def head(self):
        self.label_title = ctk.CTkLabel(self, text=" Rutas del sabor", padx=5, pady=5, text_color=color.TEXT, fg_color="transparent", font=self.logo_font,image=self.logo_icon, compound="left")
        self.label_title.grid(row=0, column=0, padx=15, pady=(15,10))

    def buttons_nav(self):
        self.home_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=15, text="Inicio", text_color=color.TEXT_LIGHT ,fg_color=color.PRIMARY, hover_color=color.PRIMARY, command=lambda: self.switch_frame("home"), font=self.nav_font, image=self.home_light_icon, compound="left", anchor="w")
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.activity_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=15, text="Actividades", text_color=color.TEXT, fg_color="transparent", hover_color=color.HOVER_NAV, command=lambda: self.switch_frame("activity"), font=self.nav_font, image=self.activity_icon, compound="left", anchor="w")
        self.activity_button.grid(row=2, column=0, sticky="ew")

        self.planning_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=15, text="Planificación", text_color=color.TEXT, fg_color="transparent", hover_color=color.HOVER_NAV, command=lambda: self.switch_frame("planning"), font=self.nav_font, image=self.planning_icon, compound="left", anchor="w")
        self.planning_button.grid(row=3, column=0, sticky="ew")

        self.map_button = ctk.CTkButton(self, corner_radius=0, height=40, border_spacing=15, text="Mapa", text_color=color.TEXT, fg_color="transparent", hover_color=color.HOVER_NAV, command=lambda: self.switch_frame("map"), font=self.nav_font, image=self.map_icon, compound="left", anchor="w")
        self.map_button.grid(row=4, column=0, sticky="ew")

    def actions(self):
        self.grid_rowconfigure(5, weight=1)

        self.logout_button = ctk.CTkButton(self, height=20, text="Cerrar Sesión", border_spacing=10, text_color=color.TEXT_BUTTON, fg_color=color.SECONDARY,hover_color=color.HOVER_SECONDARY, command=self.logout, font=self.button_font, image=self.logout_icon, compound="left")
        self.logout_button.grid(row=6, column=0,padx=15,pady=(0,15), sticky="ews")

    def load_images(self):
        self.logo_icon = ctk.CTkImage(Image.open(get_image_path("logo.png")),size=(30,30))
        self.home_icon = ctk.CTkImage(Image.open(get_image_path("home.png")),size=(20,20))
        self.activity_icon = ctk.CTkImage(Image.open(get_image_path("activity.png")),size=(20,20))
        self.planning_icon = ctk.CTkImage(Image.open(get_image_path("plan.png")),size=(20,20))
        self.map_icon = ctk.CTkImage(Image.open(get_image_path("map.png")),size=(20,20))
        self.home_light_icon = ctk.CTkImage(Image.open(get_image_path("home_light.png")),size=(20,20))
        self.activity_light_icon = ctk.CTkImage(Image.open(get_image_path("activity_light.png")),size=(20,20))
        self.planning_light_icon = ctk.CTkImage(Image.open(get_image_path("plan_light.png")),size=(20,20))
        self.map_light_icon = ctk.CTkImage(Image.open(get_image_path("map_light.png")),size=(20,20))
        self.logout_icon = ctk.CTkImage(Image.open(get_image_path("logout_light.png")),size=(15,15))
        

    def switch_frame(self,frame):
        self.home_button.configure(fg_color=color.PRIMARY if frame == "home" else "transparent",text_color=color.TEXT_LIGHT if frame == "home" else color.TEXT,hover_color=color.HOVER_PRIMARY if frame == "home" else color.HOVER_NAV,image=self.home_light_icon if frame == "home" else self.home_icon)
        self.activity_button.configure(fg_color=color.PRIMARY if frame == "activity" else "transparent",text_color=color.TEXT_LIGHT if frame == "activity" else color.TEXT,hover_color=color.HOVER_PRIMARY if frame == "activity" else color.HOVER_NAV,image=self.activity_light_icon if frame == "activity" else self.activity_icon)
        self.planning_button.configure(fg_color=color.PRIMARY if frame == "planning" else "transparent",text_color=color.TEXT_LIGHT if frame == "planning" else color.TEXT,hover_color=color.HOVER_PRIMARY if frame == "planning" else color.HOVER_NAV,image=self.planning_light_icon if frame == "planning" else self.planning_icon)
        self.map_button.configure(fg_color=color.PRIMARY if frame == "map" else "transparent",text_color=color.TEXT_LIGHT if frame == "map" else color.TEXT,hover_color=color.HOVER_PRIMARY if frame == "map" else color.HOVER_NAV,image=self.map_light_icon if frame == "map" else self.map_icon)

        self.parent.switch_frame(frame)
            

    def logout(self):
        self.parent.logout()

    def load_fonts(self):
        self.logo_font = font.logo_font()
        self.nav_font = font.nav_font()
        self.button_font = font.button_font()