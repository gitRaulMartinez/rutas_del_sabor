import customtkinter as ctk
import tkinter as tk
import threading

import src.utils.colors as color
import src.utils.fonts as font

import src.utils.form_control as form_control

from src.services.culinaryDestination import CulinaryDestinationService
from src.widgets.destinations.listDestinationYScrollFrame import ListDestinationYScrollFrame
from src.widgets.loadings.loadingSmallFrame import LoadingSmallFrame

class ListDesinationMap(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.title("Destinos")
        self.position()
        self.load_structure()
        self.load_data()
        self.load_widgets()

    def position(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 700
        window_height = 500
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    
    def load_structure(self):
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

    def load_data(self):
        self.destination_services = CulinaryDestinationService()
        self.destinations = self.destination_services.get_info()

    def load_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="Destinos culinarios",text_color=color.TEXT,font=font.text_normal_bold_font(),fg_color="transparent")
        self.title_label.grid(row=0,column=0,padx=5,pady=5,sticky="ew")

        self.loading_frame = LoadingSmallFrame(self)
        self.list_destinations_frame = ListDestinationYScrollFrame(self,action="map")
        self.list_destinations_frame.grid(row=1,column=0,padx=5,pady=5,sticky="nsew")

        for destination in self.destinations:
            self.list_destinations_frame.add_item(destination)

    def location(self,destination):
        [x,y] = destination.location_id.coordinates
        self.parent.set_zoom_map(15,x,y)
        self.destroy()