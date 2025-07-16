#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_configurations.model.tabs.general.general import GeneralModel
from sqlalchemy.inspection import inspect



class GeneralController:
    _configuration = {}

    def __init__(self):
        self.model = GeneralModel()
        self._configuration = self.model.get()

    @property
    def configuration(self):
        instance = self._configuration[0]
        return {
            column.key: getattr(instance, column.key)
            for column in inspect(instance).mapper.column_attrs
        }

    # a setter function
    @configuration.setter
    def configuration(self, configuration):
        self.model.update(configuration)
