#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
#######

from PySide6 import QtWidgets


class TabView:
    __is_tab__ = True
    controller_class = None

    def __init__(self, tab: QtWidgets.QWidget, name: str):
        self.tab = tab
        self.name = name

        if self.controller_class:
            self.controller = self.controller_class()
            self._configuration = self.controller.configuration
        else:
            self.controller = None
            self._configuration = {}

        self.init_ui()
        self.set_form_data(self._configuration)

    def init_ui(self):
        pass

    def find(self, widget_type, name):
        return self.tab.findChild(widget_type, name)

    def accept(self):
        if hasattr(self, "controller"):
            self.controller.configuration = self.collect_form_data()

    def reject(self):
        if hasattr(self, "controller"):
            self.set_form_data(self._configuration)

    def collect_form_data(self):
        return {}

    def set_form_data(self, data):
        pass
