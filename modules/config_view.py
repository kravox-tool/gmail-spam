# -*- coding: utf-8 -*-

from core.utils import clear_screen, print_banner

def show_config():
    """Muestra información de configuración"""
    clear_screen()
    print_banner()
    
    config_info = """
\033[96m╔══════════════════════════════════════════════════════════╗
║              INFORMACIÓN DE CONFIGURACIÓN                ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║        1. Abre en tu navegador/PC:                       ║
║     myaccount.google.com/apppasswords                    ║
║                                                          ║
║  2. Inicia sesión con tu cuenta de Gmail                 ║
║                                                          ║
║  3. En "Seleccionar app" elige: "Otra"                   ║
║                                                          ║
║  4. Escribe un nombre: "Spam Tool"                       ║
║                                                          ║
║  5. Haz clic en "GENERAR"                                ║
║                                                          ║
║  6. Copia la contraseña de 16 caracteres                 ║
║     (aparece en amarillo)                                ║
║                                                          ║
║  ⚠️  IMPORTANTE: La contraseña solo se muestra una vez    ║ 
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝\033[0m
"""
    print(config_info)
    input("Presiona Enter para volver al menú...")
