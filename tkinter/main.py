import tkinter
import customtkinter

from src.views.login import LoginFrame

class Login(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rutas del sabor")

        self.position()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.checkbox_frame = LoginFrame(self)
        self.checkbox_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def position(self):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición para colocar la ventana en el centro
        window_width = 450
        window_height = 600
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Colocar la ventana en el centro de la pantalla
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def open_main(self):
        main = Main()
        self.destroy()
        main.mainloop()

        

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rutas del sabor")

        self.position()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def position(self):
        # Obtener las dimensiones de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición para colocar la ventana en el centro
        window_width = 1200
        window_height = 800
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Colocar la ventana en el centro de la pantalla
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")



if __name__ == "__main__":
    login = Login()
    login.mainloop()