#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
#######

import sys
import pkgutil
from inspect import isclass
from importlib import import_module

from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

import fit_configurations.view.tabs as tabs
from fit_configurations.view import classname2objectname




#fit-commom
from fit_configurations.utils import resolve_path, get_version


from fit_assets import resources


class Configuration(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Configuration, self).__init__(parent)

        self.__tabs = []
        self.__init_ui()

    def __init_ui(self):
        loader = QUiLoader()
        ui_file = QFile(resolve_path("fit_configurations/ui/configuration.ui"))
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

        self.minimize_button = self.loaded_ui.findChild(QtWidgets.QPushButton, "minimize_button")
        self.minimize_button.clicked.connect(self.showMinimized)

        self.close_button = self.loaded_ui.findChild(QtWidgets.QPushButton, "close_button")
        self.close_button.clicked.connect(self.close)

        self.version = self.loaded_ui.findChild(QtWidgets.QLabel, "version")
        self.version.setText(get_version())

        self.cancel_button = self.loaded_ui.findChild(QtWidgets.QPushButton, "cancel_button")
        self.cancel_button.clicked.connect(self.reject)

        self.save_button = self.loaded_ui.findChild(QtWidgets.QPushButton, "save_button")
        self.save_button.clicked.connect(self.accept)

        self.menu_tabs = self.loaded_ui.findChild(QtWidgets.QTreeWidget, "menu_tabs")
        self.tabs = self.loaded_ui.findChild(QtWidgets.QStackedWidget, "tabs")

        self.__load_tabs()
        for tab in self.__tabs:
            self.menu_tabs.addTopLevelItem(QtWidgets.QTreeWidgetItem([tab.name]))

        if self.menu_tabs.topLevelItemCount() > 0:
            self.tabs.setCurrentIndex(0)
            self.menu_tabs.topLevelItem(0).setSelected(True)
            self.menu_tabs.itemClicked.connect(self.__on_tab_clicked)

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

        for importer, modname, ispkg in pkgutil.walk_packages(
            path=package.__path__, prefix=package.__name__ + ".", onerror=lambda x: None
        ):
            if modname not in sys.modules and not ispkg:
                import_module(modname)

            if modname in sys.modules and not ispkg:
                class_name = [
                    x for x in dir(sys.modules[modname])
                    if isclass(getattr(sys.modules[modname], x))
                    and getattr(sys.modules[modname], "__is_tab__", False)
                    and x.lower() == modname.rsplit(".", 1)[1]
                ]

                if class_name:
                    
                    class_name = class_name[0]
                    ui_tab = self.loaded_ui.findChild(QtWidgets.QWidget, classname2objectname.__dict__.get(class_name.upper()))


                    if ui_tab:
                        tab_class = getattr(sys.modules[modname], class_name)
                        tab = tab_class(
                            ui_tab, tabs.__dict__.get(ui_tab.objectName().upper())
                        )
                        self.__tabs.append(tab)

    def accept(self):
        for tab in self.__tabs:
            tab.accept()
        return super().accept()

    def reject(self):
        for tab in self.__tabs:
            tab.reject()
        return super().reject()
