#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
#######

from fit_configurations.view.configuration import Configuration

from fit_configurations.controller.tabs.language.language import (
    Language as LanguageController,
)


def get_language():
    controller = LanguageController()
    return controller.options["language"]


def show_configuration_dialog():
    Configuration().show()
