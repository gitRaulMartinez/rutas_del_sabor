import customtkinter as ctk
import threading
import tkinter as tk
import src.services.auth as auth_service
import src.utils.form_control as form_control
import src.utils.colors as color
import src.utils.fonts as font

class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=color.BG_LOGIN, bg_color=color.BG_LIGHT ,border_width=1, corner_radius=10)
        self.parent = parent

        self.label_title = ctk.CTkLabel(self,text='Registrarse',fg_color="transparent",font=font.text_ultra_bold_font(),text_color=color.TEXT)
        self.label_title.grid(row=1, column=0, padx=15, pady=(20,20), sticky="we")

        self.form()
        self.actions()

    def form(self):
        self.label_username = ctk.CTkLabel(self,text='Usuario:',fg_color="transparent",font=font.text_normal_font(),text_color=color.TEXT)
        self.label_username.grid(row=2, column=0, padx=15, pady=(10,0), sticky="w")

        self.entry_username = ctk.CTkEntry(self, placeholder_text="Usuario",fg_color="transparent", width=350, height=40, font=ctk.CTkFont(size=14), border_width=1)
        self.entry_username.grid(row=3, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_error_username = ctk.CTkLabel(self,text='',fg_color="transparent",font=ctk.CTkFont(size=12),text_color="red")
        self.label_error_username.grid(row=4, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_password = ctk.CTkLabel(self,text='Contraseña:',fg_color="transparent",font=font.text_normal_font(),text_color=color.TEXT)
        self.label_password.grid(row=5, column=0, padx=15, pady=(2,0), sticky="w")

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Contraseña",fg_color="transparent", width=350, height=40, font=ctk.CTkFont(size=14) ,show="*", border_width=1)
        self.entry_password.grid(row=6, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_error_password = ctk.CTkLabel(self,text='',fg_color="transparent",font=ctk.CTkFont(size=12),text_color="red")
        self.label_error_password.grid(row=7, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_name = ctk.CTkLabel(self,text='Nombre:',fg_color="transparent",font=font.text_normal_font(),text_color=color.TEXT)
        self.label_name.grid(row=8, column=0, padx=15, pady=(2,0), sticky="w")

        self.entry_name = ctk.CTkEntry(self, placeholder_text="Nombre",fg_color="transparent", width=350, height=40, font=ctk.CTkFont(size=14), border_width=1)
        self.entry_name.grid(row=9, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_error_name = ctk.CTkLabel(self,text='',fg_color="transparent",font=ctk.CTkFont(size=12),text_color="red")
        self.label_error_name.grid(row=10, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_lastname = ctk.CTkLabel(self,text='Apellido:',fg_color="transparent",font=font.text_normal_font(),text_color=color.TEXT)
        self.label_lastname.grid(row=11, column=0, padx=15, pady=(2,0), sticky="w")

        self.entry_lastname = ctk.CTkEntry(self, placeholder_text="Apellido",fg_color="transparent", width=350, height=40, font=ctk.CTkFont(size=14), border_width=1)
        self.entry_lastname.grid(row=12, column=0, padx=15, pady=(0,0), sticky="w")

        self.label_error_lastname = ctk.CTkLabel(self,text='',fg_color="transparent",font=ctk.CTkFont(size=12),text_color="red")
        self.label_error_lastname.grid(row=13, column=0, padx=15, pady=(0,0), sticky="w")

    def actions(self):
        self.button_register = ctk.CTkButton(self, text="Registrarme", text_color=color.TEXT_BUTTON,fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,command=self.submit, width=350, border_spacing=8, font=font.text_normal_bold_font())
        self.button_register.grid(row=14, column=0, padx=15, pady=(10,5))

        self.button_login = ctk.CTkButton(self, text="Volver al Inicio", text_color=color.TEXT_BUTTON,fg_color=color.SECONDARY,hover_color=color.HOVER_SECONDARY,command=self.login, width=350, border_spacing=8, font=font.text_normal_bold_font())
        self.button_login.grid(row=15, column=0, padx=15, pady=(5,15))

    def submit(self):
        result = self.form_control()
        if result:
            self.button_register.configure(text="Cargando...",state="disabled",fg_color=color.BUTTON_DISABLED, text_color_disabled=color.TEXT_BUTTON)
            thread = threading.Thread(target=self.register_request)
            thread.start()
        
    def register_request(self):
        result = self.form_control()
        if result:
            response = auth_service.register(self.entry_username.get(), self.entry_password.get(), self.entry_name.get(), self.entry_lastname.get())
            if response is not None:
                if response['status'] == 200:
                    self.parent.open_login(action="success register")
                    self.reset()
                    self.delete_errors()
                else:
                    self.label_error_username.configure(text="Este usuario ya existe")
        self.button_register.configure(text="Registrarme",state="normal",fg_color=color.PRIMARY)
    
    def login(self):
        self.delete_errors()
        self.parent.open_login()

    def form_control(self):
        self.delete_errors()
        self.delete_spaces()
        user_result = self.control_user(self.entry_username.get())
        password_result = self.control_password(self.entry_password.get())
        name_result = self.control_name(self.entry_name.get())
        lastname_result = self.control_lastname(self.entry_lastname.get())

        if(user_result and password_result and name_result and lastname_result):
            return True
        else:
            return False

            
    def control_user(self,user):
        if user == "":
            self.label_error_username.configure(text="Campo vacio")
            return False
        elif form_control.control_min_len(user):
            self.label_error_username.configure(text="Minimo de caracteres 4")
            return False
        elif form_control.control_max_len(user):
            self.label_error_username.configure(text="Maximo de caracteres 20")
            return False
        elif form_control.control_user(user):
            self.label_error_username.configure(text="Formato incorrecto: Solo letras y numeros")
            return False
        else:
            return True
    
    def control_password(self,password):
        if password == "":
            self.label_error_password.configure(text="Campo vacio")
            return False
        elif form_control.control_min_len(password):
            self.label_error_password.configure(text="Minimo de caracteres 4")
            return False
        elif form_control.control_max_len(password):
            self.label_error_password.configure(text="Maximo de caracteres 20")
            return False
        else:
            return True
    
    def control_name(self,name):
        if name == "":
            self.label_error_name.configure(text="Campo vacio")
            return False
        elif form_control.control_min_len(name):
            self.label_error_name.configure(text="Minimo de caracteres 4")
            return False
        elif form_control.control_max_len(name):
            self.label_error_name.configure(text="Maximo de caracteres 20")
            return False
        elif form_control.control_name_and_lastname(name):
            self.label_error_name.configure(text="Formato incorrecto: Solo letras y espacios")
            return False
        else:
            return True
    
    def control_lastname(self,lastname):
        if lastname == "":
            self.label_error_lastname.configure(text="Campo vacio")
            return False
        elif form_control.control_min_len(lastname):
            self.label_error_lastname.configure(text="Minimo de caracteres 4")
            return False
        elif form_control.control_max_len(lastname):
            self.label_error_lastname.configure(text="Maximo de caracteres 20")
            return False
        elif form_control.control_name_and_lastname(lastname):
            self.label_error_lastname.configure(text="Formato incorrecto: Solo letras y espacios")
            return False
        else:
            return True
    
    def delete_errors(self):
        self.label_error_username.configure(text="")
        self.label_error_password.configure(text="")
        self.label_error_name.configure(text="")
        self.label_error_lastname.configure(text="")

    def delete_spaces(self):
        value = self.entry_username.get().strip()
        self.entry_username.delete(0,tk.END)
        self.entry_username.insert(0,value)

        value = self.entry_name.get().strip()
        self.entry_name.delete(0,tk.END)
        self.entry_name.insert(0,value)

        value = self.entry_lastname.get().strip()
        self.entry_lastname.delete(0,tk.END)
        self.entry_lastname.insert(0,value)

    def reset(self):
        self.entry_username.delete(0,tk.END)
        self.entry_password.delete(0,tk.END)
        self.entry_name.delete(0,tk.END)
        self.entry_lastname.delete(0,tk.END)