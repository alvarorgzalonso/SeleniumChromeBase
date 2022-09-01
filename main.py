import time

import keyboard
import cv2
from selenium import webdriver
import numpy as np
import pickle


print('Nombres:\nDiscover\nHome\nLogIn\nNotificaciones\nPerfil')

def paramos():
    exit()
keyboard.add_hotkey('F1', lambda: paramos())

mobile_emulation = {"deviceName": "iPhone X"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=chrome_options)  # sometimes you have to insert your execution path
driver.get('https://www.google.com')

driver.set_window_size(150, 960)
driver.get('https://www.instagram.com/')

def captura():
    img = cv2.imdecode(np.frombuffer(np.array(driver.get_screenshot_as_png()), np.uint8), -1)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    nombre = input("Nombre de la imagen(pantalla): ")
    path_imagen = "data/imagenes/" + nombre + ".png"
    cv2.imwrite(img, path_imagen)
    print("Imagen guardada en " + path_imagen)

keyboard.add_hotkey('F2', lambda: captura())


def guardarCookies():
    nombre = input("Nombre del archivo de cookes: ")
    ruta_cookie = "data/cookies/" + nombre + ".pk1"
    pickle.dump(driver.get_cookies(), open(ruta_cookie, "wb"))
    print("Cookie guardada en " + ruta_cookie)

keyboard.add_hotkey('F3', lambda: guardarCookies())


def cargarCookies():
    nombre = input("Nombre del archivo de cookes(sin '.pk1'): ")
    ruta_cookie = "data/cookies/" + nombre + ".pk1"
    cookies = pickle.load(open(ruta_cookie, "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    print("Cookie cargada desde " + ruta_cookie)


keyboard.add_hotkey('F4', lambda: cargarCookies())

print('F1: SALIR\nF2: CAPTURA\nF3: GUARDAR COOKIES\nF4: CARGAR COOKIES')
while True:
    time.sleep(1)