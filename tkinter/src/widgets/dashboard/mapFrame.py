import customtkinter as ctk
import tkintermapview
import threading
import time

import src.utils.colors as color
import src.utils.fonts as font

from src.services.culinaryDestination import CulinaryDestinationService
from src.widgets.map.listDestinationMap import ListDesinationMap

class MapFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent

        self.load_structure()
        self.load_data()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure((0),weight=1)

    def load_data(self):
        self.destinations_services = CulinaryDestinationService()
        self.destinations = self.destinations_services.get_info()

    def load_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="Mapa de destinos culinarios",text_color=color.TEXT,font=font.text_hight_bold_font(),fg_color="transparent")
        self.title_label.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        self.back_button = ctk.CTkButton(self,text="Ver mapa completo",text_color=color.TEXT_BUTTON,font=font.text_small_bold_font(),fg_color=color.SECONDARY,hover_color=color.HOVER_SECONDARY,height=30,command=lambda: self.set_zoom_map(2,0,0))
        self.back_button.grid(row=0,column=1,padx=5,pady=10,sticky="e")

        self.back_button = ctk.CTkButton(self,text="Ver Destinos",text_color=color.TEXT_BUTTON,font=font.text_small_bold_font(),fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,height=30,command=self.open_list_destinations)
        self.back_button.grid(row=0,column=2,padx=5,pady=10,sticky="e")

        self.map_view = tkintermapview.TkinterMapView(self,corner_radius=0)
        self.map_view.grid(row=1,column=0,columnspan=3,sticky="nsew")

        self.map_view.set_position(0,0)
        self.map_view.set_zoom(2)

        self.markers = []

        for destination in self.destinations:
            [x,y] = destination.location_id.coordinates
            marker = self.map_view.set_marker(x,y,text=destination.name,command=self.click_marker)
            self.markers.append(marker)

    def click_marker(self,event):
        (x,y) = event.position
        thread = threading.Thread(target=lambda: self.set_zoom_map(15,x,y))
        thread.start()
    
    def set_zoom_map(self,zoom,x,y):
        self.map_view.set_zoom(zoom)
        self.map_view.set_position(x,y)

    def open_list_destinations(self):
        self.list_destination_map_toplevel = ListDesinationMap(self)
        self.list_destination_map_toplevel.grab_set()