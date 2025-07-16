#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
######

import imaplib
import smtplib

from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap, QIntValidator
from PySide6.QtWidgets import QMessageBox

from fit_configurations.view.tabs.tab import TabView
from fit_configurations.controller.tabs.pec.pec import PecController
from fit_common.core.utils import resolve_path
from fit_configurations.lang import load_translations
from fit_common.gui.clickable_label import ClickableLabel as ClickableLabelView
from fit_common.gui.error import Error as ErrorView


class PecView(TabView):
    controller_class = PecController

    def init_ui(self):
        self.translations = load_translations()

        self.enable_pec_layout = self.find(QtWidgets.QHBoxLayout, "enable_pec_layout")
        self.enable_pec_layout.addWidget(
            ClickableLabelView(
                self.translations["TWO_FACTOR_AUTH_URL"],
                self.translations["TWO_FACTOR_AUTH"],
            )
        )

        self.enable_pec = self.find(QtWidgets.QCheckBox, "enable_pec")
        self.pec_settings = self.find(QtWidgets.QFrame, "pec_settings")
        self.pec_email = self.find(QtWidgets.QLineEdit, "pec_email")
        self.pec_password = self.find(QtWidgets.QLineEdit, "pec_password")
        self.retries_eml_download = self.find(QtWidgets.QLineEdit, "retries_eml_download")
        self.imap_server = self.find(QtWidgets.QLineEdit, "pec_imap_server")
        self.imap_port = self.find(QtWidgets.QLineEdit, "pec_imap_server_port")
        self.smtp_server = self.find(QtWidgets.QLineEdit, "pec_smtp_server")
        self.smtp_port = self.find(QtWidgets.QLineEdit, "pec_smtp_server_port")
        self.verification_imap_button = self.find(QtWidgets.QPushButton, "verification_imap_button")
        self.info_imap_img = self.find(QtWidgets.QLabel, "info_imap_img_label")
        self.verification_smtp_button = self.find(QtWidgets.QPushButton, "verification_smtp_button")
        self.info_smtp_img = self.find(QtWidgets.QLabel, "info_smtp_img_label")

        self.pec_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.retries_eml_download.setValidator(QIntValidator(0, 10))
        self.imap_port.setValidator(QIntValidator(0, 65535))
        self.smtp_port.setValidator(QIntValidator(0, 65535))

        self.enable_pec.stateChanged.connect(self._toggle_pec_settings)
        self.pec_email.textEdited.connect(self._sanitize_input)
        self.imap_server.textEdited.connect(self._sanitize_input)
        self.smtp_server.textEdited.connect(self._sanitize_input)

        self.verification_imap_button.clicked.connect(self._verify_imap)
        self.verification_smtp_button.clicked.connect(self._verify_smtp)

        self.info_imap_img.setVisible(False)
        self.info_smtp_img.setVisible(False)

    def set_form_data(self, data):
        self.enable_pec.setChecked(data.get("enabled", False))
        self.pec_email.setText(data.get("pec_email", ""))
        self.pec_password.setText(data.get("password", ""))
        self.smtp_server.setText(data.get("smtp_server", ""))
        self.smtp_port.setText(data.get("smtp_port", ""))
        self.imap_server.setText(data.get("imap_server", ""))
        self.imap_port.setText(data.get("imap_port", ""))
        self.retries_eml_download.setText(str(data.get("retries", "0")))

        self._toggle_pec_settings()

    def collect_form_data(self):
        return {
            "enabled": self.enable_pec.isChecked(),
            "pec_email": self.pec_email.text(),
            "password": self.pec_password.text(),
            "smtp_server": self.smtp_server.text(),
            "smtp_port": self.smtp_port.text(),
            "imap_server": self.imap_server.text(),
            "imap_port": self.imap_port.text(),
            "retries": int(self.retries_eml_download.text() or "0"),
        }

    def _toggle_pec_settings(self):
        self.pec_settings.setEnabled(self.enable_pec.isChecked())

    def _sanitize_input(self, text):
        sender = self.tab.sender()
        sender.setText(text.replace(" ", ""))

    def _verify_imap(self):
        self.info_imap_img.setVisible(False)
        try:
            server = imaplib.IMAP4_SSL(self.imap_server.text(), int(self.imap_port.text()))
            server.login(self.pec_email.text(), self.pec_password.text())
            server.logout()
            self.info_imap_img.setPixmap(QPixmap(resolve_path("ui/icons/green-mark.png")).scaled(20, 20))
        except Exception as e:
            self.info_imap_img.setPixmap(QPixmap(resolve_path("ui/icons/red-mark.png")).scaled(20, 20))
            self._show_error(str(e))
        finally:
            self.info_imap_img.setVisible(True)

    def _verify_smtp(self):
        self.info_smtp_img.setVisible(False)
        try:
            server = smtplib.SMTP_SSL(self.smtp_server.text(), int(self.smtp_port.text()))
            server.login(self.pec_email.text(), self.pec_password.text())
            server.quit()
            self.info_smtp_img.setPixmap(QPixmap(resolve_path("ui/icons/green-mark.png")).scaled(20, 20))
        except Exception as e:
            self.info_smtp_img.setPixmap(QPixmap(resolve_path("ui/icons/red-mark.png")).scaled(20, 20))
            self._show_error(str(e))
        finally:
            self.info_smtp_img.setVisible(True)

    def _show_error(self, message):
        ErrorView(
            QMessageBox.Icon.Critical,
            self.translations["LOGIN_FAILED"],
            self.translations["LOGIN_ERROR"],
            message,
        ).exec()
