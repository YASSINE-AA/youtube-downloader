from PySide2.QtWidgets import QFileDialog, QMainWindow, QLabel, QPushButton, QMenuBar, QLineEdit, QComboBox
from PySide2.QtGui import QFont, QPainter, QPolygon, QBrush, QColor, Qt, QPixmap
from pytube import YouTube


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_init()

    def window_init(self):
        self.setWindowTitle("Youtube Downloader")
        self.resize(600, 310)
        self.setFixedSize(self.size())
        self.ui_components()
        self.show()

    def ui_components(self):
        font = QFont("Roboto", 20)
        font2 = QFont("Roboto", 14)

        logoImg = QPixmap("logo.png")
        logo = QLabel("", self)
        logo.setPixmap(logoImg)
        logo.adjustSize()
        logo.resize(70, 45)
        logo.move(122, 47)

        logo.setScaledContents(True)
        title_label = QLabel("Youtube Downloader", self)
        title_label.setFont(font)
        title_label.setStyleSheet("color: white")
        title_label.move(210, 50)
        title_label.setFont(font)
        title_label.adjustSize()

        # Main Content
        # Link Text
        link_label = QLabel("Insert video link:", self)
        link_label.setFont(font2)
        link_label.adjustSize()
        link_label.move(10, 130)
        # Link LineEdit
        link_box = QLineEdit(self)
        link_box.setPlaceholderText(
            "example: https://www.youtube.com/watch?v=DWOv_pypaHk")
        link_box.setFixedSize(570, 50)
        link_box.move(10, 170)
        link_box.setFont(font2)
        # Convert and download Section
        # Download btn
        download_btn = QPushButton("Download", self)
        download_btn.setFixedSize(100, 50)
        download_btn.move(480, 235)
        download_btn.setStyleSheet("background-color: white; color: #F44336;")

        # Extension selection
        extension = QComboBox(self)
        extension.addItem("mp4")
        # extension.addItem("mp3")
        extension.move(360, 235)
        extension.setFixedHeight(50)
        extension.setFont(font2)
        extension.setStyleSheet("color: #F44336; background-color: white;")

        def download_vid():
            if link_box.text() != '':
                directory_download = QFileDialog.getExistingDirectory(
                    self, 'Select directory')
                yt = YouTube(f'{link_box.text()}')
                yt.streams.filter(progressive=True, file_extension=f"{extension.currentText()}").order_by(
                    'resolution').desc().first().download(directory_download)
        download_btn.clicked.connect(download_vid)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setBrush(
            QBrush(QColor.fromRgb(244, 67, 54), Qt.SolidPattern))
        painter.drawRect(0, 0, 600, 110)
        painter.setBrush(
            QBrush(QColor.fromRgb(211, 47, 47), Qt.SolidPattern))
        painter.drawRect(0, 0, 600, 30)
