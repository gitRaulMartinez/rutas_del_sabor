import customtkinter as ctk
import threading

import src.services.auth as auth_service

import src.utils.colors as color

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=color.BG_LOGIN, corner_radius=10,bg_color=color.BG_LIGHT, border_width=1)
        self.parent = parent

        self.label_title = ctk.CTkLabel(self,text='Inicio de Sesión',fg_color="transparent",font=ctk.CTkFont(size=25,weight='bold'))
        self.label_title.grid(row=1, column=0, padx=15, pady=(15,0), sticky="we")

        self.label_username = ctk.CTkLabel(self,text='Usuario:',fg_color="transparent",font=ctk.CTkFont(size=16))
        self.label_username.grid(row=2, column=0, padx=15, pady=(30,0), sticky="w")

        self.entry_username = ctk.CTkEntry(self, placeholder_text="Usuario",fg_color="transparent", width=350, height=40, font=ctk.CTkFont(size=14), border_width=1)
        self.entry_username.grid(row=3, column=0, padx=15, pady=(0,10), sticky="w")

        self.label_password = ctk.CTkLabel(self,text='Contraseña:',fg_color="transparent",font=ctk.CTkFont(size=16))
        self.label_password.grid(row=4, column=0, padx=15, pady=(10,0), sticky="w")

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Contraseña",fg_color="transparent", width=350, height=40, font=ctk.CTkFont(size=14) ,show="*", border_width=1)
        self.entry_password.grid(row=5, column=0, padx=15, pady=(0,10), sticky="w")

        self.label_response = ctk.CTkLabel(self,text="", height=40, fg_color="transparent",font=ctk.CTkFont(size=16))
        self.label_response.grid(row=6, column=0, padx=15, pady=(0,5), sticky="we")

        self.button_login = ctk.CTkButton(self, text="Iniciar Sesión", text_color=color.TEXT_BUTTON, fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,command=self.submit, width=350, border_spacing=10, font=ctk.CTkFont(size=14,weight='bold'))
        self.button_login.grid(row=7, column=0, padx=15, pady=(10,5))

        self.button_register = ctk.CTkButton(self, text="Registrarse", text_color=color.TEXT_BUTTON, fg_color=color.SECONDARY,hover_color=color.HOVER_SECONDARY, command=self.register, width=350, border_spacing=10, font=ctk.CTkFont(size=14,weight='bold'))
        self.button_register.grid(row=8, column=0, padx=15, pady=(5,15))

        # Quitar luego
        self.entry_username.insert(0,"marquitos10")
        self.entry_password.insert(0,"marco123")

    def submit(self):
        self.button_login.configure(text="Cargando...",state="disabled",fg_color=color.BUTTON_DISABLED, text_color_disabled=color.TEXT_BUTTON)
        #self.update_idletasks()
        thread = threading.Thread(target=self.login_request)
        thread.start()
    
    def login_request(self):
        result = auth_service.login(self.entry_username.get(),self.entry_password.get())
        if result:
            if 'token' in result:
                self.parent.success_login(result['token'])
            else:
                self.label_response.configure(text=result['message'])
        self.button_login.configure(text="Iniciar Sesión",state="normal",fg_color=color.PRIMARY)
    
    def register(self):
        self.label_response.configure(text="")
        self.parent.open_register()
            

        

        
        


