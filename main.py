#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

from fit_common.core import AcquisitionType
from PySide6.QtWidgets import QApplication

from fit_configurations.view.configuration import Configuration


def main():
    app = QApplication(sys.argv)
    window = Configuration(acquisition_type=AcquisitionType.WEB)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
