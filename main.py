#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PySide6.QtWidgets import QApplication
import sys

from fit_configurations.view.configuration import Configuration


def main():
    app = QApplication(sys.argv)
    window = Configuration()
    window.show()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()
