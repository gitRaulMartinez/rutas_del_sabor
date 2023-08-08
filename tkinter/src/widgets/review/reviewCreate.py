import customtkinter as ctk
import tkinter as tk

import src.utils.colors as color
import src.utils.fonts as font

import src.utils.form_control as form_control

from src.services.routeVisit import RouteVisitServices
from src.services.review import ReviewServices
from src.widgets.destinations.listDestinationYScrollFrame import ListDestinationYScrollFrame

class ReviewCreate(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.select_destination = None
        self.title("Reviews")
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
        self.route_visit_services = RouteVisitServices()
        self.destinations_visited = self.route_visit_services.destinations_visited()

        self.review_services = ReviewServices()
        self.my_reviews = self.review_services.get_my_reviews()

        self.destinations_not_review = []

        for destination in self.destinations_visited:
            band = False
            for review in self.my_reviews:
                if review.culinary_destination_id == destination._id:
                    band = True
                    break
            if not band:    
                self.destinations_not_review.append(destination)
    
    def load_structure(self):
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def load_widgets(self):
        self.list_destinations = DestinationsVisitedFrame(self)
        self.list_destinations.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

        self.create_review_frame = CreateReviewFrame(self)

    def open_create_frame(self,destination_id):
        self.list_destinations.grid_forget()
        self.select_destination = destination_id
        self.create_review_frame.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

    def submit_review(self,data):
        self.parent.submit_review(data)
        self.destroy()

class DestinationsVisitedFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.load_structure()
        self.load_widgets()
    
    def load_structure(self):
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure(0,weight=1)

    def load_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="Destinos visitados",text_color=color.TEXT,font=font.text_hight_bold_font(),fg_color="transparent")
        self.title_label.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

        self.list_destinations_visited_frame = ListDestinationYScrollFrame(self,action="review")
        self.list_destinations_visited_frame.grid(row=1,column=0,padx=10,pady=10,sticky="nsew")

        for destination in self.parent.destinations_not_review:
            self.list_destinations_visited_frame.add_item(destination)

    def open_create(self,destination_id):
        self.parent.open_create_frame(destination_id)

class CreateReviewFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent

        self.load_structure()
        self.load_data()
        self.load_widgets()

    def load_data(self):
        self.score = tk.IntVar()
        self.animo = tk.StringVar()
    
    def load_structure(self):
        self.grid_rowconfigure(6,weight=1)
        self.grid_columnconfigure(0,weight=1)
    
    def load_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="Crear review",text_color=color.TEXT,font=font.text_hight_bold_font(),fg_color="transparent")
        self.title_label.grid(row=0,column=0,padx=10,pady=3,sticky="ew")

        self.score_label = ctk.CTkLabel(self,text="Puntaje: ",text_color=color.TEXT,font=font.text_normal_font(),fg_color="transparent")
        self.score_label.grid(row=1,column=0,padx=10,pady=0,sticky="w")

        self.score_options = ctk.CTkFrame(self,fg_color="transparent")
        self.score_options.radio_buttons = []
        self.score_options.grid(row=2,column=0,padx=10,pady=(0,10),sticky="ew")
        self.score_options.grid_columnconfigure((0,1,2,3,4),weight=1)
        for i in range(5):
            radio_button = ctk.CTkRadioButton(self.score_options,text=f"{i+1}",variable=self.score,value=i+1,border_color=color.TEXT,border_width_checked=5,hover_color=color.PRIMARY,border_width_unchecked=3)
            radio_button.grid(row=0,column=i,padx=2,pady=2,sticky="ew")
            self.score_options.radio_buttons.append(radio_button)

        self.animo_label = ctk.CTkLabel(self,text="¿ Recomienda este lugar ?: ",text_color=color.TEXT,font=font.text_normal_font(),fg_color="transparent")
        self.animo_label.grid(row=3,column=0,padx=10,pady=0,sticky="w")

        self.animo_options = ctk.CTkFrame(self,fg_color="transparent")
        self.animo_options.radio_buttons = []
        self.animo_options.grid(row=4,column=0,padx=10,pady=(0,10),sticky="ew")
        self.animo_options.grid_columnconfigure((0,1),weight=1)
        radio_button = ctk.CTkRadioButton(self.animo_options,text="Si",variable=self.animo,value="positive",border_color=color.TEXT,border_width_checked=5,hover_color=color.PRIMARY,border_width_unchecked=3)
        radio_button.grid(row=0,column=0,padx=2,pady=2,sticky="w")
        radio_button = ctk.CTkRadioButton(self.animo_options,text="No",variable=self.animo,value="negative",border_color=color.TEXT,border_width_checked=5,hover_color=color.PRIMARY,border_width_unchecked=3)
        radio_button.grid(row=0,column=1,padx=2,pady=2,sticky="w")
        self.animo_options.radio_buttons.append(radio_button)

        self.comment_label = ctk.CTkLabel(self,text="Dejanos un comentario: ",text_color=color.TEXT,font=font.text_normal_font(),fg_color="transparent")
        self.comment_label.grid(row=5,column=0,padx=10,pady=0,sticky="w")

        self.comment_text = ctk.CTkTextbox(self,border_width=1,fg_color="white",text_color=color.TEXT,font=font.text_normal_font())
        self.comment_text.grid(row=6,column=0,padx=10,pady=0,sticky="nsew")

        self.error_label = ctk.CTkLabel(self,text="",text_color="red",font=font.text_normal_font(),fg_color="transparent")
        self.error_label.grid(row=7,column=0,padx=10,pady=(5,2),sticky="w")

        self.create_button = ctk.CTkButton(self,text="Crear review",fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,font=font.text_small_bold_font(),text_color=color.TEXT_BUTTON,command=self.submit,height=40)
        self.create_button.grid(row=8,column=0,padx=10,pady=10,sticky="nsew")
    
    def submit(self):
        if self.control():
            self.error_label.configure(text="")
            data = {
                'score': self.score.get(),
                'animo': self.animo.get(),
                'comment': self.comment_text.get("0.0", "end"),
                'culinary_destination_id': self.parent.select_destination
            }
            self.parent.submit_review(data=data)

    def control(self):
        if(self.score.get() == ""):
            self.error_label.configure(text="* Selecciona una opción de puntaje")
            return False
        elif(self.animo.get() == ""):
            self.error_label.configure(text="* Selecciona una opción de recomendación")
            return False
        elif(self.comment_text.get("0.0", "end") == ""):
            self.error_label.configure(text="* Añade algunas palabras en el cuadro de comentarios")
            return False
        return True
