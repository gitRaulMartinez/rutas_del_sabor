import customtkinter

from src.widgets.login.loginFrame import LoginFrame
from src.widgets.login.registerFrame import RegisterFrame

from src.views.dashboard import Dashboard

from src.assets.images import path_images

class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.head()
        self.position()
        self.structure()

        self.login_frame = LoginFrame(self)
        self.login_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.register_frame = RegisterFrame(self)

        self.dashboard = None
    
    def head(self):
        self.title("Rutas del sabor")

        image_path = path_images("hola.jpg")
        print(image_path)

    def position(self):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición para colocar la ventana en el centro
        window_width = 500
        window_height = 700
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Colocar la ventana en el centro de la pantalla
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def structure(self):
        self.grid_columnconfigure((0,2), weight=1)
        self.grid_rowconfigure((0,2), weight=1)

    def success_login(self):
        self.hidden_window()
        self.open_dashboard()

    def hidden_window(self):
        self.withdraw()
    
    def show_window(self):
        self.deiconify()

    def open_register(self):
        self.login_frame.grid_forget()
        self.register_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

    def open_login(self):
        self.register_frame.grid_forget()
        self.login_frame.grid(row=1, column=1, padx=0, pady=0, sticky="nsew")

    def open_dashboard(self):
        if self.dashboard is None or not self.dashboard.winfo_exists():
            self.dashboard = Dashboard(self)
        else:
            self.dashboard.focus()