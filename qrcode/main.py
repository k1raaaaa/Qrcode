import qrcode
import cv2
import colorama
from colorama import Fore, Style
from qrcode.constants import ERROR_CORRECT_L
import os

colorama.init()

text = (Fore.RED + """
   ____     ____            __  ___    ___    _____  ______    ______    ____ 
  / __ \   / __ \          /  |/  /   /   |  / ___/ /_  __/   / ____/   / __ \ 
 / / / /  / /_/ / ______  / /|_/ /   / /| |  \__ \   / /     / __/     / /_/ /
/ /_/ /  / _, _/ /_____/ / /  / /   / ___ | ___/ /  / /     / /___    / _, _/ 
\___\_\ /_/ |_|         /_/  /_/   /_/  |_|/____/  /_/     /_____/   /_/ |_|  by k1ra 
                                                                              
""" + Style.RESET_ALL)

def main():
    os.system("cls")
    print(text)
    p = input("1- Gen qrcodes   2-Lecteur qrcodes [BETA]   choisi un nombre\n=>")

    if p == '1':
        qr()

    if p == '2':
        lecteur()

def qr():
    lien = input("entrer un lien\n=>  ")
    taille = input("entrer la taille de votre Qrcode (1 à 40)\n=>  ")
    couleur = input("""entrer une couleur (black, blue, red, yellow, green)
    \n/!\ Merci d'écrire une seule couleur pas en majuscule !\n=>  """)
    nom = input ("entre le nom de ton fichier\n=> ")
    qr = qrcode.QRCode(
        version = taille,
        error_correction=ERROR_CORRECT_L,
    )
    qr.add_data(lien)
    img = qr.make_image(back_color=('white'), fill_color=(couleur))
    img.save(nom + '.png')

    y = input("m-MENU\n=>")

    if y == 'm':
        main()

def lecteur():
    print(Fore.RED + "VERSION NON FINIE LA LECTURE DES QRCODES PEUT ETRE OBSELETE " + Style.RESET_ALL)
    qr = input("nom de ton fichier (ex: qrcode.png)\n=>")
    a = cv2.QRCodeDetector()

    valeur, point, donne = a.detectAndDecode(cv2.imread(qr))

    print(valeur)

    y = input("m-MENU\n=>")

    if y == 'm':
        main()



if __name__ == '__main__':
    main()