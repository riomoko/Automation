import pyautogui as agui
import time

class AguiTools:

    def __init__(self):
        pass
    def imagePresent(self, image):
      #  print("cercando immagine")
       # print (images)
        try:
            location = agui.locateOnScreen(image, confidence=0.8)
            print(location)
            return True
        except Exception as e:
            print(f"Errore generico: {e}")
            return False

    def imageClick(self, image):
        location = agui.locateCenterOnScreen(image, confidence=0.75)
        agui.moveTo(location, duration=0.2)
        agui.click()

    def dragAndDrop(self, imageToDrag, imageToDropOn, delay=1.9):
        locationToDrag = agui.locateCenterOnScreen(imageToDrag, confidence=0.8)
        locationToDropOn = agui.locateCenterOnScreen(imageToDropOn, confidence=0.8)
        agui.moveTo(locationToDrag)
        agui.dragTo(locationToDropOn, duration=delay)

    def dragAndDropBis(self, imageToDrag, imageToDropOn):
        print("nuovo drag and drop")
        # Attendere 5 secondi per posizionare il cursore sull'elemento da trascinare
        time.sleep(5)
        print("nuovo drag and drop")
        locationToDrag = agui.locateCenterOnScreen(imageToDrag, confidence=0.8)
        print(locationToDrag)
        locationToDropOn = agui.locateCenterOnScreen(imageToDropOn, confidence=0.8)
        print(locationToDropOn)
        agui.moveTo(locationToDrag )

        # Simulare il click del mouse per iniziare il drag
        agui.mouseDown(button='left')


        agui.moveTo(locationToDropOn , duration=1)  # Durata di 1 secondo per il movimento

        # Rilasciare il mouse per completare il drag and drop
        agui.mouseUp(button='left')

    def moveToImageCenter(self, image, delay=0.6):
        location = agui.locateCenterOnScreen(image, confidence=0.8)
        agui.moveTo(location, duration=delay)




    # === ESEMPIO USO ===
if __name__ == "__main__":
    try:
        upload_location = agui.locateOnScreen("images/plus_upload.png", confidence=0.9)
        if upload_location is not None:
            uploadPos = agui.center(upload_location)
            print(uploadPos)
            agui.moveTo(uploadPos)
            agui.sleep(3.5)
            agui.click()
        else:
            print("Errore: icona di upload non trovata.")
    except Exception as e:
        print(f"Errore generico: {e}")

