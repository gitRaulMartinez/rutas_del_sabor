import customtkinter as ctk
import tkinter as tk

from src.widgets.login.loginFrame import LoginFrame
from src.widgets.login.registerFrame import RegisterFrame
from src.widgets.notifications.notification import Notification

import src.utils.session as session

from src.views.dashboard import Dashboard

from PIL import Image
from src.utils.images import get_image_path

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.load_fonts()
        self.load_bg()
        self.head()
        self.position()
        self.structure()

        self.login_frame = LoginFrame(self)
        self.login_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

        self.register_frame = RegisterFrame(self)

        self.dashboard = None
        self.notification = None

    def head(self):
        self.title("Rutas del sabor")
        self.iconbitmap(get_image_path("logo.ico"))

    def position(self):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición para colocar la ventana en el centro
        window_width = 700
        window_height = 700
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Colocar la ventana en el centro de la pantalla
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def structure(self):
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_rowconfigure((0,2), weight=1)

    def success_login(self,token):
        self.hidden_window()
        session.set_token(token)
        self.open_dashboard()

    def hidden_window(self):
        self.withdraw()
    
    def show_window(self):
        self.dashboard.destroy()
        self.deiconify()

    def open_register(self):
        self.login_frame.grid_forget()
        self.register_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

    def open_login(self,action=None):
        self.register_frame.grid_forget()
        self.login_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

        if action is not None:
            if action == 'success register':
                self.open_notification("¡ Registrado con éxito !")
        
    def open_dashboard(self):
        if self.dashboard is None or not self.dashboard.winfo_exists():
            self.dashboard = Dashboard(self)
        else:
            self.dashboard.focus()

    def open_notification(self, message):
        if self.notification is None or not self.notification.winfo_exists():
            self.notification = Notification(self, message)
        else:
            self.notification.focus()

    def load_bg(self):
        self.bg_image = ctk.CTkImage(Image.open(get_image_path("bg.png")),size=(700,700))
        self.background_image = ctk.CTkLabel(self, image=self.bg_image)
        self.background_image.grid(row=0, column=0,rowspan=3, columnspan=3, sticky="nsew")

    def load_fonts(self):
        pass

