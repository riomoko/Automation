import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QPushButton, QListWidget, QListWidgetItem, QLabel)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont


class FileDropArea(QListWidget):
    """Widget personalizzato per il drag & drop dei file"""
    file_dropped = Signal(str)  # Segnale per comunicare con la finestra principale

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                self.file_dropped.emit(path)  # Emetti il segnale invece di chiamare direttamente
        else:
            event.ignore()


class FileDropWindow(QMainWindow):
    """Finestra principale con area drag & drop e pulsante conferma"""

    def __init__(self):
        super().__init__()

        # Configurazione finestra
        self.setWindowTitle("Drag & Drop File")
        self.setMinimumSize(500, 400)
        self.file_paths = []

        # Widget centrale
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principale
        layout = QVBoxLayout(central_widget)

        # Titolo
        title = QLabel("Trascina qui i tuoi file")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Istruzioni
        instructions = QLabel("Trascina i file direttamente su questa finestra")
        instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructions)

        # Area drag & drop
        self.file_list = FileDropArea()
        self.file_list.file_dropped.connect(self.add_file)  # Connetti il segnale al metodo
        layout.addWidget(self.file_list)

        # Contatore file
        self.file_counter = QLabel("File aggiunti: 0")
        self.file_counter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.file_counter)

        # Pulsante conferma
        self.confirm_button = QPushButton("Conferma")
        self.confirm_button.setMinimumHeight(40)
        self.confirm_button.clicked.connect(self.confirm_files)
        layout.addWidget(self.confirm_button)

        # Lista interna dei file
        self.files = []

        # Variabile per i file confermati
        self.confirmed_files = None

    def add_file(self, file_path):
        """Aggiunge un file alla lista"""
        if os.path.isfile(file_path):
            # Evita duplicati
            if file_path not in self.files:
                self.files.append(file_path)
                file_name = os.path.basename(file_path)
                item = QListWidgetItem(file_name)
                item.setToolTip(file_path)  # Mostra il percorso completo al passaggio del mouse
                self.file_list.addItem(item)
                self.update_counter()
        elif os.path.isdir(file_path):
            # Se è una cartella, aggiungiamo tutti i file al suo interno
            try:
                for root, _, files in os.walk(file_path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        if full_path not in self.files:
                            self.files.append(full_path)
                            item = QListWidgetItem(os.path.basename(full_path))
                            item.setToolTip(full_path)
                            self.file_list.addItem(item)
                self.update_counter()
            except Exception as e:
                print(f"Errore nell'aggiunta dei file dalla cartella: {e}")

    def update_counter(self):
        """Aggiorna il contatore dei file"""
        self.file_counter.setText(f"File aggiunti: {len(self.files)}")

    def confirm_files(self):
        """Salva i file selezionati nella variabile confirmed_files"""
        if self.files:
            self.confirmed_files = self.files.copy()
            print(f"File confermati: {len(self.confirmed_files)}")
            for file in self.confirmed_files:
                print(f" - {file}")
                self.file_paths.append(file)
        else:
            print("Nessun file da confermare")
        self.close()

    def get_confirmed_files(self):
        """Restituisce la lista dei file confermati"""
        return self.confirmed_files

    def get_file_paths(self):
        return self.file_paths


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDropWindow()
    window.show()
    sys.exit(app.exec())