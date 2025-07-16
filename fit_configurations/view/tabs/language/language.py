#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
######

from PySide6 import QtWidgets

from fit_configurations.view.tabs.tab import TabView
from fit_configurations.controller.tabs.language.language import LanguageController
from fit_configurations.lang import load_translations


class LanguageView(TabView):
    controller_class = LanguageController
    __is_tab__ = True

    def init_ui(self):
        self.translations = load_translations()

        self.report_language = self.find(QtWidgets.QComboBox, "report_language")
        self.report_language.addItem(self.translations["ITALIAN"])
        self.report_language.addItem(self.translations["ENGLISH"])
        self.report_language.lineEdit().setReadOnly(True)
        self.report_language.lineEdit().setPlaceholderText(
            self.translations["REPORT_LANGUAGE"]
        )

    def set_form_data(self, data):
        self.report_language.setCurrentText(data["language"])

    def collect_form_data(self):
        return {
            "id": self._configuration["id"],
            "language": self.report_language.currentText(),
        }
