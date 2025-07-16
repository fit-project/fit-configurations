#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog


from fit_configurations.view.tab import Tab

from fit_common.gui.clickable_label import ClickableLabel as ClickableLabelView
from fit_common.core.utils import resolve_db_path

from fit_configurations.controller.tabs.general.legal_proceeding_type import LegalProceedingTypeController
from fit_configurations.controller.tabs.general.general import (
    GeneralController as GeneralController,
)
from fit_configurations.lang import load_translations


import os

__is_tab__ = True


class GeneralView(Tab):

    def __init__(self, tab: QtWidgets.QWidget, name: str):
        super().__init__(tab, name)

        self.__configuration = GeneralController().configuration

        self.translations = load_translations()

        self.__init_ui()
        self.__set_current_config_values()

    def __init_ui(self):
        # CASES FOLDER LINE-EDIT
        self.cases_folder_path = self.tab.findChild(
            QtWidgets.QLineEdit, "cases_folder_path"
        )

        # CASES FOLDER BUTTON
        self.cases_folder_button = self.tab.findChild(
            QtWidgets.QPushButton, "cases_folder_button"
        )
        self.cases_folder_button.clicked.connect(self.__select_cases_folder)

        # HOME PAGE URL LINE-EDIT
        self.home_page_url = self.tab.findChild(QtWidgets.QLineEdit, "home_page_url")

        # USER AGENT PLAIN-TEXT-EDIT
        self.user_agent = self.tab.findChild(QtWidgets.QPlainTextEdit, "user_agent")

        # USER AGENT LAYOUT
        self.user_agent_layout = self.tab.findChild(
            QtWidgets.QVBoxLayout, "user_agent_layout"
        )
        # CLIKABLELABEL
        self.user_agent_layout.addWidget(
            ClickableLabelView(
                self.translations["USER_AGENT_SITE"],
                self.translations["USER_AGENT_SITE_LABEL"],
            )
        )
        # USER AGENT RESET BUTTON
        self.user_agent_button = self.tab.findChild(
            QtWidgets.QPushButton, "user_agent_button"
        )
        self.user_agent_button.clicked.connect(self.__default_user_agent)

        # TYPES PROCEEDINGS PLAIN-TEXT-EDIT
        self.types_proceedings = self.tab.findChild(
            QtWidgets.QPlainTextEdit, "types_proceedings"
        )

        self.db_path = self.tab.findChild(QtWidgets.QLineEdit, "db_path")
        self.db_path.setText(resolve_db_path("configurations.db"))

    def __select_cases_folder(self):
        cases_folder = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            self.translations["SELECT_CASE_FOLDER"],
            os.path.expanduser(self.cases_folder_path.text()),
            QFileDialog.Option.ShowDirsOnly,
        )
        self.cases_folder_path.setText(cases_folder)

    def __default_user_agent(self):
        self.user_agent.setPlainText(self.translations["DEFAULT_USER_AGENT"])

    def __set_current_config_values(self):
        self.cases_folder_path.setText(self.__configuration["cases_folder_path"])
        self.home_page_url.setText(self.__configuration["home_page_url"])
        self.user_agent.setPlainText(self.__configuration["user_agent"])
        self.types_proceedings.setPlainText(
            ",".join([str(elem) for elem in LegalProceedingTypeController().names])
        )

    def __save_current_values(self):
        for keyword in self.__configuration:
            item = self.tab.findChild(QtCore.QObject, keyword)
            if item is not None:
                if (
                    isinstance(item, QtWidgets.QComboBox) is not False
                    and item.currentText()
                ):
                    item = item.currentText()
                elif isinstance(item, QtWidgets.QLineEdit) is not False and item.text():
                    item = item.text()
                elif (
                    isinstance(item, QtWidgets.QPlainTextEdit) is not False
                    and item.toPlainText()
                ):
                    item = item.toPlainText()

                self.__configuration[keyword] = item

    def accept(self):
        self.__save_current_values()
        GeneralController().configuration = self.__configuration
        LegalProceedingTypeController().names = self.types_proceedings.toPlainText().split(
            ","
        )
