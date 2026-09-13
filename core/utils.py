# -*- coding: utf-8 -*-

import os
from core.config import BOM_BANNER, BOMB_ART, MENU_BANNER

def clear_screen():
    """Limpia la pantalla"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    """Muestra el banner principal"""
    print("\033[91m" + BOM_BANNER + "\033[0m")
    print("\033[93m" + BOMB_ART + "\033[0m")

def print_menu():
    """Muestra el menú"""
    print("\033[92m" + MENU_BANNER + "\033[0m")
