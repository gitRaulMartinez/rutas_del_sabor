import customtkinter as ctk
import tkinter as tk
import src.utils.colors as color
import src.utils.fonts as font
import src.utils.form_control as form_control

from src.widgets.destinations.listDestinationYScrollFrame import ListDestinationYScrollFrame
from src.services.culinaryDestination import CulinaryDestinationService

class RouteVisitCreate(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
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
        self.destinations_services = CulinaryDestinationService()
        self.destinations = self.destinations_services.get_info()
        self.required_text = tk.StringVar(value="")
        self.list_destinations_data = []
    
    def load_structure(self):
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(4,weight=1)

    def load_widgets(self):
        self.title = ctk.CTkLabel(self,text="Creacion de rutas",text_color=color.TEXT,font=font.text_hight_bold_font())
        self.title.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

        self.name_label = ctk.CTkLabel(self,text="Nombre:",text_color=color.TEXT,font=font.text_small_font(),fg_color="transparent",anchor="w")
        self.name_label.grid(row=1,column=0,padx=10,pady=2,sticky="ew")

        self.name_entry = ctk.CTkEntry(self,placeholder_text="Ingresar nombre de la ruta",font=font.text_small_font(),text_color=color.TEXT,border_width=1,fg_color="white",height=40)
        self.name_entry.grid(row=2,column=0,padx=10,pady=2,sticky="ew")

        self.head_list_frame = TitleFrame(self)
        self.head_list_frame.grid(row=3,column=0,padx=(8,10),pady=(10,2),sticky="ew")

        self.list_destinations = ListDestinationYScrollFrame(self,action="create")
        self.list_destinations.grid(row=4,column=0,padx=3,pady=2,sticky="nsew")

        for destination in self.destinations:
            self.list_destinations.add_item(destination)
        
        self.required_label = ctk.CTkLabel(self,textvariable=self.required_text,font=font.text_small_font(),text_color="red")
        self.required_label.grid(row=5,column=0,padx=10,pady=2,sticky="ew")
        
        self.create_routes_button = ctk.CTkButton(self,text="Crear ruta",fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,height=40,command=self.create_route_destinations,font=font.text_small_bold_font(),text_color=color.TEXT_BUTTON)
        self.create_routes_button.grid(row=6,column=0,padx=10,pady=(5,10),sticky="ew")


    def create_route_destinations(self):
        if self.control(self.name_entry.get(),self.list_destinations.items):
            self.list_destinations_data = []
            for item in self.list_destinations.items:
                if item.check_button.get() == 1:
                    self.list_destinations_data.append(item.data)
            self.parent.create_route(name=self.name_entry.get(),list_destinations=self.list_destinations_data)
            self.destroy()

    def control(self,value,list):
        if len(value) == 0:
            self.required_text.set("* Campo nommbre obligatorio")
            return False
        elif form_control.control_name_route(value):
            self.required_text.set("* Solo se permiten letras, numeros y espacios")
            return False
        elif form_control.control_min_len(value):
            self.required_text.set("* Minimo 4 caracteres")
            return False
        elif form_control.control_max_len(value):
            self.required_text.set("* Maximo 20 caracteres")
            return False
        else:
            for item in list:
                if item.check_button.get() == 1:
                    return True
            self.required_text.set("* No selecciono ningun destino")
            return False

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

        self.culinary_destination_label = ctk.CTkLabel(self,text="Acciones",text_color=color.TEXT,font=font.text_normal_font(),anchor="w",width=100)
        self.culinary_destination_label.grid(row=0,column=2,padx=(2,10),pady=5,sticky="w")


        