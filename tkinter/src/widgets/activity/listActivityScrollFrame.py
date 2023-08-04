import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font
import src.utils.date as date

class ActivityScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.items = []
        self.load_fonts()
        self.load_structure()
        self.load_empty()

    def load_fonts(self):
        self.title_font = font.title_font()
        self.text_font = font.text_normal_font()
        self.button_font = font.text_normal_bold_font()

    def load_empty(self):
        self.list_empty = ctk.CTkLabel(self,text="No se encontraron actividades o eventos",fg_color="transparent",text_color=color.TEXT,font=self.text_font)
        self.list_empty.grid(row=0,column=0,sticky="ew")

    def load_structure(self):
        self.grid_columnconfigure(0,weight=1)

    def add_item(self,activity):
        if self.list_empty.winfo_manager():
            self.list_empty.grid_forget()
        
        frame_item = ctk.CTkFrame(self,fg_color=color.NAV,border_width=1,corner_radius=10)
        frame_item.grid(row=len(self.items),column=0, padx=0, pady=5,sticky="ew")
        frame_item.grid_columnconfigure(0,weight=1)

        frame_item.name_label = ctk.CTkLabel(frame_item,text=activity.name,fg_color="transparent",text_color=color.TEXT,font=self.text_font,anchor="w")
        frame_item.name_label.grid(row=0,column=0,padx=(10,2),pady=10,sticky="ew")

        frame_item.start_time_label = ctk.CTkLabel(frame_item,text=date.convert_date_format(activity.start_time),fg_color="transparent",text_color=color.TEXT,font=self.text_font,anchor="w",width=250)
        frame_item.start_time_label.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        frame_item.culinary_destination_label = ctk.CTkLabel(frame_item,text=activity.culinary_destination.name,fg_color="transparent",text_color=color.TEXT,font=self.text_font,anchor="w",width=280)
        frame_item.culinary_destination_label.grid(row=0,column=2,padx=(2,10),pady=10,sticky="w")

        self.items.append(frame_item)

    def remove(self):
        for item in self.items:
            item.destroy()

        self.items = []
        self.grid_columnconfigure(0,weight=1)
        self.list_empty.grid(row=0,column=0,sticky="ew")