import customtkinter as ctk
import tkinter as tk
import threading

import src.utils.colors as color
import src.utils.fonts as font

from PIL import Image
from src.utils.images import get_image_path

from src.services.culinaryDestination import CulinaryDestinationService
from src.widgets.destinations.listDestinationScrollFrame import ListDestinationScrollFrame
from src.widgets.destinations.destinationFrame import DestinationFrame
from src.widgets.destinations.destinationFilter import DestinationFilter
from src.widgets.loadings.loadingSmallFrame import LoadingSmallFrame

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
        self.search_name_data = tk.StringVar()
        self.search_kitchen_data = tk.StringVar()
        self.search_kitchen_data.set("Todos")
        self.search_ingredient_data = tk.StringVar()
        self.minimal_price_data = tk.IntVar()
        self.minimal_price_data.set(0)
        self.maximum_price_data = tk.IntVar()
        self.maximum_price_data.set(5000)
        self.minimal_popularity_data = tk.IntVar()
        self.minimal_popularity_data.set(0)
        self.maximum_popularity_data = tk.IntVar()
        self.maximum_popularity_data.set(5)

    def load_fonts(self):
        self.title_font = font.title_font()
        self.name_font = font.text_small_font()

    def load_structure(self):
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def load_widgets(self):
        self.search_frame = SearchFrame(self)
        self.search_frame.grid(row=0,column=0,padx=15,pady=(20,0),sticky="new")
        self.list_destinations = ListDestinationScrollFrame(self,self.show_destination)
        self.list_destinations.grid(row=1, column=0, sticky="nsew")
        for culinary_destination in self.culinary_destinations:
            self.list_destinations.add_item(culinary_destination)

        self.loading_frame = LoadingSmallFrame(self)
        self.destination_frame = DestinationFrame(self)

    def list_culinary_destinations_filter(self):
        for culinary_destination in self.culinary_destinations:
            self.list_destinations.add_item(culinary_destination)
        self.loading_frame.grid_forget()
        self.list_destinations.grid(row=1, column=0, sticky="nsew")

    def show_destination(self,culinary_destination_id):
        self.list_destinations.grid_forget()
        self.search_frame.grid_forget()
        self.loading_frame.grid(row=0, column=0,rowspan=2,sticky="nsew")
        self.destination_frame.destroy()
        thread = threading.Thread(target=lambda: self.load_destination(culinary_destination_id))
        thread.start()

    def load_destination(self,culinary_destination_id):
        self.destination_frame = DestinationFrame(self,culinary_destination_id,self.show_list)
        self.loading_frame.grid_forget()
        self.destination_frame.grid(row=1, column=0, sticky="nsew")

    def show_list(self):
        self.destination_frame.grid_forget()
        self.search_frame.grid(row=0,column=0,padx=15,pady=(20,0),sticky="new")
        self.list_destinations.grid(row=1, column=0, sticky="nsew")

    def search_name(self):
        self.culinary_destinations = self.culinary_destinations_services.filter(name=self.search_name_data.get())
        self.list_destinations.remove()
        self.list_destinations.grid_forget()
        self.loading_frame.grid(row=1, column=0,sticky="nsew")
        thread = threading.Thread(target=self.list_culinary_destinations_filter)
        thread.start()

    def open_filter(self):
        self.destination_filter = DestinationFilter(self)
        self.destination_filter.grab_set()

    def filter(self):
        self.destination_filter.destroy()
        self.culinary_destinations = self.culinary_destinations_services.filter(name=self.search_name_data.get(),ingredient=self.search_ingredient_data.get(),kitchen=self.search_kitchen_data.get(),minimal_price=self.minimal_price_data.get(),maximun_price=self.maximum_price_data.get(),minimal_popularity=self.minimal_popularity_data.get(),maximum_popularity=self.maximum_popularity_data.get())
        self.list_destinations.remove()
        self.list_destinations.grid_forget()
        self.loading_frame.grid(row=1, column=0,sticky="nsew")
        thread = threading.Thread(target=self.list_culinary_destinations_filter)
        thread.start()

class SearchFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent

        self.load_fonts()
        self.load_structure()
        self.load_widgets()

    def load_fonts(self):
        self.title_font = font.title_font()
        self.name_font = font.text_small_font()

    def load_structure(self):
        self.grid_rowconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)

    def load_widgets(self):
        self.search_label = ctk.CTkLabel(self,text="Buscar:",text_color=color.TEXT,fg_color="transparent",font=self.name_font)
        self.search_label.grid(row=0,column=0,padx=(0,5),pady=10,sticky="w")

        self.search_entry = ctk.CTkEntry(self,placeholder_text="Ingrese nombre de destino culinario",placeholder_text_color=color.TEXT,textvariable=self.parent.search_name_data,border_width=1)
        self.search_entry.grid(row=0,column=1,padx=5,pady=10,sticky="ew")

        self.search_button = ctk.CTkButton(self,text="Buscar",width=100,font=self.name_font,fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,command=self.parent.search_name)
        self.search_button.grid(row=0,column=2,padx=5,pady=10,sticky="e")

        self.search_filter_image = ctk.CTkImage(Image.open(get_image_path('filter_light.png')),size=(20,20))
        self.open_button = ctk.CTkButton(self,text="",width=30,font=self.name_font,fg_color=color.SECONDARY,hover_color=color.HOVER_SECONDARY,image=self.search_filter_image,compound="left",command=self.parent.open_filter)
        self.open_button.grid(row=0,column=3,padx=5,pady=10,sticky="e")

