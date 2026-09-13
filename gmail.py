#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from core.utils import clear_screen, print_banner, print_menu
from modules.spam_engine import send_spam
from modules.config_view import show_config

def main():
    """Función principal"""
    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        opcion = input("\033[96m[?] Selecciona una opción: \033[0m")
        
        if opcion == '1':
            send_spam()
        elif opcion == '2':
            show_config()
        elif opcion == '3':
            print("\n\033[93m[*] Saliendo...\033[0m")
            time.sleep(0.5)
            break
        else:
            print("\n\033[91m[!] Opción inválida\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[93m[*] Programa interrumpido\033[0m")
        exit(0)
