#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


import os

from PySide6 import QtWidgets
from fit_configurations.view.tab import Tab


from fit_configurations.controller.tabs.language.language import (
    Language as LanguageController,
)

from fit_configurations.lang import load_translations


__is_tab__ = True


class Language(Tab):

    def __init__(self, tab: QtWidgets.QWidget, name: str):
        super().__init__(tab, name)

        self.__options = LanguageController().options
        self.translations = load_translations()
        self.__init_ui()
        self.__set_current_config_values()

    def __init_ui(self):

        # REPORT LANGUAGE
        self.report_language = self.tab.findChild(
            QtWidgets.QComboBox, "report_language"
        )

        self.report_language.addItem(self.translations["ITALIAN"])
        self.report_language.addItem(self.translations["ENGLISH"])

        self.report_language.lineEdit().setReadOnly(True)
        self.report_language.lineEdit().setPlaceholderText(
            self.translations["REPORT_LANGUAGE"]
        )

    def __set_current_config_values(self):
        self.report_language.setCurrentText(self.__options["language"])

    def __get_current_values(self):
        self.__options["language"] = self.report_language.currentText()

    def accept(self):
        self.__get_current_values()
        LanguageController().options = self.__options
