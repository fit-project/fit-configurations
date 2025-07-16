#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6 import QtWidgets
from fit_configurations.view.tabs.tab import TabView
from fit_configurations.controller.tabs.packet_capture.packet_capture import PacketCaptureController
from fit_common.core.utils import is_admin, is_npcap_installed, get_platform


class PacketCaptureView(TabView):
    controller_class = PacketCaptureController

    def init_ui(self):
        self.enable_checkbox: QtWidgets.QCheckBox = self.find(QtWidgets.QCheckBox, "enable_packet_capture_recorder")
        self.filename_input: QtWidgets.QLineEdit = self.find(QtWidgets.QLineEdit, "packet_capture_recorder_filename")

        self.enable_checkbox.stateChanged.connect(self._on_enable_checkbox_changed)

    def _on_enable_checkbox_changed(self):
        self.filename_input.setEnabled(self.enable_checkbox.isChecked())

    def set_form_data(self, data):
        enabled = data.get("enabled", False)
        if enabled and is_admin():
            if get_platform() == "win":
                enabled = is_npcap_installed()
            else:
                enabled = True
        else:
            enabled = False

        self.enable_checkbox.setEnabled(enabled)
        self.enable_checkbox.setChecked(enabled)
        self.filename_input.setText(data.get("filename", ""))
        self._on_enable_checkbox_changed()

    def collect_form_data(self):
        return {
            "enabled": self.enable_checkbox.isChecked(),
            "filename": self.filename_input.text().strip(),
        }
