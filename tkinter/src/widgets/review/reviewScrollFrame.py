import customtkinter as ctk

import src.utils.colors as color
import src.utils.fonts as font

from PIL import Image
from src.utils.images import get_image_path

class ReviewScrollFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.items = []
        self.load_empty()

    def load_empty(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.empty_frame = EmptyFrame(self)
        self.empty_frame.grid(row=0,column=0,padx=0,pady=0,sticky="nsew")
        
    def load_structure(self):
        self.grid_columnconfigure(0,weight=1)

    def add_item(self,review):
        if self.empty_frame.winfo_manager():
            self.empty_frame.grid_forget()
            self.grid_rowconfigure(0,weight=0)

        frame_item = ctk.CTkFrame(self,fg_color=color.NAV,border_width=1,corner_radius=10)
        frame_item.grid(row=len(self.items),column=0, padx=0, pady=5,sticky="ew")
        frame_item.grid_rowconfigure(2,weight=1)
        frame_item.grid_columnconfigure((0,1),weight=1)

        frame_item.user_label = ctk.CTkLabel(frame_item,text=f"Usuario: {review.user.username}",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w")
        frame_item.user_label.grid(row=0,column=0,padx=10,pady=(10,3),sticky="w")

        frame_item.destination_label = ctk.CTkLabel(frame_item,text=f"Destino culinario: {review.destination.name}",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w")
        frame_item.destination_label.grid(row=0,column=1,padx=10,pady=(10,3),sticky="e")

        frame_item.score_frame = ScoreFrame(frame_item,review.score)
        frame_item.score_frame.grid(row=1,column=0,padx=10,pady=3,sticky="w")

        frame_item.animo_image = ctk.CTkImage(Image.open(get_image_path("positive.png")),size=(20,20)) if review.animo == 'positive' else ctk.CTkImage(Image.open(get_image_path("negative.png")),size=(20,20))
        frame_item.animo_label = ctk.CTkLabel(frame_item,image=frame_item.animo_image,text="")
        frame_item.animo_label.grid(row=1,column=1,padx=10,pady=3,sticky="e")

        frame_item.comment_label = ctk.CTkLabel(frame_item,text="Comentario:",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w")
        frame_item.comment_label.grid(row=2,column=0,padx=10,pady=3,columnspan=2,sticky="w")

        frame_item.comment_text = ctk.CTkLabel(frame_item,text=f"{review.comment}",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w")
        frame_item.comment_text.grid(row=3,column=0,padx=10,pady=(3,10),columnspan=2,sticky="ew")

        self.items.append(frame_item)

    def remove(self):
        for item in self.items:
            item.destroy()

        self.items = []
        self.grid_columnconfigure(0,weight=1)
        self.list_empty.grid(row=0,column=0,sticky="ew")

class EmptyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.load_structure()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure((0,2),weight=1)
        self.grid_columnconfigure((0,2),weight=1)
    
    def load_widgets(self):
        self.label_empty = ctk.CTkLabel(self,text="No se encontro ningun review",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font())
        self.label_empty.grid(row=1,column=1,padx=15,pady=15,sticky="ew")

class ScoreFrame(ctk.CTkFrame):
    def __init__(self, parent, score):
        super().__init__(parent,fg_color="transparent")
        self.score = score

        self.load_widgets()

    def load_widgets(self):
        self.score_label = ctk.CTkLabel(self,text="Calificación:",fg_color="transparent",text_color=color.TEXT,font=font.text_normal_font(),anchor="w")
        self.score_label.grid(row=0,column=0,padx=0,pady=5,sticky="w")

        self.start_image = ctk.CTkImage(Image.open(get_image_path("start.png")),size=(15,15))
        self.starts_labels = []
        for i in range(self.score):
            start_label = ctk.CTkLabel(self,text="",fg_color="transparent",anchor="w",image=self.start_image)
            start_label.grid(row=0,column=i+1,padx=3,pady=5,sticky="w")
            self.starts_labels.append(start_label)