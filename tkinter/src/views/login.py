import tkinter
import customtkinter

import src.services.auth.auth as auth_service

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=350, height=400)
        self.success = parent.open_main

        self.label_title = customtkinter.CTkLabel(self,text='Inicio de Sesión',fg_color="transparent",font=('Roboto',25))
        self.label_title.grid(row=1, column=0, padx=20, pady=(20,0), sticky="we")

        self.label_username = customtkinter.CTkLabel(self,text='Usuario:',fg_color="transparent",font=('Roboto',16))
        self.label_username.grid(row=2, column=0, padx=20, pady=(30,0), sticky="w")

        self.entry_username = customtkinter.CTkEntry(self, placeholder_text="Usuario", width=350, height=40, font=('Roboto',16))
        self.entry_username.grid(row=3, column=0, padx=20, pady=(0,10), sticky="w")

        self.label_password = customtkinter.CTkLabel(self,text='Contraseña:',fg_color="transparent",font=('Roboto',16))
        self.label_password.grid(row=4, column=0, padx=20, pady=(10,0), sticky="w")

        self.entry_password = customtkinter.CTkEntry(self, placeholder_text="Contraseña", width=350, height=40, font=('Roboto',16) ,show="*")
        self.entry_password.grid(row=5, column=0, padx=20, pady=(0,10), sticky="w")

        self.label_response = customtkinter.CTkLabel(self,text='', height=40, fg_color="transparent",font=('Roboto',16))
        self.label_response.grid(row=6, column=0, padx=20, pady=(10,10), sticky="we")

        self.button_session = customtkinter.CTkButton(self, text="Iniciar Sesión",command=self.submit, width=350, height=40, font=('Roboto',20))
        self.button_session.grid(row=7, column=0, padx=20, pady=(10,20))

    def submit(self):
        self.button_session.configure(text="Cargando...",state="disabled")
        self.update_idletasks()

        result = auth_service.login(self.entry_username.get(),self.entry_password.get())
        if 'token' in result:
            print(result['token'])
            self.success()
        else:
            self.label_response.configure(text=result['mensaje'])
            self.button_session.configure(text="Iniciar Sesión",state="normal")
            

        

        
        


