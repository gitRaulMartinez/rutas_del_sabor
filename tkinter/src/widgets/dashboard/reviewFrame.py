import customtkinter as ctk
import threading

import src.utils.colors as color
import src.utils.fonts as font

from src.services.review import ReviewServices
from src.widgets.review.reviewScrollFrame import ReviewScrollFrame
from src.widgets.review.reviewCreate import ReviewCreate
from src.widgets.loadings.loadingSmallFrame import LoadingSmallFrame

class ReviewFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.load_structure()
        self.load_data()
        self.load_widgets()
    
    def load_structure(self):
        self.grid_rowconfigure(1,weight=1)
        self.grid_columnconfigure((0,1),weight=1)

    def load_data(self):
        self.review_services = ReviewServices()
        self.my_reviews = self.review_services.get_my_reviews()

    def load_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="Mis reviews",text_color=color.TEXT,font=font.text_ultra_bold_font(),anchor="w")
        self.title_label.grid(row=0,column=0,padx=10,pady=20,sticky="w")

        self.create_review_button = ctk.CTkButton(self,text="Crear review",fg_color=color.SECONDARY,hover_color=color.HOVER_SECONDARY,font=font.text_small_bold_font(),border_spacing=5,command=self.create_review,text_color=color.TEXT_BUTTON,corner_radius=100)
        self.create_review_button.grid(row=0,column=1,padx=10,pady=20,sticky="e")

        self.list_reviews_frame = ReviewScrollFrame(self)
        self.list_reviews_frame.grid(row=1,column=0,padx=(10,2),pady=10,columnspan=2,sticky="nsew")

        for review in self.my_reviews:
            self.list_reviews_frame.add_item(review)

        self.loading_frame = LoadingSmallFrame(self)

    def create_review(self):
        self.view_route_toplevel = ReviewCreate(self)
        self.view_route_toplevel.grab_set()

    def submit_review(self,data):
        self.list_reviews_frame.grid_forget()
        self.loading_frame.grid(row=1,column=0,padx=(10,2),pady=10,columnspan=2,sticky="nsew")
        thread = threading.Thread(target=lambda: self.new_review(data))
        thread.start()

    def new_review(self,data):
        new_review = self.review_services.create(data)
        self.loading_frame.grid_forget()
        self.list_reviews_frame.grid(row=1,column=0,padx=(10,2),pady=10,columnspan=2,sticky="nsew")
        self.list_reviews_frame.add_item(new_review)
