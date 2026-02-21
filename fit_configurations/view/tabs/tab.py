#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
#######

from __future__ import annotations

from typing import Any, ClassVar

from PySide6 import QtWidgets


class TabView:
    __is_tab__ = True
    controller_class: ClassVar[type[Any] | None] = None

    def __init__(self, tab: QtWidgets.QWidget, name: str):
        self.tab = tab
        self.name = name
        self.controller: Any | None
        self._configuration: dict[str, Any]

        if self.controller_class is not None:
            self.controller = self.controller_class()
            self._configuration = self.controller.configuration
        else:
            self.controller = None
            self._configuration = {}

        self.init_ui()
        self.set_form_data(self._configuration)

    def init_ui(self) -> None:
        pass

    def find(self, widget_type: type[Any], name: str) -> Any:
        return self.tab.findChild(widget_type, name)

    def accept(self) -> None:
        if self.controller is not None:
            self.controller.configuration = self.collect_form_data()

    def reject(self) -> None:
        if self.controller is not None:
            self.set_form_data(self._configuration)

    def collect_form_data(self) -> dict[str, Any]:
        return {}

    def set_form_data(self, data: dict[str, Any]) -> None:
        pass
