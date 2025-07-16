#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
######

import os
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog

from fit_common.core.utils import resolve_db_path
from fit_common.gui.clickable_label import ClickableLabel as ClickableLabelView
from fit_configurations.view.tabs.tab import TabView
from fit_configurations.controller.tabs.general.general import GeneralController
from fit_configurations.controller.tabs.general.legal_proceeding_type import LegalProceedingTypeController
from fit_configurations.lang import load_translations


class GeneralView(TabView):
    controller_class = GeneralController
    __is_tab__ = True

    def init_ui(self):
        self.translations = load_translations()

        self.cases_folder_path = self.find(QtWidgets.QLineEdit, "cases_folder_path")
        self.cases_folder_button = self.find(QtWidgets.QPushButton, "cases_folder_button")
        self.cases_folder_button.clicked.connect(self.__select_cases_folder)

        self.home_page_url = self.find(QtWidgets.QLineEdit, "home_page_url")
        self.user_agent = self.find(QtWidgets.QPlainTextEdit, "user_agent")
        self.user_agent_button = self.find(QtWidgets.QPushButton, "user_agent_button")
        self.user_agent_button.clicked.connect(self.__default_user_agent)

        self.user_agent_layout = self.find(QtWidgets.QVBoxLayout, "user_agent_layout")
        self.user_agent_layout.addWidget(
            ClickableLabelView(
                self.translations["USER_AGENT_SITE"],
                self.translations["USER_AGENT_SITE_LABEL"]
            )
        )

        self.types_proceedings = self.find(QtWidgets.QPlainTextEdit, "types_proceedings")

        self.db_path = self.find(QtWidgets.QLineEdit, "db_path")
        self.db_path.setText(resolve_db_path("configurations.db"))

    def __select_cases_folder(self):
        folder = QFileDialog.getExistingDirectory(
            None,
            self.translations["SELECT_CASE_FOLDER"],
            os.path.expanduser(self.cases_folder_path.text()),
            QFileDialog.Option.ShowDirsOnly
        )
        if folder:
            self.cases_folder_path.setText(folder)

    def __default_user_agent(self):
        self.user_agent.setPlainText(self.translations["DEFAULT_USER_AGENT"])

    def set_form_data(self, data):
        self.cases_folder_path.setText(data["cases_folder_path"])
        self.home_page_url.setText(data["home_page_url"])
        self.user_agent.setPlainText(data["user_agent"])
        self.types_proceedings.setPlainText(
            ",".join(LegalProceedingTypeController().names)
        )

    def collect_form_data(self):
        return {
            "id": self._configuration["id"],
            "cases_folder_path": self.cases_folder_path.text(),
            "home_page_url": self.home_page_url.text(),
            "language": self._configuration["language"],  # se non modificabile nel form
            "user_agent": self.user_agent.toPlainText()
        }

    def accept(self):
        super().accept()
        LegalProceedingTypeController().names = self.types_proceedings.toPlainText().split(",")
