#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from sqlalchemy import inspect

class TabController:
    def __init__(self, model_cls):
        self.model = model_cls()
        self._configuration = self.model.get_first_or_default()

    @property
    def configuration(self):
        instance = self._configuration[0]
        return {
            column.key: getattr(instance, column.key)
            for column in inspect(instance).mapper.column_attrs
        }

    @configuration.setter
    def configuration(self, values: dict):
        self.model.update_by_id(values.get("id"), values)
