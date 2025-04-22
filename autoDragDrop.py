import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QListWidget, QListWidgetItem, QWidget, QVBoxLayout
from PyQt5.QtGui import QDrag, QPixmap, QIcon, QPainter, QCursor
from PyQt5.QtCore import Qt, QMimeData, QUrl, QPoint, QTimer
import time
import threading
import pyautogui as agui
from tts import TTS

#clsse che crea finestra con la lista dei video da trascinare
class FileDragLabel(QListWidget):
    def __init__(self, file_paths):
        super().__init__()
        self.file_paths = file_paths
        self.setViewMode(QListWidget.IconMode)
        self.setIconSize(QPixmap("images/default.png").size())
        self.setDragDropMode(QListWidget.DragOnly)  # Imposta la modalità drag-only
        self.setSelectionMode(QListWidget.SingleSelection)
        self.setSpacing(10)
        self.setDragEnabled(True)
        self.populate()
        # Per migliorare la rilevazione degli eventi mouse
        self.setMouseTracking(True)
        # Variabile per tracciare il drag
        self.dragStartPosition = None

    def populate(self):
        for path in self.file_paths:
            icon = QIcon(self.get_icon(path))
            item = QListWidgetItem(icon, os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.addItem(item)
#todo remove this
    def get_icon(self, path):

            return "icons/am.png"

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragStartPosition = event.pos()
            # Debug: stampa l'item al momento del click
            item = self.itemAt(event.pos())
            if item:
                print("Clicked on item:", item.text())
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton) or not self.dragStartPosition:
            return

        # Verifica se il movimento è abbastanza grande per iniziare un drag
        if (event.pos() - self.dragStartPosition).manhattanLength() < QApplication.startDragDistance():
            return

        # Verifica se c'è un item nella posizione di inizio drag
        item = self.itemAt(self.dragStartPosition)
        if not item:
            print("No item found at drag start position")
            return

        # Debug: stampa quale item stiamo trascinando
        print("Starting drag for item:", item.text())

        # Ottieni il percorso del file
        file_path = item.data(Qt.UserRole)
        if not os.path.isfile(file_path):
            print("File not found:", file_path)
            return

        # Crea il drag
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setUrls([QUrl.fromLocalFile(file_path)])
        drag.setMimeData(mime_data)

        # Imposta l'immagine del drag
        icon_path = self.get_icon(file_path)
        pixmap = QPixmap(icon_path)
        if pixmap.isNull():
            print("Warning: Icon not found, using text instead")
            pixmap = QPixmap(100, 30)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.drawText(10, 20, os.path.basename(file_path))
            painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(QPoint(pixmap.width() // 2, pixmap.height() // 2))

        # Esegui il drag
        print("Executing drag operation")
        result = drag.exec_(Qt.CopyAction)
        print("Drag result:", result)

        # Reset della posizione iniziale
        self.dragStartPosition = None


class MainWindowAutoDrop(QWidget):
    def __init__(self, files, imageToDrag, imageToDropOn):
        super().__init__()
        self.setWindowTitle("ASTROMOSTRO Drag & Drop")
        self.setGeometry(3000, 200, 800, 600)
        self.imageToDrag = imageToDrag
        self.imageToDropOn = imageToDropOn
        layout = QVBoxLayout()
        self.file_list = FileDragLabel(files)
        layout.addWidget(self.file_list)
        self.setLayout(layout)
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_time_finished)
        self.timer.start(8000)  # 20 secondi

    def on_time_finished(self):
        print("parte il drag!")
        thread_drop = threading.Thread(target=self.dragAndDrop, args=(self.imageToDrag, self.imageToDropOn))
       # thread_drop.daemon = True  # permette di terminare il thread alla chiusura della finestra
        thread_drop.start()
        thread_drop.join()
        #self.dragAndDrop(self.imageToDrag, self.imageToDropOn)

    def dragAndDrop(self, imageToDrag, imageToDropOn):
        print("nuovo drag and drop 1")
        # Attendere 5 secondi per posizionare il cursore sull'elemento da trascinare
        time.sleep(1)
        print("nuovo drag and drop 2")
        TTS.read("provo a draggare")
        locationToDrag = agui.locateCenterOnScreen(imageToDrag, confidence=0.8)
        print("AM locationToDrag" + str(locationToDrag))
        locationToDropOn = agui.locateCenterOnScreen(imageToDropOn, confidence=0.8)
        print("tiktok locationToDropOn" + str(locationToDropOn))
        agui.moveTo(locationToDrag)
        time.sleep(2)
        print ("dovrei essere in posizione video")
        TTS.read("dovrei essere in posizione video")
        agui.mouseDown(button='left')
        agui.mouseDown(button='left')
        agui.moveTo(locationToDropOn)
        time.sleep(1)
        agui.moveTo(locationToDropOn)  # Durata di 0.5 secondi per il movimento
        # Rilasciare il mouse per completare il drag and drop
        time.sleep(1)
        agui.mouseUp(button='left')
        print ("dovrei aver droppato")
        TTS.read("dovrei aver droppato")
        time.sleep(5)
        print ("drop terminato")
        TTS.read("drop terminato")




if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Solo per debug
    print("Starting application")

    file_list = [
        r"C:\Users\Admin\Dropbox\ASTROMOSTRO\pt-PT\up\Áries Horóscopo Previsão Diária 21 abril 2025.mp4",
    ]

    window = MainWindowAutoDrop(file_list, "icons/am.png", "images/video_upload.png")

    window.show()
    sys.exit(app.exec_())