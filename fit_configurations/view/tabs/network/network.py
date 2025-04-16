#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######


from PySide6 import QtCore, QtWidgets
from fit_configurations.view.tab import Tab

from fit_configurations.controller.tabs.network.networktools import (
    NetworkTools as NetworkToolsController,
)
from fit_configurations.controller.tabs.network.networkcheck import (
    NetworkControllerCheck as NetworkCheckController,
)

from fit_common.core.utility import is_admin, is_npcap_installed, get_platform

__is_tab__ = True


class Network(Tab):
    def __init__(self, tab: QtWidgets.QWidget, name: str):
        super().__init__(tab, name)

        self.__configuration_network_tools = NetworkToolsController().configuration
        self.__configuration_network_check = NetworkCheckController().configuration

        self.__init_ui()
        self.__set_current_config_values()

    def __init_ui(self):

        # ENABLE NETWORK TOOLS
        self.whois = self.tab.findChild(QtWidgets.QCheckBox, "whois")
        self.headers = self.tab.findChild(QtWidgets.QCheckBox, "headers")
        self.traceroute = self.tab.findChild(QtWidgets.QCheckBox, "traceroute")
        self.ssl_keylog = self.tab.findChild(QtWidgets.QCheckBox, "ssl_keylog")
        self.nslookup = self.tab.findChild(QtWidgets.QCheckBox, "nslookup")
        self.ssl_certificate = self.tab.findChild(
            QtWidgets.QCheckBox, "ssl_certificate"
        )

        # NTP SERVER
        self.ntp_server = self.tab.findChild(QtWidgets.QLineEdit, "ntp_server")
        # NSLOOKUP DNS SERVER
        self.nslookup_dns_server = self.tab.findChild(
            QtWidgets.QLineEdit, "nslookup_dns_server"
        )
        # NSLOOKUP ENABLE TCP
        self.nslookup_enable_tcp = self.tab.findChild(
            QtWidgets.QCheckBox, "nslookup_enable_tcp"
        )
        # NSLOOKUP ENABLE VERBOSE MODE
        self.nslookup_enable_verbose_mode = self.tab.findChild(
            QtWidgets.QCheckBox, "nslookup_enable_verbose_mode"
        )

    def __set_current_config_values(self):
        self.__set_current_network_tools_values()
        self.__set_current_network_check_values()

    def __set_current_network_tools_values(self):
        self.whois.setChecked(self.__configuration_network_tools["whois"])
        self.headers.setChecked(self.__configuration_network_tools["headers"])
        self.ssl_keylog.setChecked(self.__configuration_network_tools["ssl_keylog"])
        self.nslookup.setChecked(self.__configuration_network_tools["nslookup"])
        self.ssl_certificate.setChecked(
            self.__configuration_network_tools["ssl_certificate"]
        )
        enabled = self.__configuration_network_tools["traceroute"]
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

    def __set_current_network_check_values(self):
        self.ntp_server.setText(self.__configuration_network_check["ntp_server"])
        self.nslookup_dns_server.setText(
            self.__configuration_network_check["nslookup_dns_server"]
        )
        self.nslookup_enable_tcp.setChecked(
            self.__configuration_network_check["nslookup_enable_tcp"]
        )
        self.nslookup_enable_verbose_mode.setChecked(
            self.__configuration_network_check["nslookup_enable_verbose_mode"]
        )

    def __get_current_values(self):
        self.__get_current_network_tools_values()
        self.__get_current_network_check_values()

    def __get_current_network_tools_values(self):
        for keyword in self.__configuration_network_tools:
            item = self.tab.findChild(QtCore.QObject, keyword)
            if isinstance(item, QtWidgets.QCheckBox):
                item = item.isChecked()
                self.__configuration_network_tools[keyword] = item

    def __get_current_network_check_values(self):
        for keyword in self.__configuration_network_check:
            item = self.tab.findChild(QtCore.QObject, keyword)

            if item is not None:
                if isinstance(item, QtWidgets.QLineEdit) is not False and item.text():
                    item = item.text()
                elif isinstance(item, QtWidgets.QCheckBox):
                    item = item.isChecked()

                self.__configuration_network_check[keyword] = item

    def accept(self) -> None:
        self.__get_current_values()
        NetworkToolsController().configuration = self.__configuration_network_tools
        NetworkCheckController().configuration = self.__configuration_network_check
