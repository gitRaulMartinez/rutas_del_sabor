import customtkinter as ctk

from src.widgets.nav.navFrame import NavFrame
from src.widgets.head.headFrame import HeadFrame
from src.widgets.dashboard.homeFrame import HomeFrame
from src.widgets.dashboard.activityFrame import ActivityFrame
from src.widgets.dashboard.planningFrame import PlanningFrame
from src.widgets.dashboard.mapFrame import MapFrame

class Dashboard(ctk.CTkToplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        self.head()
        self.position()
        self.structure()
        self.body()

        self.protocol("WM_DELETE_WINDOW", self.close_window)
    
    def head(self):
        self.title("Rutas del sabor")

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

    def structure(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

    def close_window(self):
        self.parent.destroy()

    def body(self):
        self.nav_frame = NavFrame(self)    
        self.head_frame = HeadFrame(self)

        self.home_frame = HomeFrame(self)       
        self.activity_frame = ActivityFrame(self)
        self.planning_frame = PlanningFrame(self)
        self.map_frame = MapFrame(self)

        self.nav_frame.grid(row=0, column=0, rowspan=2, padx=0, pady=0, sticky="sn")
        self.head_frame.grid(row=0, column=1, padx=0, pady=0, sticky="ew")
        self.home_frame.grid(row=1, column=1, padx=0, pady=0, sticky="snew")

    def logout(self):
        self.parent.show_window()

    def switch_frame(self, frame):
        if frame == "home":
            self.home_frame.grid(row=1, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.home_frame.grid_forget()
        if frame == "activity":
            self.activity_frame.grid(row=1, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.activity_frame.grid_forget()
        if frame == "planning":
            self.planning_frame.grid(row=1, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.planning_frame.grid_forget()
        if frame == "map":
            self.map_frame.grid(row=1, column=1, padx=0, pady=0, sticky="snew")
        else:
            self.map_frame.grid_forget()

        