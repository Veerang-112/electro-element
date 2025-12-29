import sys
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt, QTimer, QEventLoop, QProcess
from main import Custom_Title_UI

class SplashScreen(QSplashScreen):
    def __init__(self, gif_path):
        super().__init__(QPixmap(gif_path))
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        #self.showMaximized()
        self.movie = QMovie(gif_path)
        self.movie.frameChanged.connect(self.onNextFrame)
        self.movie.start()

    def onNextFrame(self):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)

    def showEvent(self, event):
        super().showEvent(event)
        # Adjust the size to cover the entire screen
        self.setGeometry(0, 0, self.screen().size().width(), self.screen().size().height())

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Path to your GIF file
    gif_path = '6fce97c9-cabb-418a-8d9e-39c6511d37a2.gif'

    splash = SplashScreen(gif_path)
    splash.show()

    # Create the main window
    main_window = Custom_Title_UI()

    # Close the splash screen after a delay (e.g., 5000 milliseconds or 5 seconds)
    delay_ms = 8000

    # Use a QEventLoop to delay the splash screen closing
    loop = QEventLoop()
    QTimer.singleShot(delay_ms, loop.quit)
    loop.exec_()

    # Close the splash screen
    splash.close()

    # Show the main window
    main_window.show()

    sys.exit(app.exec_())
