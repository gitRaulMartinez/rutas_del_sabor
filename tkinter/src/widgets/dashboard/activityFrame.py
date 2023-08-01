import customtkinter as ctk
import tkinter as tk
import threading

import src.utils.colors as color
import src.utils.fonts as font

from src.services.activity import ActivitiesServices
from src.widgets.activity.listActivityScrollFrame import ActivityScrollFrame
from src.widgets.loadings.loadingSmallFrame import LoadingSmallFrame

class ActivityFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent

        self.load_fonts()
        self.load_data()
        self.load_structure()
        self.load_widgets()

    def load_fonts(self):
        self.title_font = font.title_font()
        self.text_font = font.text_normal_font()

    def load_data(self):
        self.activities_services = ActivitiesServices()
        self.search_name_data = tk.StringVar()
        self.segemented_button_data = ctk.StringVar(value="Hoy")
        self.activities = self.activities_services.filter(date_option="Hoy")

    def load_structure(self):    
        self.rowconfigure(4,weight=1)
        self.columnconfigure(0,weight=1)

    def load_widgets(self):
        self.title_frame = ctk.CTkLabel(self,text="Actividades y eventos",text_color=color.TEXT,fg_color="transparent",font=self.title_font,anchor="w")
        self.title_frame.grid(row=0,column=0,padx=110,pady=15,sticky="ew")

        self.search_frame = SearchActivityFrame(self)
        self.search_frame.grid(row=1,column=0,padx=15,pady=0,sticky="ew")

        self.segmented_button = ctk.CTkSegmentedButton(self,values=["Hoy","Proximos","Pasados","Todos"],variable=self.segemented_button_data,command=self.filter,fg_color=color.BG_LIGHT,selected_color=color.PRIMARY,selected_hover_color=color.HOVER_PRIMARY,unselected_color=color.BG_DARK,unselected_hover_color=color.PRIMARY,height=40,font=font.text_small_bold_font(),corner_radius=50)
        self.segmented_button.grid(row=2,column=0,padx=15,pady=(5,5),sticky="w")

        self.title_list_frame = TitleListFrame(self)
        self.title_list_frame.grid(row=3,column=0,padx=(15,26),pady=(5,5),sticky="ew")

        self.list_activities = ActivityScrollFrame(self)
        self.list_activities.grid(row=4,column=0,padx=(9,10),pady=(5,15),sticky="nsew")

        for activity in self.activities:
            self.list_activities.add_item(activity)

        self.loading_frame = LoadingSmallFrame(self)

    def filter(self,value=None):
        self.activities = self.activities_services.filter(name=self.search_name_data.get(),date_option=self.segemented_button_data.get())
        self.list_activities.remove()
        self.list_activities.grid_forget()
        self.loading_frame.grid(row=4, column=0,sticky="nsew")
        thread = threading.Thread(target=self.list_activities_filter)
        thread.start()

    def list_activities_filter(self):
        for activity in self.activities:
            self.list_activities.add_item(activity)
        self.loading_frame.grid_forget()
        self.list_activities.grid(row=4, column=0,padx=10,pady=(0,15),sticky="nsew")

class SearchActivityFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.load_structure()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure(0,weight=0)
        self.grid_columnconfigure(1,weight=1)

    def load_widgets(self):
        self.search_label = ctk.CTkLabel(self,text="Nombre de actividad: ",text_color=color.TEXT,fg_color="transparent",font=font.text_normal_font())
        self.search_label.grid(row=0,column=0,padx=(0,5),pady=10,sticky="w")

        self.search_entry = ctk.CTkEntry(self,placeholder_text="Ingrese nombre de destino culinario",placeholder_text_color=color.TEXT,textvariable=self.parent.search_name_data,border_width=1)
        self.search_entry.grid(row=0,column=1,padx=5,pady=10,sticky="ew")

        self.search_button = ctk.CTkButton(self,text="Buscar",width=100,fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,command=self.parent.filter)
        self.search_button.grid(row=0,column=2,padx=5,pady=10,sticky="e")

class TitleListFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.NAV,border_width=1,corner_radius=10)
        self.parent = parent
        self.load_structure()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure(0,weight=0)
        self.grid_columnconfigure(0,weight=1)

    def load_widgets(self):
        self.name_label = ctk.CTkLabel(self,text="Nombre de actividad",text_color=color.TEXT,fg_color="transparent",font=font.text_normal_font(),anchor="w")
        self.name_label.grid(row=0,column=0,padx=(10,2),pady=10,sticky="ew")

        self.date_label = ctk.CTkLabel(self,text="Fecha y hora de inicio",text_color=color.TEXT,font=font.text_normal_font(),anchor="w",width=250)
        self.date_label.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        self.culinary_destination_label = ctk.CTkLabel(self,text="Destino culinario",text_color=color.TEXT,font=font.text_normal_font(),anchor="w",width=280)
        self.culinary_destination_label.grid(row=0,column=2,padx=(2,10),pady=10,sticky="w")

    
