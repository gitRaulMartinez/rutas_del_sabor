import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from PIL import Image
from src.services.google_cloud import get_image
from src.utils.images import get_image_path

class ListDestinationYScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent,action=None):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.action = action
        self.items = []
        self.load_empty()

    def load_empty(self):
        self.grid_columnconfigure(0,weight=1)
        self.list_empty = ctk.CTkLabel(self,height=100,text="No se encontraron destinos culinarios",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font())
        self.list_empty.grid(row=0,column=0,sticky="ew")

    def add_item(self,culinary_destination):
        if self.list_empty.winfo_manager():
            self.list_empty.grid_forget()

        frame_item = ctk.CTkFrame(self,width=150, height=200,fg_color="white",border_width=1,corner_radius=10)
        frame_item.grid(row=len(self.items),column=0, padx=0, pady=5,sticky="ew")
        frame_item.grid_rowconfigure(0,weight=1)
        frame_item.grid_columnconfigure(3,weight=1)

        frame_item.logo_image = ctk.CTkImage(Image.open(get_image(culinary_destination.logo)),size=(50,50))
        frame_item.logo_label = ctk.CTkLabel(frame_item,image=frame_item.logo_image, fg_color="white",text="",corner_radius=0,width=50,height=50)
        frame_item.logo_label.grid(row=0,column=0,rowspan=2,padx=10,pady=(10,5),sticky="w")

        frame_item.title_label = ctk.CTkLabel(frame_item,text=culinary_destination.name, fg_color="transparent",width=200,text_color=color.TEXT,font=font.text_small_bold_font(),anchor="w")
        frame_item.title_label.grid(row=0,column=1,padx=10,pady=(5,5),sticky="w")

        frame_item.location_image = ctk.CTkImage(Image.open(get_image_path("map.png")),size=(20,20))
        frame_item.location_label = ctk.CTkLabel(frame_item,text=f": {culinary_destination.location_id.country}", fg_color="transparent",image=frame_item.location_image,compound="left",text_color=color.TEXT,font=font.text_small_font())
        frame_item.location_label.grid(row=1,column=1,padx=10,pady=(5,5),sticky="w")

        frame_item.price_label = ctk.CTkLabel(frame_item,text=f"Desde: $ {culinary_destination.minimal_price} Hasta: $ {culinary_destination.maximum_price}", fg_color="transparent",text_color=color.TEXT,font=font.text_small_font())
        frame_item.price_label.grid(row=0,column=2,padx=10,pady=(5,5),sticky="w")

        frame_item.popularity_image = ctk.CTkImage(Image.open(get_image_path("start.png")),size=(20,20))
        frame_item.popularity_label = ctk.CTkLabel(frame_item,text=f": {culinary_destination.popularity}", fg_color="transparent",text_color=color.TEXT,image=frame_item.location_image,compound="left")
        frame_item.popularity_label.grid(row=1,column=2,padx=10,pady=(5,5),sticky="w")

        if self.action == "create":
            frame_item.check_button = ctk.CTkCheckBox(frame_item,border_color=color.PRIMARY,border_width=2,fg_color=color.PRIMARY,hover_color=color.HOVER_NAV,text="Agregar",text_color=color.TEXT,font=font.text_small_font())
            frame_item.check_button.grid(row=0,column=3,rowspan=2,padx=10,pady=(5,10),sticky="e")
            frame_item.data = culinary_destination._id
        elif self.action == "review":
            frame_item.check_button = ctk.CTkButton(frame_item,fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,text="Hacer review",text_color=color.TEXT_BUTTON,font=font.text_small_bold_font(),height=40,command=lambda: self.parent.open_create(culinary_destination._id))
            frame_item.check_button.grid(row=0,column=3,rowspan=2,padx=10,pady=(5,10),sticky="e")

        self.items.append(frame_item)

    def remove(self):
        for item in self.items:
            item.destroy()

        self.items = []
        self.grid_columnconfigure(0,weight=1)
        self.list_empty.grid(row=0,column=0,sticky="ew")