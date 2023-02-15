from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

import ws


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('design.ui', self)

        self.onSearch()
        self.search.clicked.connect(self.onSearch)

    def onSearch(self):
        weather = ws.get_weather(self.query.text())
        icon = QPixmap()
        icon.loadFromData(weather['icon'])
        self.icon.setPixmap(icon)
        self.temperature.setText(f'<html>Температура {weather["temperature"]} &deg;C</html>')
        self.wind_speed.setText(f'Скорость ветра: {weather["wind_speed"]} км/ч')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())