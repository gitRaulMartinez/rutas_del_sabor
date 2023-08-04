import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font
import src.utils.date as date

from src.widgets.routeVisit.routeVisitCreate import RouteVisitCreate

class RouteVisitScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent,open_create,open_view):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.open_create = open_create
        self.open_view = open_view
        self.items = []
        self.load_empty()

    def load_empty(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.empty_frame = EmptyFrame(self,self.open_create)
        self.empty_frame.grid(row=0,column=0,padx=0,pady=0,sticky="nsew")
        
    def load_structure(self):
        self.grid_columnconfigure(0,weight=1)

    def add_item(self,route_visit):
        if self.empty_frame.winfo_manager():
            self.empty_frame.grid_forget()
            self.grid_rowconfigure(0,weight=0)

        frame_item = ctk.CTkFrame(self,fg_color=color.NAV,border_width=1,corner_radius=10)
        frame_item.grid(row=len(self.items),column=0, padx=0, pady=5,sticky="ew")
        frame_item.grid_columnconfigure(0,weight=1)

        frame_item.name_label = ctk.CTkLabel(frame_item,text=route_visit.name,fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w")
        frame_item.name_label.grid(row=0,column=0,padx=(10,2),pady=10,sticky="ew")

        frame_item.count_destination_label = ctk.CTkLabel(frame_item,text=f"{len(route_visit.destinations)}",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w",width=250)
        frame_item.count_destination_label.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        frame_item.view_button = ctk.CTkButton(frame_item,text="Ver destinos",height=30,fg_color=color.PRIMARY,text_color=color.TEXT_BUTTON,hover_color=color.HOVER_PRIMARY,font=font.text_small_bold_font(),width=100,command=lambda: self.open_view(route_visit))
        frame_item.view_button.grid(row=0,column=2,padx=(2,10),pady=10,sticky="w")

        self.items.append(frame_item)

    def remove(self):
        for item in self.items:
            item.destroy()

        self.items = []
        self.grid_columnconfigure(0,weight=1)
        self.list_empty.grid(row=0,column=0,sticky="ew")

class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent,command):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.command = command
        self.load_structure()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure((0,2),weight=1)
        self.grid_columnconfigure((0,2),weight=1)
    
    def load_widgets(self):
        self.label_empty = ctk.CTkLabel(self,text="No se encontro ninguna ruta",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font())
        self.label_empty.grid(row=1,column=1,padx=15,pady=15,sticky="ew")
        self.button_empty = ctk.CTkButton(self,text="Crear una nueva ruta",fg_color=color.PRIMARY,text_color=color.TEXT_BUTTON,font=font.text_small_bold_font(),hover_color=color.HOVER_PRIMARY,height=40,width=150,corner_radius=100,command=self.command)
        self.button_empty.grid(row=2,column=1,padx=15,pady=15,sticky="ew")