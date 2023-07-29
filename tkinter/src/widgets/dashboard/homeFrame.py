import customtkinter as ctk
import threading

import src.utils.colors as color
import src.utils.fonts as font

from src.services.culinaryDestination import CulinaryDestinationService
from src.widgets.destinations.listDestinationScrollFrame import ListDestinationScrollFrame
from src.widgets.destinations.destinationFrame import DestinationFrame
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

    def load_fonts(self):
        self.title_font = font.title_font()
        self.name_font = font.text_small_font()

    def load_structure(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def load_widgets(self):
        self.list_destinations = ListDestinationScrollFrame(self,self.show_destination)
        self.list_destinations.grid(row=0, column=0, sticky="nsew")

        for culinary_destination in self.culinary_destinations:
            self.list_destinations.add_item(culinary_destination)

        self.loading_frame = LoadingSmallFrame(self)
        self.destination_frame = DestinationFrame(self)

    def show_destination(self,culinary_destination_id):
        self.list_destinations.grid_forget()
        self.loading_frame.grid(row=0, column=0, sticky="nsew")
        thread = threading.Thread(target=lambda: self.load_destination(culinary_destination_id))
        thread.start()

    def load_destination(self,culinary_destination_id):
        self.destination_frame.destroy()
        self.destination_frame = DestinationFrame(self,culinary_destination_id,self.show_list)
        self.loading_frame.grid_forget()
        self.destination_frame.grid(row=0, column=0, sticky="nsew")

    def show_list(self):
        self.destination_frame.grid_forget()
        self.list_destinations.grid(row=0, column=0, sticky="nsew")






