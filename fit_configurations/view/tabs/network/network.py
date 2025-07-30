#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
######

from fit_common.core import get_platform, is_admin, is_npcap_installed
from PySide6 import QtCore, QtWidgets

from fit_configurations.controller.tabs.network.network_check import (
    NetworkCheckController,
)
from fit_configurations.controller.tabs.network.network_tool import (
    NetworkToolController,
)
from fit_configurations.view.tabs.tab import TabView


class NetworkView(TabView):
    __is_tab__ = True

    def __init__(self, tab: QtWidgets.QWidget, name: str):
        self.tool_controller = NetworkToolController()
        self.check_controller = NetworkCheckController()
        self._tool_config = self.tool_controller.configuration
        self._check_config = self.check_controller.configuration

        super().__init__(tab, name)

    def init_ui(self):
        # TOOL CHECKBOXES
        self.whois = self.find(QtWidgets.QCheckBox, "whois")
        self.headers = self.find(QtWidgets.QCheckBox, "headers")
        self.traceroute = self.find(QtWidgets.QCheckBox, "traceroute")
        self.ssl_keylog = self.find(QtWidgets.QCheckBox, "ssl_keylog")
        self.nslookup = self.find(QtWidgets.QCheckBox, "nslookup")
        self.ssl_certificate = self.find(QtWidgets.QCheckBox, "ssl_certificate")

        # NETWORK CHECK INPUTS
        self.ntp_server = self.find(QtWidgets.QLineEdit, "ntp_server")
        self.nslookup_dns_server = self.find(QtWidgets.QLineEdit, "nslookup_dns_server")
        self.nslookup_enable_tcp = self.find(QtWidgets.QCheckBox, "nslookup_enable_tcp")
        self.nslookup_enable_verbose_mode = self.find(
            QtWidgets.QCheckBox, "nslookup_enable_verbose_mode"
        )

    def set_form_data(self, _):
        # Tool config
        self.whois.setChecked(self._tool_config["whois"])
        self.headers.setChecked(self._tool_config["headers"])
        self.ssl_keylog.setChecked(self._tool_config["ssl_keylog"])
        self.nslookup.setChecked(self._tool_config["nslookup"])
        self.ssl_certificate.setChecked(self._tool_config["ssl_certificate"])

        enabled = self._tool_config["traceroute"]
        if enabled and is_admin() and get_platform() != "win":
            enabled = True
        elif (
            enabled and is_admin() and get_platform() == "win" and is_npcap_installed()
        ):
            enabled = True
        else:
            enabled = False
        self.traceroute.setEnabled(enabled)
        self.traceroute.setChecked(enabled)

        # Check config
        self.ntp_server.setText(self._check_config["ntp_server"])
        self.nslookup_dns_server.setText(self._check_config["nslookup_dns_server"])
        self.nslookup_enable_tcp.setChecked(self._check_config["nslookup_enable_tcp"])
        self.nslookup_enable_verbose_mode.setChecked(
            self._check_config["nslookup_enable_verbose_mode"]
        )

    def collect_form_data(self):
        for key in self._tool_config:
            item = self.find(QtCore.QObject, key)
            if isinstance(item, QtWidgets.QCheckBox):
                self._tool_config[key] = item.isChecked()

        for key in self._check_config:
            item = self.find(QtCore.QObject, key)
            if isinstance(item, QtWidgets.QLineEdit):
                self._check_config[key] = item.text()
            elif isinstance(item, QtWidgets.QCheckBox):
                self._check_config[key] = item.isChecked()

        return self._tool_config, self._check_config

    def accept(self):
        self.collect_form_data()
        self.tool_controller.configuration = self._tool_config
        self.check_controller.configuration = self._check_config

    def reject(self):
        self.set_form_data(None)
