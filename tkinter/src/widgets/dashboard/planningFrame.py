import customtkinter as ctk
import threading

import src.utils.colors as color
import src.utils.fonts as font

from src.widgets.routeVisit.routeVisitScrollFrame import RouteVisitScrollFrame
from src.widgets.routeVisit.routeVisitCreate import RouteVisitCreate
from src.widgets.routeVisit.routeVisitView import RouteVisitView
from src.widgets.loadings.loadingSmallFrame import LoadingSmallFrame
from src.widgets.notifications.notification import Notification

from src.services.routeVisit import RouteVisitServices

class PlanningFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.BG_LIGHT)
        self.parent = parent
        self.load_structure()
        self.load_data()
        self.load_widgets()
    
    def load_structure(self):
        self.grid_rowconfigure(2,weight=1)
        self.grid_columnconfigure(0,weight=1)

    def load_data(self):
        self.route_visit_services = RouteVisitServices()
        self.routes = self.route_visit_services.get_data()

    def load_widgets(self):
        self.title_frame = TitleFrame(self,command=self.open_create,routes=self.routes)
        self.title_frame.grid(row=0,column=0,padx=10,pady=10,sticky="ew")

        self.title_list_frame = TitleListFrame(self)
        self.title_list_frame.grid(row=1,column=0,padx=(15,26),pady=5,sticky="ew")

        self.list_routes_frame = RouteVisitScrollFrame(self,open_create=self.open_create,open_view=self.open_view)
        self.list_routes_frame.grid(row=2,column=0,padx=(9,10),pady=5,sticky="nsew")

        for route in self.routes:
            self.list_routes_frame.add_item(route)

        self.loading_frame = LoadingSmallFrame(self)
        self.notification = None
    
    def open_create(self):
        self.create_route_toplevel = RouteVisitCreate(self)
        self.create_route_toplevel.grab_set()
    
    def open_view(self,route_visit):
        self.view_route_toplevel = RouteVisitView(self,route_visit)
        self.view_route_toplevel.grab_set()

    def create_route(self,name,list_destinations):
        self.list_routes_frame.grid_forget()
        self.loading_frame.grid(row=2,column=0,padx=(9,10),pady=5,sticky="nsew")
        thread = threading.Thread(target=lambda: self.opeartion_create_route(name,list_destinations))
        thread.start()

    def opeartion_create_route(self,name,list_destinations):
        new_route_visit = self.route_visit_services.create(name=name,list_destinations=list_destinations)
        self.loading_frame.grid_forget()
        self.list_routes_frame.grid(row=2,column=0,padx=(9,10),pady=5,sticky="nsew")
        self.list_routes_frame.add_item(new_route_visit)
        self.routes.append(new_route_visit)
        self.open_notification("¡ Ruta creada con exito !")
        self.title_frame.destroy()
        self.title_frame = TitleFrame(self,command=self.open_create,routes=self.routes)
        self.title_frame.grid(row=0,column=0,padx=15,pady=15,sticky="ew")

    def open_notification(self, message):
        if self.notification is None or not self.notification.winfo_exists():
            self.notification = Notification(self, message)
        else:
            self.notification.focus()

class TitleListFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,fg_color=color.NAV,border_width=1,corner_radius=10)
        self.parent = parent
        self.load_structure()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure(0,weight=0)
        self.grid_columnconfigure(0,weight=1)

    def load_widgets(self):
        self.name_label = ctk.CTkLabel(self,text="Nombre de ruta",text_color=color.TEXT,fg_color="transparent",font=font.text_normal_font(),anchor="w")
        self.name_label.grid(row=0,column=0,padx=(10,2),pady=10,sticky="ew")

        self.date_label = ctk.CTkLabel(self,text="Cantidad de destinos",text_color=color.TEXT,font=font.text_normal_font(),anchor="w",width=250)
        self.date_label.grid(row=0,column=1,padx=2,pady=10,sticky="w")

        self.culinary_destination_label = ctk.CTkLabel(self,text="Acciones",text_color=color.TEXT,font=font.text_normal_font(),anchor="w",width=100)
        self.culinary_destination_label.grid(row=0,column=2,padx=(2,10),pady=10,sticky="w")

class TitleFrame(ctk.CTkFrame):
    def __init__(self, parent,command,routes):
        super().__init__(parent,fg_color="transparent")
        self.parent = parent
        self.routes = routes
        self.command = command
        self.load_structure()
        self.load_widgets()

    def load_structure(self):
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)

    def load_widgets(self):
        self.title_label = ctk.CTkLabel(self,text="Mis rutas de visitas",text_color=color.TEXT,font=font.text_hight_bold_font(),anchor="w")
        self.title_label.grid(row=0,column=0,padx=(10,2),pady=10,sticky="ew")

        if len(self.routes) > 0: 
            self.create_button = ctk.CTkButton(self,text="Crear ruta",text_color=color.TEXT_BUTTON,font=font.text_small_bold_font(),height=30,fg_color=color.PRIMARY,hover_color=color.HOVER_PRIMARY,command=self.command)
            self.create_button.grid(row=0,column=1,padx=(2,10),pady=10,sticky="e")