import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from PIL import Image
from src.services.google_cloud import get_image
from src.utils.images import get_image_path

class ListDestinationScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent,command=None):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.command = command
        self.items = []
        self.maxcolumn = 4
        self.load_fonts()


    def load_fonts(self):
        self.title_font = font.title_font()
        self.button_font = font.text_normal_bold_fond()

    def add_item(self,culinary_destination):
        frame_item = ctk.CTkFrame(self,width=150, height=200,fg_color=color.NAV,border_width=1,corner_radius=10)
        frame_item.grid(row=len(self.items)//self.maxcolumn,column=len(self.items)%self.maxcolumn, padx=10, pady=15)

        frame_item.logo_image = ctk.CTkImage(Image.open(get_image(culinary_destination.logo)),size=(100,100))
        frame_item.logo_label = ctk.CTkLabel(frame_item,image=frame_item.logo_image, fg_color="white",text="",corner_radius=0,width=100,height=100)
        frame_item.logo_label.grid(row=0,column=0,columnspan=2,padx=10,pady=(10,5))

        frame_item.title_label = ctk.CTkLabel(frame_item,text=culinary_destination.name, fg_color="transparent",width=200,text_color=color.TEXT)
        frame_item.title_label.grid(row=1,column=0,columnspan=2,padx=10,pady=(5,5),sticky="ew")

        frame_item.start_image = ctk.CTkImage(Image.open(get_image_path("start_light.png")),size=(20,20))
        frame_item.popularity_label = ctk.CTkLabel(frame_item,text=": "+str(culinary_destination.popularity), fg_color="transparent",image=frame_item.start_image,compound="left",text_color=color.TEXT)
        frame_item.popularity_label.grid(row=2,column=0,padx=10,pady=(5,5),sticky="w")

        frame_item.location_image = ctk.CTkImage(Image.open(get_image_path("map_light.png")),size=(20,20))
        frame_item.location_label = ctk.CTkLabel(frame_item,text=": "+culinary_destination.location_id.short_country, fg_color="transparent",image=frame_item.location_image,compound="left",text_color=color.TEXT)
        frame_item.location_label.grid(row=2,column=1,padx=10,pady=(5,5),sticky="w")

        frame_item.minimal_price_label = ctk.CTkLabel(frame_item,text="Desde: $ "+str(culinary_destination.minimal_price), fg_color="transparent",text_color=color.TEXT)
        frame_item.minimal_price_label.grid(row=3,column=0,padx=10,pady=(5,5),sticky="w")

        frame_item.maximum_price_label = ctk.CTkLabel(frame_item,text="Hasta: $ "+str(culinary_destination.maximum_price), fg_color="transparent",text_color=color.TEXT)
        frame_item.maximum_price_label.grid(row=3,column=1,padx=10,pady=(5,5),sticky="w")

        frame_item.details_button = ctk.CTkButton(frame_item,text="Mas detalles",command=lambda: self.command(culinary_destination._id),fg_color=color.SECONDARY,border_spacing=5,hover_color=color.HOVER_SECONDARY,font=self.button_font)
        frame_item.details_button.grid(row=4,column=0,columnspan=2,padx=10,pady=(5,10),sticky="ew")

        self.items.append(frame_item)