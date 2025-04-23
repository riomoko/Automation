import sys
import random
from tts import TTS
from windowAM import MainWindow
from autoGui import AguiTools
from PySide6.QtWidgets import QApplication
import time
import threading
import pyautogui as agui
from windowAM import MainWindow

def dragAndDrop(imageToDrag, imageToDropOn):
    print("nuovo drag and drop 1")
    time.sleep(random.uniform(0.1, 1.8))

    locationToDrag = agui.locateCenterOnScreen(imageToDrag, confidence=0.8)
    print("AM locationToDrag"+str(locationToDrag))
    locationToDropOn = agui.locateCenterOnScreen(imageToDropOn, confidence=0.8)
    print("tiktok locationToDropOn"+str(locationToDropOn))
    agui.moveTo(locationToDrag)
    time.sleep(random.uniform(0.1, 2.1))
    TTS.read("Draggo")
    agui.mouseDown(button='left')
    agui.moveTo(locationToDropOn, duration=random.uniform(0.3, 2.1))  # Durata di 1 secondo per il movimento
    # Rilasciare il mouse per completare il drag and drop
    agui.mouseUp(button='left')
    TTS.read("drop")


# Funzione per gestire la finestra principale
def run_window(file_list):
    app = QApplication(sys.argv)
  #  app = QApplication([])
    window = MainWindow(file_list)
    window.show()
    app.exec_()

# Funzione per eseguire il controllo immagine
def run_image_check():
    imageCheck("images/am.png")

def imageCheck(image, seconds=20):
    ok = False
    for i in range(20):
        print(f"secondi caricamento {i + 1}")
        time.sleep(1)
        if agui_tools.imagePresent(image):
            ok = True
            print(image + " present")
            break
    if not ok:
        print(image + " missing")
        TTS.read(image + " missing")
        TTS.read("Programma terminato")
        sys.exit()

uploadPlus= "images/uploadBuzz.png"
videoUploadArea = "images/uploadVideoBuzz.png"
iconAM="images/am.png"
hashAstromostro = "images/HashAstromostroBuzz.PNG"
uploaded="images/uploadedBuzz.PNG"
post="images/postBuzz.PNG"
views="images/viewsBuzz.PNG"
successivo="images/successivoBuzz.PNG"

for i in range(12):
    TTS.read("automazione iniziata")

    agui_tools = AguiTools()
    imageCheck(uploadPlus)
    agui_tools.imageClick(uploadPlus)
    time.sleep(random.uniform(0.1, 0.12))
   # agui_tools.imageClick(uploadPlus)
    imageCheck(videoUploadArea)
    imageCheck(iconAM)
    time.sleep(random.uniform(0.1,0.2))
    dragAndDrop(iconAM,videoUploadArea )
    time.sleep(random.uniform(0.1, 2.1))
    imageCheck(hashAstromostro)
    TTS.read("tag")
    agui_tools.moveToImageCenter(hashAstromostro, random.uniform(0.3, 1.9))
    for i in range(15):
        agui.click()
      #  TTS.read("t")
        time.sleep(random.uniform(0.1,0.2))
    TTS.read("tag finiti")
    time.sleep(random.uniform(0.1, 2.1))
    imageCheck(uploaded, seconds=40)
    TTS.read("caricato")
    time.sleep(random.uniform(0.1, 1.1))
    agui.scroll(-1300)
    TTS.read("scrollato")
    imageCheck(post)
    time.sleep(random.uniform(0.1, 1.1))
    agui_tools.moveToImageCenter(post, random.uniform(0.3, 1.9))
    time.sleep(random.uniform(0.1, 0.3))
    TTS.read("posto")
    agui.click()

    time.sleep(random.uniform(1, 2.1))
    TTS.read("emozione!!! ")
    imageCheck(views)
    imageCheck(successivo)
    agui_tools.imageClick(successivo)
    time.sleep(random.uniform(2, 3.1))


time.sleep(random.uniform(2, 3.1))
TTS.read("Terminato")
sys.exit(0)












