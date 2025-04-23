import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QDrag, QPixmap, QIcon, QPainter, QCursor
from PySide6.QtCore import Qt, QMimeData, QUrl, QPoint, QTimer


#clsse che crea finestra con la lista dei video da trascinare
class FileDragLabel(QListWidget):
    def __init__(self, file_paths):
        super().__init__()
        self.file_paths = file_paths
        self.setViewMode(QListWidget.IconMode)
        self.setIconSize(QPixmap("images/am.png").size())
        #print (("images/am.png").size())
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
            print(self.get_icon(path))
            item = QListWidgetItem(icon, os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.addItem(item)
#todo make better
    def get_icon(self, path):
            return "images/am.png"

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
        if not os.path.exists(icon_path):
            print("Icon not found at:", icon_path)
        else :
            print("Icon found at:", icon_path)
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


class MainWindow(QWidget):
    def __init__(self, files):
        super().__init__()
        self.setWindowTitle("ASTROMOSTRO Drag & Drop")
        self.setGeometry(5500, 10, 400, 300)
      #  self.setGeometry(1500, 100,400, 300)
        layout = QVBoxLayout()
        self.file_list = FileDragLabel(files)
        layout.addWidget(self.file_list)
        self.setLayout(layout)

        button_layout = QHBoxLayout()
        self.button_next = QPushButton("Successivo")
        self.button_next.clicked.connect(self.close)
        button_layout.addWidget(self.button_next)

        self.button_exit = QPushButton("Termina")
        self.button_exit.clicked.connect(self.exit_application)
        button_layout.addWidget(self.button_exit)

        layout.addLayout(button_layout)

      #  self.timer = QTimer()
       # self.timer.timeout.connect(self.on_time_finished)
      #  self.timer.start(20000)  # 20 secondi

    def on_time_finished(self):
        print("Tempo scaduto!")
        self.close()

    def exit_application(self):
        # Perform any cleanup if necessary
        print("Exiting application...")
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Solo per debug
    print("Starting application")

    file_list = [
        r"C:\Users\Admin\Dropbox\ASTROMOSTRO\pt-PT\up\Áries Horóscopo Previsão Diária 21 abril 2025.mp4",
    ]

    window = MainWindow(file_list)
    window.show()
    sys.exit(app.exec())