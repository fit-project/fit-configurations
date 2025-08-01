#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
#######

import pkgutil
import sys
from importlib import import_module
from importlib.resources import files
from inspect import isclass

from fit_assets import resources  # noqa: F401
from fit_common.core import get_local_version
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

import fit_configurations.view.tabs as tabs
from fit_configurations.lang import load_translations


class Configuration(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Configuration, self).__init__(parent)
        self.translations = load_translations()

        self.__tabs = []
        self.__init_ui()

    def __init_ui(self):
        loader = QUiLoader()
        ui_path = files("fit_configurations.ui").joinpath("configuration.ui")
        ui_file = QFile(str(ui_path))
        ui_file.open(QFile.ReadOnly)
        self.loaded_ui = loader.load(ui_file, self)
        ui_file.close()

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.loaded_ui)
        self.setLayout(layout)

        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # CUSTOM TOP BAR
        self.left_box = self.loaded_ui.findChild(QtWidgets.QWidget, "left_box")
        self.left_box.mouseMoveEvent = self.move_window

        self.minimize_button = self.loaded_ui.findChild(
            QtWidgets.QPushButton, "minimize_button"
        )
        self.minimize_button.clicked.connect(self.showMinimized)

        self.close_button = self.loaded_ui.findChild(
            QtWidgets.QPushButton, "close_button"
        )
        self.close_button.clicked.connect(self.close)

        self.version = self.loaded_ui.findChild(QtWidgets.QLabel, "version_label")
        self.version.setText(get_local_version())

        self.cancel_button = self.loaded_ui.findChild(
            QtWidgets.QPushButton, "cancel_button"
        )
        self.cancel_button.clicked.connect(self.reject)

        self.save_button = self.loaded_ui.findChild(
            QtWidgets.QPushButton, "save_button"
        )
        self.save_button.clicked.connect(self.accept)

        self.menu_tabs = self.loaded_ui.findChild(QtWidgets.QTreeWidget, "menu_tabs")
        self.tabs = self.loaded_ui.findChild(QtWidgets.QStackedWidget, "tabs")

        self.__translate_ui()

        self.__load_tabs()
        for tab in self.__tabs:
            self.menu_tabs.addTopLevelItem(QtWidgets.QTreeWidgetItem([tab.name]))

        if self.menu_tabs.topLevelItemCount() > 0:
            self.tabs.setCurrentIndex(0)
            self.menu_tabs.topLevelItem(0).setSelected(True)
            self.menu_tabs.itemClicked.connect(self.__on_tab_clicked)

    def __translate_ui(self):
        self.__traverse_widgets(self.loaded_ui)

    def __traverse_widgets(self, widget: QtWidgets.QWidget):
        self.__apply_translation(widget)

        for child in widget.findChildren(
            QtWidgets.QWidget, options=QtCore.Qt.FindDirectChildrenOnly
        ):
            self.__traverse_widgets(child)

    def __apply_translation(self, widget: QtWidgets.QWidget):
        name = widget.objectName()
        if not name:
            return

        key = name.upper()

        if key not in self.translations:
            return

        value = self.translations[key]

        # Se ha testo, sostituiscilo
        if (
            hasattr(widget, "text")
            and callable(widget.text)
            and hasattr(widget, "setText")
        ):
            current_text = widget.text()
            if current_text is not None and current_text.strip() != "":
                widget.setText(value)

        # Se ha placeholder, sostituiscilo
        if (
            hasattr(widget, "placeholderText")
            and callable(widget.placeholderText)
            and hasattr(widget, "setPlaceholderText")
        ):
            current_placeholder = widget.placeholderText()
            if current_placeholder is not None and current_placeholder.strip() != "":
                widget.setPlaceholderText(value)

    def __on_tab_clicked(self, item, column):
        self.tabs.setCurrentIndex(self.menu_tabs.indexOfTopLevelItem(item))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def __load_tabs(self):
        package = tabs

        for _, modname, ispkg in pkgutil.walk_packages(
            path=package.__path__,
            prefix=package.__name__ + ".",
            onerror=lambda x: None,
        ):
            if ispkg:
                continue

            if modname not in sys.modules:
                import_module(modname)

            module = sys.modules[modname]
            for name in dir(module):
                obj = getattr(module, name)
                if isclass(obj) and getattr(obj, "__is_tab__", False):
                    ui_name = name.replace("View", "").lower()
                    ui_tab = self.loaded_ui.findChild(QtWidgets.QWidget, ui_name)

                    if ui_tab:
                        tab_instance = obj(ui_tab, self.translations[ui_name.upper()])
                        self.__tabs.append(tab_instance)

    def accept(self):
        for tab in self.__tabs:
            tab.accept()
        return super().accept()

    def reject(self):
        for tab in self.__tabs:
            tab.reject()
        return super().reject()
