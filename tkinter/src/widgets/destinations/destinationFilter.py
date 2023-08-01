import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from src.services.culinaryDestination import CulinaryDestinationService

class DestinationFilter(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.load_fonts()
        self.load_data()
        self.position()
        
        self.load_widgets()
        self.grid_columnconfigure((0,1),weight=1)
        self.grid_rowconfigure(15,weight=1)

    def load_fonts(self):
        self.title_font = font.title_font()
        self.text_small_font = font.text_small_font()
        self.text_button = font.button_font()
        self.text_font = font.text_normal_font()

    def load_data(self):
        self.culinary_destination_service = CulinaryDestinationService()
        self.type_of_kitchens = ["Todos"] + [culinary_destination.type_of_kitchen for culinary_destination in self.culinary_destination_service.get_info()]
    
    def position(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 400
        window_height = 550
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def load_widgets(self):
        self.title = ctk.CTkLabel(self,text="Filtros",text_color=color.TEXT,font=self.title_font,height=30,fg_color="transparent")
        self.title.grid(row=0,column=0,padx=10,pady=10,columnspan=2,sticky="ew")

        self.name_label = ctk.CTkLabel(self,text="Nombre:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.name_label.grid(row=1,column=0,padx=10,pady=0,columnspan=2,sticky="w")

        self.name_entry = ctk.CTkEntry(self,textvariable=self.parent.search_name_data,text_color=color.TEXT,border_width=1,height=30)
        self.name_entry.grid(row=2,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.kitchen_label = ctk.CTkLabel(self,text="Tipo de cocina:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.kitchen_label.grid(row=3,column=0,padx=10,pady=0,columnspan=2,sticky="w")

        self.kitchen_entry = ctk.CTkOptionMenu(self,values=self.type_of_kitchens,variable=self.parent.search_kitchen_data,fg_color="white",button_color=color.PRIMARY,button_hover_color=color.HOVER_PRIMARY,dropdown_fg_color="white",dropdown_hover_color=color.HOVER_NAV,text_color=color.TEXT,dropdown_text_color=color.TEXT,font=self.text_font)
        self.kitchen_entry.grid(row=4,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.ingredient_label = ctk.CTkLabel(self,text="Ingrediente:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.ingredient_label.grid(row=5,column=0,padx=10,pady=0,columnspan=2,sticky="w")

        self.ingredient_entry = ctk.CTkEntry(self,textvariable=self.parent.search_ingredient_data,text_color=color.TEXT,border_width=1,height=30,placeholder_text="Ingredients")
        self.ingredient_entry.grid(row=6,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.minimal_price_label = ctk.CTkLabel(self,text="Precio minimo:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.minimal_price_label.grid(row=7,column=0,padx=10,pady=0,sticky="w")

        self.minimal_price_data_label = ctk.CTkLabel(self,textvariable=self.parent.minimal_price_data,text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.minimal_price_data_label.grid(row=7,column=1,padx=10,pady=0,sticky="e")

        self.minimal_price_slider = ctk.CTkSlider(self,variable=self.parent.minimal_price_data,from_=0,to=5000,fg_color=color.BG_LOGIN,progress_color=color.PRIMARY,button_color=color.BG_NAV,button_hover_color=color.HOVER_NAV)
        self.minimal_price_slider.grid(row=8,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.maximum_price_label = ctk.CTkLabel(self,text="Precio maximo:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.maximum_price_label.grid(row=9,column=0,padx=10,pady=0,sticky="w")

        self.maximum_price_data_label = ctk.CTkLabel(self,textvariable=self.parent.maximum_price_data,text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.maximum_price_data_label.grid(row=9,column=1,padx=10,pady=0,sticky="e")

        self.maximum_price_slider = ctk.CTkSlider(self,variable=self.parent.maximum_price_data,from_=0,to=5000,fg_color=color.BG_LOGIN,progress_color=color.PRIMARY,button_color=color.BG_NAV,button_hover_color=color.HOVER_NAV)
        self.maximum_price_slider.grid(row=10,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.minimal_popularity_label = ctk.CTkLabel(self,text="Popularidad minima:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.minimal_popularity_label.grid(row=11,column=0,padx=10,pady=0,sticky="w")

        self.minimal_popularity_data_label = ctk.CTkLabel(self,textvariable=self.parent.minimal_popularity_data,text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.minimal_popularity_data_label.grid(row=11,column=1,padx=10,pady=0,sticky="e")

        self.minimal_popularity_slider = ctk.CTkSlider(self,variable=self.parent.minimal_popularity_data,from_=0,to=5,fg_color=color.BG_LOGIN,progress_color=color.PRIMARY,button_color=color.BG_NAV,button_hover_color=color.HOVER_NAV,number_of_steps=5)
        self.minimal_popularity_slider.grid(row=12,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.maximum_popularity_label = ctk.CTkLabel(self,text="Popularidad maxima:",text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.maximum_popularity_label.grid(row=13,column=0,padx=10,pady=0,sticky="w")

        self.maximum_popularity_data_label = ctk.CTkLabel(self,textvariable=self.parent.maximum_popularity_data,text_color=color.TEXT,font=self.text_font,fg_color="transparent")
        self.maximum_popularity_data_label.grid(row=13,column=1,padx=10,pady=0,sticky="e")

        self.maximum_popularity_slider = ctk.CTkSlider(self,variable=self.parent.maximum_popularity_data,from_=0,to=5,fg_color=color.BG_LOGIN,progress_color=color.PRIMARY,button_color=color.BG_NAV,button_hover_color=color.HOVER_NAV,number_of_steps=5)
        self.maximum_popularity_slider.grid(row=14,column=0,padx=10,pady=(0,10),columnspan=2,sticky="ew")

        self.filter_button = ctk.CTkButton(self,text="Filtrar",fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,font=self.text_button,text_color=color.TEXT_BUTTON,height=30,command=self.parent.filter)
        self.filter_button.grid(row=15,column=0,columnspan=2,padx=10,pady=15,sticky="ews")