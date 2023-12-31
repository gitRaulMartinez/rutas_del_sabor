import customtkinter as ctk
import threading

import src.utils.colors as color

from src.widgets.nav.navFrame import NavFrame
from src.widgets.dashboard.homeFrame import HomeFrame
from src.widgets.dashboard.activityFrame import ActivityFrame
from src.widgets.dashboard.planningFrame import PlanningFrame
from src.widgets.dashboard.reviewFrame import ReviewFrame
from src.widgets.dashboard.mapFrame import MapFrame

from src.widgets.loadings.loadingFrame import LoadingFrame

from src.services.users import UserService

from src.utils.images import get_image_path

class Dashboard(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        self.head()
        self.position()
        self.structure_loading()
        self.body()

        self.protocol("WM_DELETE_WINDOW", self.close_window)
        self.user_services = UserService()
    
    def head(self):
        self.title("Rutas del sabor")
        self.iconbitmap(get_image_path("logo.ico"))

    def position(self):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición para colocar la ventana en el centro
        window_width = 1200
        window_height = 700
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Colocar la ventana en el centro de la pantalla
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def structure_loading(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def structure(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def close_window(self):
        self.parent.destroy()

    def body(self):
        self.loading_frame = LoadingFrame(self)
        self.loading_frame.grid(row=0, column=0, sticky="nswe")
        thread = threading.Thread(target=self.load_nav)
        thread.start()

    def load_nav(self):
        self.nav_frame = NavFrame(self)   
        self.loading_frame.label_title.configure(text="Cargando Destinos...")
        thread = threading.Thread(target=self.load_home)
        thread.start()

    def load_home(self):
        self.home_frame = HomeFrame(self)
        self.loading_frame.label_title.configure(text="Cargando Actividades...")
        thread = threading.Thread(target=self.load_activity)
        thread.start()

    def load_activity(self):
        self.activity_frame = ActivityFrame(self)
        self.loading_frame.label_title.configure(text="Cargando Rutas...")
        thread = threading.Thread(target=self.load_planning)
        thread.start()

    def load_planning(self):
        self.planning_frame = PlanningFrame(self)
        self.loading_frame.label_title.configure(text="Cargando Reviews...")
        thread = threading.Thread(target=self.load_review)
        thread.start()

    def load_review(self):
        self.review_frame = ReviewFrame(self)
        self.loading_frame.label_title.configure(text="Cargando Mapa...")
        thread = threading.Thread(target=self.load_map)
        thread.start()

    def load_map(self):
        self.map_frame = MapFrame(self)
        self.loading_frame.grid_forget()
        self.structure()
        self.nav_frame.grid(row=0, column=0, padx=0, pady=0, sticky="sn")
        self.home_frame.grid(row=0, column=1, padx=0, pady=0, sticky="snew")

    def logout(self):
        self.user_services.logout()
        self.parent.show_window()

    def switch_frame(self, frame):
        if frame == "home":
            self.home_frame.grid(row=0, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.home_frame.grid_forget()
        if frame == "activity":
            self.activity_frame.grid(row=0, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.activity_frame.grid_forget()
        if frame == "planning":
            self.planning_frame.grid(row=0, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.planning_frame.grid_forget()
        if frame == "review":
            self.review_frame.grid(row=0, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.review_frame.grid_forget()
        if frame == "map":
            self.map_frame.grid(row=0, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.map_frame.grid_forget()

        