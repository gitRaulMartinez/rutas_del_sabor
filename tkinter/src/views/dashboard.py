import customtkinter

class Dashboard(customtkinter.CTkToplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent

        self.head()
        self.position()
        self.structure()

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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def close_window(self):
        self.parent.destroy()
        