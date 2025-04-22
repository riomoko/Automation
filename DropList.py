import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt, QUrl
#classe per raccogliere i video

class DraggableListWidget(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QListWidget.InternalMove)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QListWidget.ExtendedSelection)


class FileDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📂 Trascina e organizza i file")
        self.resize(1000, 800)
        self.setAcceptDrops(True)
        self.file_paths = []
        # Layout e UI
        layout = QVBoxLayout()
        self.label = QLabel("Trascina qui i file\nPuoi ordinarli con Drag & Drop")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 16px; padding: 10px;")
        layout.addWidget(self.label)
        self.list_widget = DraggableListWidget()
        layout.addWidget(self.list_widget)
        self.confirm_button = QPushButton("✅ Conferma")
        self.confirm_button.clicked.connect(self.confirm_files)

        layout.addWidget(self.confirm_button)
        self.setLayout(layout)


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            if url.isLocalFile():
                file_path = url.toLocalFile()
                if file_path not in self.file_paths:
                    self.file_paths.append(file_path)
                    item = QListWidgetItem(file_path)
                    self.list_widget.addItem(item)
                    print(f"📥 File aggiunto: {file_path}")

    def confirm_files(self):
        ordered_paths = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
        print("📋 Lista file ordinata:")
        for i, path in enumerate(ordered_paths, 1):
            print(f"{i}. {path}")
        self.close()

    def get_file_paths(self):
        return self.file_paths

    # === ESEMPIO USO ===
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDropWidget()
    window.show()
    sys.exit(app.exec_())