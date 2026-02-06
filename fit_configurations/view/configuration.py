#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
#######

from importlib import import_module
from inspect import isclass

from fit_assets import resources  # noqa: F401
from fit_common.core import get_version
from fit_common.gui.ui_translation import translate_ui
from PySide6 import QtCore, QtWidgets

from fit_configurations.lang import load_translations
from fit_configurations.view.configuration_ui import Ui_fit_configuration
from fit_configurations.view.tabs import TAB_MODULES


class Configuration(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Configuration, self).__init__(parent)
        self.__translations = load_translations()

        self.__tabs = []
        self.__init_ui()

    def __init_ui(self):
        self.ui = Ui_fit_configuration()
        self.ui.setupUi(self)

        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # CUSTOM TOP BAR
        self.ui.left_box.mouseMoveEvent = self.move_window

        # MINIMIZE BUTTON
        self.ui.minimize_button.clicked.connect(self.showMinimized)

        # CLOSE BUTTON
        self.ui.close_button.clicked.connect(self.close)

        self.ui.version.setText(f"v{get_version()}")

        self.ui.cancel_button.clicked.connect(self.reject)

        self.ui.save_button.clicked.connect(self.accept)

        translate_ui(self.__translations, self)

        self.__load_tabs()
        for tab in self.__tabs:
            self.ui.menu_tabs.addTopLevelItem(QtWidgets.QTreeWidgetItem([tab.name]))

        if self.ui.menu_tabs.topLevelItemCount() > 0:
            self.ui.tabs.setCurrentIndex(0)
            self.ui.menu_tabs.topLevelItem(0).setSelected(True)
            self.ui.menu_tabs.itemClicked.connect(self.__on_tab_clicked)

    def __on_tab_clicked(self, item, column):
        self.ui.tabs.setCurrentIndex(self.ui.menu_tabs.indexOfTopLevelItem(item))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def __load_tabs(self):
        for modname in TAB_MODULES:
            try:
                module = import_module(modname)
            except Exception:
                continue

            for name in dir(module):
                obj = getattr(module, name)
                if isclass(obj) and getattr(obj, "__is_tab__", False):
                    ui_name = name.replace("View", "").lower()
                    ui_tab = getattr(self.ui, ui_name, None)
                    if not ui_tab:
                        continue
                    tab_instance = obj(
                        ui_tab, self.__translations.get(ui_name.upper(), {})
                    )
                    self.__tabs.append(tab_instance)

    def accept(self):
        for tab in self.__tabs:
            tab.accept()
        return super().accept()

    def reject(self):
        for tab in self.__tabs:
            tab.reject()
        return super().reject()
