#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
######

from fit_configurations.controller.tabs.tab import TabController
from fit_configurations.model.tabs.language.language import LanguageModel


class LanguageController(TabController):
    def __init__(self):
        super().__init__(LanguageModel)
