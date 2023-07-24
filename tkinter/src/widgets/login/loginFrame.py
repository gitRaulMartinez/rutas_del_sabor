import customtkinter

import src.services.auth.auth as auth_service

from src.utils.colors import BG_LIGHT,BG_DARK, BG_LOGIN, TEXT, HOVER_NAV, TEXT_BUTTON, SECONDARY, HOVER_SECONDARY, PRIMARY, HOVER_PRIMARY

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=BG_LOGIN, corner_radius=15,bg_color=BG_LIGHT, border_width=1)
        self.parent = parent

        self.label_title = customtkinter.CTkLabel(self,text='Inicio de Sesión',fg_color="transparent",font=customtkinter.CTkFont(size=25,weight='bold'))
        self.label_title.grid(row=1, column=0, padx=15, pady=(15,0), sticky="we")

        self.label_username = customtkinter.CTkLabel(self,text='Usuario:',fg_color="transparent",font=customtkinter.CTkFont(size=16))
        self.label_username.grid(row=2, column=0, padx=15, pady=(30,0), sticky="w")

        self.entry_username = customtkinter.CTkEntry(self, placeholder_text="Usuario",fg_color="transparent", width=350, height=40, font=customtkinter.CTkFont(size=14), border_width=1)
        self.entry_username.grid(row=3, column=0, padx=15, pady=(0,10), sticky="w")

        self.label_password = customtkinter.CTkLabel(self,text='Contraseña:',fg_color="transparent",font=customtkinter.CTkFont(size=16))
        self.label_password.grid(row=4, column=0, padx=15, pady=(10,0), sticky="w")

        self.entry_password = customtkinter.CTkEntry(self, placeholder_text="Contraseña",fg_color="transparent", width=350, height=40, font=customtkinter.CTkFont(size=14) ,show="*", border_width=1)
        self.entry_password.grid(row=5, column=0, padx=15, pady=(0,10), sticky="w")

        self.label_response = customtkinter.CTkLabel(self,text="", height=40, fg_color="transparent",font=customtkinter.CTkFont(size=16))
        self.label_response.grid(row=6, column=0, padx=15, pady=(0,5), sticky="we")

        self.button_login = customtkinter.CTkButton(self, text="Iniciar Sesión", text_color=TEXT_BUTTON, fg_color=PRIMARY,hover_color=HOVER_PRIMARY,command=self.submit, width=350, border_spacing=10, font=customtkinter.CTkFont(size=14,weight='bold'))
        self.button_login.grid(row=7, column=0, padx=15, pady=(10,5))

        self.button_register = customtkinter.CTkButton(self, text="Registrarse", text_color=TEXT_BUTTON, fg_color=SECONDARY,hover_color=HOVER_SECONDARY, command=self.register, width=350, border_spacing=10, font=customtkinter.CTkFont(size=14,weight='bold'))
        self.button_register.grid(row=8, column=0, padx=15, pady=(5,15))

        # Quitar luego
        self.entry_username.insert(0,"marquitos10")
        self.entry_password.insert(0,"marco123")

    def submit(self):
        self.button_login.configure(text="Cargando...",state="disabled")
        self.update_idletasks()

        result = auth_service.login(self.entry_username.get(),self.entry_password.get())
        if result:
            if 'token' in result:
                self.parent.success_login(result['token'])
            else:
                self.label_response.configure(text=result['message'])
        self.button_login.configure(text="Iniciar Sesión",state="normal")
        
    
    def register(self):
        self.label_response.configure(text="")
        self.parent.open_register()
            

        

        
        


