from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter

from snake.renderer import Renderer


class Board(QFrame):
    UPDATE_INTERVAL = 120
    statusUpdated = pyqtSignal(str)

    def __init__(self, game, parent):
        super().__init__(parent)

        self.game = game

        self.timer = QBasicTimer()
        self.timer.start(self.UPDATE_INTERVAL, self)

        self.setFocusPolicy(Qt.StrongFocus)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.game.update()
            self.update()
            self.update_status()
        else:
            super().timerEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setViewport(self.contentsRect())

        renderer = Renderer(painter)
        renderer.render(self.game.field)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Space:
            self.game.pause()
            return

        if self.game.is_paused:
            return

        if key == Qt.Key_Left:
            self.game.turn('left')
        elif key == Qt.Key_Right:
            self.game.turn('right')
        elif key == Qt.Key_Down:
            self.game.turn('down')
        elif key == Qt.Key_Up:
            self.game.turn('up')
        else:
            super().keyPressEvent(event)

    def update_status(self):
        status = 'Score: {0}'.format(self.game.score)
        if self.game.is_paused:
            status = 'PAUSED'
        elif self.game.is_dead:
            status = 'GAME OVER. ' + status
        self.statusUpdated.emit(status)


class SnakeWindow(QMainWindow):

    def __init__(self, game):
        super().__init__()

        self.board = Board(game, self)
        self.status_bar = self.statusBar()

        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.board)

        self.board.statusUpdated[str].connect(self.status_bar.showMessage)

        self.setWindowTitle('Snake')
        self.resize(600, 600)
        self.center()
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

