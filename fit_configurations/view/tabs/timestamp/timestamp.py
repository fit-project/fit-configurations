#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6 import QtWidgets

from fit_configurations.controller.tabs.timestamp.timestamp import TimestampController
from fit_configurations.view.tabs.tab import TabView


class TimestampView(TabView):
    controller_class = TimestampController

    def init_ui(self):
        self.enable_timestamp = self.find(QtWidgets.QCheckBox, "enable_timestamp")
        self.timestamp_settings = self.find(QtWidgets.QFrame, "timestamp_settings")
        self.timestamp_server_name = self.find(
            QtWidgets.QLineEdit, "timestamp_server_name"
        )
        self.timestamp_certificate_url = self.find(
            QtWidgets.QLineEdit, "timestamp_certificate_url"
        )

        self.enable_timestamp.stateChanged.connect(self._toggle_timestamp_settings)

    def _toggle_timestamp_settings(self):
        self.timestamp_settings.setEnabled(self.enable_timestamp.isChecked())

    def set_form_data(self, data):
        self.enable_timestamp.setChecked(data.get("enabled", False))
        self.timestamp_server_name.setText(data.get("server_name", ""))
        self.timestamp_certificate_url.setText(data.get("cert_url", ""))
        self._toggle_timestamp_settings()

    def collect_form_data(self):
        return {
            "id": self._configuration["id"],
            "enabled": self.enable_timestamp.isChecked(),
            "server_name": self.timestamp_server_name.text().strip(),
            "cert_url": self.timestamp_certificate_url.text().strip(),
        }
