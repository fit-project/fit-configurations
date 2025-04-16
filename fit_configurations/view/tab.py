#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
#######

from PySide6.QtWidgets import QWidget

__is_tab__ = False


class Tab:
    def __init__(self, tab: QWidget, name: str):
        self.tab = tab
        self.name = name

    def reject(self):
        pass