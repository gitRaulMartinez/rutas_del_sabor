import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from src.services.culinaryDestination import CulinaryDestinationService

from PIL import Image
from src.services.google_cloud import get_image
from src.utils.images import get_image_path

class HomeFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent

        self.load_fonts()
        self.load_data()
        self.load_structure()
        self.load_widgets()

    def load_data(self):
        self.culinary_destinations_services = CulinaryDestinationService()
        self.culinary_destinations = self.culinary_destinations_services.get_info()

    def load_fonts(self):
        self.title_font = font.title_font()
        self.name_font = font.text_small_font()

    def load_structure(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

    def load_widgets(self):
        self.label_title = ctk.CTkLabel(self, text="Destinos culinarios", padx=5, pady=5, fg_color="transparent", text_color=color.TEXT, font=self.title_font)
        self.label_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.container = ctk.CTkScrollableFrame(self,fg_color="transparent")
        self.container.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")
        self.container.element = []
        max_column = 4
        for i, culinary_destination in enumerate(self.culinary_destinations):
            self.container.element.append(ctk.CTkFrame(self.container,width=150, height=200))
            self.container.element[i].grid(row=i//max_column,column=i%max_column, padx=10, pady=10)
            self.container.element[i].columnconfigure((0,1), weight=1)
            self.container.element[i].logo_image = ctk.CTkImage(Image.open(get_image(culinary_destination.logo)),size=(100,100))
            self.container.element[i].logo_label = ctk.CTkLabel(self.container.element[i],image=self.container.element[i].logo_image, fg_color=color.BG_LIGHT,text="",corner_radius=0,width=100,height=100)
            self.container.element[i].logo_label.grid(row=0,column=0,columnspan=2,padx=5,pady=(5,5))
            self.container.element[i].title_label = ctk.CTkLabel(self.container.element[i],text=culinary_destination.name, fg_color="transparent",width=200,font=self.name_font)
            self.container.element[i].title_label.grid(row=1,column=0,columnspan=2,padx=5,pady=(5,5),sticky="ew")
            self.container.element[i].start_image = ctk.CTkImage(Image.open(get_image_path("start_light.png")),size=(20,20))
            self.container.element[i].popularity_label = ctk.CTkLabel(self.container.element[i],text=": "+str(culinary_destination.popularity), fg_color="transparent",image=self.container.element[i].start_image,compound="left")
            self.container.element[i].popularity_label.grid(row=2,column=0,padx=5,pady=(5,5),sticky="w")
            self.container.element[i].location_image = ctk.CTkImage(Image.open(get_image_path("map_light.png")),size=(20,20))
            self.container.element[i].location_label = ctk.CTkLabel(self.container.element[i],text=": "+culinary_destination.location_id.short_country, fg_color="transparent",image=self.container.element[i].location_image,compound="left")
            self.container.element[i].location_label.grid(row=2,column=1,padx=5,pady=(5,5),sticky="w")
            self.container.element[i].minimal_price_label = ctk.CTkLabel(self.container.element[i],text="Desde: $ "+str(culinary_destination.minimal_price), fg_color="transparent")
            self.container.element[i].minimal_price_label.grid(row=3,column=0,padx=5,pady=(5,5),sticky="w")
            self.container.element[i].maximum_price_label = ctk.CTkLabel(self.container.element[i],text="Hasta: $ "+str(culinary_destination.maximum_price), fg_color="transparent")
            self.container.element[i].maximum_price_label.grid(row=3,column=1,padx=5,pady=(5,5),sticky="w")
            self.container.element[i].details_button = ctk.CTkButton(self.container.element[i],text="Mas detalles",command=self.more_details)
            self.container.element[i].details_button.grid(row=4,column=0,columnspan=2,padx=5,pady=(5,5),sticky="ew")

    def more_details(self):
        print("Mas detalles")





