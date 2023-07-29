import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from PIL import Image
from src.services.google_cloud import get_image
from src.utils.images import get_image_path

from src.services.culinaryDestination import CulinaryDestinationService

class DestinationFrame(ctk.CTkFrame):
    def __init__(self, parent, culinary_destination_id=None,command=None):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.command = command

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

        self.load_fonts()
        if culinary_destination_id is not None:
            self.load_data(culinary_destination_id)
            self.load_widgets()
        

    def load_fonts(self):
        self.title_font = font.title_font()

    def load_data(self,culinary_destination_id):
        self.culinary_destinations_services = CulinaryDestinationService()
        self.culinary_destination = self.culinary_destinations_services.get_destination(culinary_destination_id)

    def load_widgets(self):
        self.head_frame = HeadDestinationFrame(self, self.culinary_destination,self.command)
        self.head_frame.grid(row=0,column=0,sticky="nwe")


        
class HeadDestinationFrame(ctk.CTkFrame):
    def __init__(self,parent,destination,command=None):
        super().__init__(parent,fg_color="transparent")
        self.culinary_destination = destination
        self.command = command
        self.load_fonts()
        self.load_structure()
        self.load_widgets()
    
    def load_structure(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(2,weight=1)

    def load_fonts(self):
        self.text_font = font.text_normal_font()
        self.title_font = font.title_font()

    def load_widgets(self):
        self.bg_destination_image = ctk.CTkImage(Image.open(get_image(self.culinary_destination.image)),size=(1000,200))
        self.bg_destination_label = ctk.CTkLabel(self,image=self.bg_destination_image,text="",fg_color="transparent")
        self.bg_destination_label.grid(row=0,column=0,columnspan=3,sticky="ew")

        self.logo_destination_image = ctk.CTkImage(Image.open(get_image(self.culinary_destination.logo)),size=(100,100))
        self.logo_destination_label = ctk.CTkLabel(self,image=self.logo_destination_image,text="",fg_color="white",corner_radius=0)
        self.logo_destination_label.grid(row=1,column=0,padx=15,pady=15,rowspan=3,sticky="w")
        
        self.title_destination_label = ctk.CTkLabel(self,text=self.culinary_destination.name, fg_color="transparent",font=self.title_font,anchor="w",text_color=color.TEXT,width=100)
        self.title_destination_label.grid(row=1,column=1,padx=5,pady=5,sticky="ew")

        self.button_back = ctk.CTkButton(self,text="Volver",fg_color=color.SECONDARY,corner_radius=5,font=self.text_font,command=self.command,text_color=color.TEXT_BUTTON,hover_color=color.HOVER_SECONDARY)
        self.button_back.grid(row=1,column=2,padx=15,pady=5,sticky="e")

        self.location_destination_image = ctk.CTkImage(Image.open(get_image_path("map.png")),size=(20,20))
        self.location_destination_label = ctk.CTkLabel(self,image=self.location_destination_image,text="   "+self.culinary_destination.location_id.address,fg_color="transparent",width=20,height=15,text_color=color.TEXT,compound="left",font=self.text_font)
        self.location_destination_label.grid(row=2,column=1,columnspan=2,padx=0,pady=5,sticky="w")

        self.popularity_destination_image = ctk.CTkImage(Image.open(get_image_path("start.png")),size=(20,20))
        self.popularity_destination_label = ctk.CTkLabel(self,image=self.popularity_destination_image,text="   "+str(self.culinary_destination.popularity),fg_color="transparent",width=20,height=15,text_color=color.TEXT,compound="left",font=self.text_font)
        self.popularity_destination_label.grid(row=3,column=1,padx=0,pady=(5,15),sticky="w")

        self.kitchen_destination_label = ctk.CTkLabel(self,text="Tipo de cocina: "+str(self.culinary_destination.type_of_kitchen),fg_color="transparent",width=25,height=25,text_color=color.TEXT,font=self.text_font )
        self.kitchen_destination_label.grid(row=4,column=0,columnspan=2,padx=15,pady=5,sticky="w")

        self.price_destination_label = ctk.CTkLabel(self,text=f"Precio minimo: ${self.culinary_destination.minimal_price}    Precio maximo: ${self.culinary_destination.maximum_price}",fg_color="transparent",width=25,height=25,text_color=color.TEXT,font=self.text_font )
        self.price_destination_label.grid(row=4,column=2,padx=15,pady=5,sticky="e")

        self.ingredients_frame = IngredientsFrame(self)
        self.ingredients_frame.grid(row=5,column=0,columnspan=3,padx=15,pady=5,sticky="ew")
        for ingredient in self.culinary_destination.ingredients:
            self.ingredients_frame.add_items(ingredient)

class IngredientsFrame(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent,fg_color="transparent")
        self.ingredients = []
        self.label = ctk.CTkLabel(self,text="Ingredientes:",text_color=color.TEXT,font=font.text_normal_font())
        self.label.grid(row=0,column=0,padx=(0,5),pady=5,sticky="e")

    def add_items(self,ingredient):
        ingredient_label = ctk.CTkLabel(self,text=f"{ingredient}",fg_color=color.SECONDARY,text_color=color.TEXT_BUTTON,corner_radius=30)
        ingredient_label.grid(row=0,column=len(self.ingredients)+1,padx=5,pady=5,sticky="e")
        self.ingredients.append(ingredient_label)

