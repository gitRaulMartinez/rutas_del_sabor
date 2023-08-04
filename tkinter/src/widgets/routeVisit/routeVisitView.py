import customtkinter as ctk
import tkinter as tk
import src.utils.colors as color
import src.utils.fonts as font

from src.widgets.destinations.listDestinationYScrollFrame import ListDestinationYScrollFrame
from src.services.culinaryDestination import CulinaryDestinationService
from src.services.routeVisit import RouteVisitServices

class RouteVisitView(ctk.CTkToplevel):
    def __init__(self, parent,route_visit):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.route_visit = route_visit
        self.title("Rutas de visita")
        self.position()
        self.load_structure()
        self.load_data()
        self.load_widgets()

    def position(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 700
        window_height = 600
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def load_data(self):
        self.culinary_destination_services = CulinaryDestinationService()
        self.destinations = [destination for destination in self.culinary_destination_services.get_info() if destination._id in self.route_visit.destinations]  
    
    def load_structure(self):
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(2,weight=1)

    def load_widgets(self):
        self.title = ctk.CTkLabel(self,text="Mi ruta",text_color=color.TEXT,font=font.text_hight_bold_font())
        self.title.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

        self.head_list_frame = TitleFrame(self)
        self.head_list_frame.grid(row=1,column=0,padx=(8,10),pady=(10,2),sticky="ew")

        self.list_destinations = ListDestinationYScrollFrame(self)
        self.list_destinations.grid(row=2,column=0,padx=3,pady=2,sticky="nsew")

        for destination in self.destinations:
            self.list_destinations.add_item(destination)

class TitleFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color="transparent",corner_radius=10)
        self.parent = parent
        self.load_structure()
        self.load_widgets()
    
    def load_structure(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)

    def load_widgets(self):
        self.name_label = ctk.CTkLabel(self,text="Destino culinario",text_color=color.TEXT,fg_color="transparent",font=font.text_normal_font(),anchor="w")
        self.name_label.grid(row=0,column=0,padx=(10,2),pady=5,sticky="ew")