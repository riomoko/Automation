import sys
from tts import TTS
from windowAM import MainWindow
from autoGui import AguiTools
from PyQt5.QtWidgets import QApplication
from DropList import FileDropWidget
import time
import threading
import pyautogui as agui
from windowAM import MainWindow

def dragAndDropBis(imageToDrag, imageToDropOn):
    print("nuovo drag and drop 1")
    # Attendere 5 secondi per posizionare il cursore sull'elemento da trascinare
    time.sleep(1)
    print("nuovo drag and drop 2")
    TTS.read("provo a draggare")
    locationToDrag = agui.locateCenterOnScreen(imageToDrag, confidence=0.8)
    print("AM locationToDrag"+str(locationToDrag))
    locationToDropOn = agui.locateCenterOnScreen(imageToDropOn, confidence=0.8)
    print("tiktok locationToDropOn"+str(locationToDropOn))
    agui.moveTo(locationToDrag)
    time.sleep(2)
    TTS.read("dovrei essere in posizione")
    agui.mouseDown(button='left')
    agui.moveTo(locationToDropOn, duration=1)  # Durata di 1 secondo per il movimento
    # Rilasciare il mouse per completare il drag and drop
    agui.mouseUp(button='left')
    TTS.read("dovrei aver droppato")
    time.sleep(5)
    TTS.read("drop terminato")

# Funzione per gestire la finestra principale
def run_window(file_list):
    app = QApplication(sys.argv)
  #  app = QApplication([])
    window = MainWindow(file_list)
    window.show()
    app.exec_()

# Funzione per eseguire il controllo immagine
def run_image_check():
    imageCheck("icons/am.png")

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



TTS.read("Iniziamo")


agui_tools = AguiTools()
if agui_tools.imagePresent("images/red_upload.png"):
    print("Icona Rossatrovata")
    app = QApplication(sys.argv)
    window = FileDropWidget()
    window.show()
    # Avvia l'applicazione e aspetta che venga chiusa
    app.exec_()

    # Dopo che la finestra è chiusa, ottieni la lista dei file
    file_paths = window.get_file_paths()
    print("File selezionati:", file_paths)
    TTS.read("fails ricevuti")
else:
    print("Icona non trovata")
    TTS.read("Icona non trovata")


app.closeAllWindows()


print("Starting application")
file_list = file_paths

for file_path in file_paths:

    imageCheck("images/red_upload.png")
    agui_tools.imageClick("images/red_upload.png")
    imageCheck("images/video_upload.png")

   # print(f"Elaboro il file: {file_path}")
    file_name = file_path.split(' ')[0]
    file_name = file_name.split('/')[-1]
    TTS.read(file_name)
    file_list = [file_path]

    print("lancio windows")
    print (file_list)

  #  window_thread = threading.Thread(target=run_window, args=(file_list,))
 #   window_thread.start()
  #  time.sleep(10)

  #  app = QApplication(sys.argv)
    window = MainWindow(file_list)
    window.show()
    app.exec_()








  #  thread_drop = threading.Thread(target=dragAndDropBis, args=("icons/am.png", "images/video_upload.png"))
   # thread_drop.start()
 #   thread_drop.join()
  #  app = QApplication(sys.argv)

 #   QTimer.singleShot(8000, window.on_timer_finished)
    print("cioppa")
    # Creazione dei thread
 #
  #  image_check_thread = threading.Thread(target=imageCheck, args=("icons/am.png",10))


    # Avvio dei thread

  #  window_thread.start()
   # image_check_thread.start()
   # image_check_thread.join()
  #  print("pre drop")


   # thread_drop.join()
    print("Bingo")

 #   print("video upload trovato")


TTS.read("closed")



sys.exit(app.exec_())


TTS.read("Finito")


