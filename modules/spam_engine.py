# -*- coding: utf-8 -*-

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from core.utils import clear_screen, print_banner

def send_spam():
    """Función principal de spam"""
    clear_screen()
    print_banner()
    
    print("\033[96m" + "="*50 + "\033[0m")
    print("\033[96m  CONFIGURACIÓN DE SPAM\033[0m")
    print("\033[96m" + "="*50 + "\033[0m")
    print()
    
    sender_email = input("\033[93m[+] Tu Gmail: \033[0m")
    sender_password = input("\033[93m[+] Tu Contraseña/App Password: \033[0m")
    
    print()
    print("\033[96m" + "-"*50 + "\033[0m")
    print()
    
    target_email = input("\033[91m[>] Gmail Objetivo: \033[0m")
    subject = input("\033[91m[>] Asunto del mensaje: \033[0m")
    message_body = input("\033[91m[>] Mensaje a enviar: \033[0m")
    
    while True:
        try:
            cantidad = int(input("\033[91m[>] Cantidad de emails: \033[0m"))
            if cantidad > 0:
                break
            else:
                print("\033[91m[!] La cantidad debe ser mayor a 0\033[0m")
        except ValueError:
            print("\033[91m[!] Ingresa un número válido\033[0m")
    
    print()
    confirm = input(f"\033[95m[?] ¿Enviar {cantidad} emails a {target_email}? (s/n): \033[0m").lower()
    
    if confirm != 's':
        print("\n\033[93m[*] Operación cancelada\033[0m")
        time.sleep(1)
        return
    
    print()
    print("\033[92m" + "="*50 + "\033[0m")
    print("\033[92m  INICIANDO ATAQUE SPAM...\033[0m")
    print("\033[92m" + "="*50 + "\033[0m")
    print()
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    exitosos = 0
    fallidos = 0
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        
        for i in range(1, cantidad + 1):
            try:
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = target_email
                msg['Subject'] = f"{subject} #{i}"
                
                msg.attach(MIMEText(message_body, 'plain'))
                
                server.send_message(msg)
                exitosos += 1
                
                print(f"\033[92m[✓] Email {i}/{cantidad} enviado exitosamente\033[0m")
                
                time.sleep(0.5)
                
            except Exception as e:
                fallidos += 1
                print(f"\033[91m[✗] Error enviando email {i}: {str(e)}[0m")
        
        server.quit()
        
    except Exception as e:
        print(f"\033[91m[!] Error de conexión: {str(e)}[0m")
        print("\033[91m[!] Verifica tu email y contraseña\033[0m")
        print("\033[93m[*] Nota: Para Gmail, usa una 'App Password'\033[0m")
        input("\nPresiona Enter para continuar...")
        return
    
    print()
    print("\033[96m" + "="*50 + "\033[0m")
    print(f"\033[96m  RESUMEN:\033[0m")
    print(f"\033[92m  ✓ Exitosos: {exitosos}\033[0m")
    print(f"\033[91m  ✗ Fallidos: {fallidos}\033[0m")
    print("\033[96m" + "="*50 + "\033[0m")
    print()
    input("Presiona Enter para volver al menú...")
