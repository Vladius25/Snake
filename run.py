#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from snake.game import Game
from snake.gui import SnakeWindow

if __name__ == '__main__':
    app = QApplication([])
    snake = SnakeWindow(Game(30, 30))
    sys.exit(app.exec_())
