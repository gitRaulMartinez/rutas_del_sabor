import customtkinter as ctk

import os

from src.assets.assets import FILE

def get_font_path(font):
    return os.path.join(os.path.dirname(os.path.realpath(FILE)), "fonts", font)

def title_font():
    return ctk.CTkFont(family="Roboto Condensed",size=25,weight="bold")

def subtitle_font():
    return ctk.CTkFont(family="Roboto Condensed",size=20,weight="bold")

def logo_font():
    return ctk.CTkFont(family="Roboto Condensed",size=18,weight="bold")

def nav_font():
    return ctk.CTkFont(family="Roboto Condensed",size=14,weight="normal")

def button_font():
    return ctk.CTkFont(family="Roboto Condensed",size=16,weight="bold")

def text_hight_font():
    return ctk.CTkFont(family="Open Sans",size=18,weight="normal")

def text_normal_font():
    return ctk.CTkFont(family="Open Sans",size=16,weight="normal")

def text_small_font():
    return ctk.CTkFont(family="Open Sans",size=14,weight="normal")

def text_normal_bold_fond():
    return ctk.CTkFont(family="Open Sans",size=16,weight="bold")

def text_small_bold_fond():
    return ctk.CTkFont(family="Open Sans",size=15,weight="bold")