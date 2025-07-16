#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
######

from sqlalchemy import inspect

from fit_configurations.controller.tabs.tab import TabController
from fit_configurations.model.tabs.general.legal_proceeding_type import LegalProceedingTypeModel


class LegalProceedingTypeController(TabController):
    def __init__(self):
        super().__init__(LegalProceedingTypeModel)
        self._proceedings = self._serialize(self._configuration)
        self._names = [p["name"] for p in self._proceedings]

    def _serialize(self, rows):
        return [
            {
                column.key: getattr(row, column.key)
                for column in inspect(row).mapper.column_attrs
            }
            for row in rows
        ]

    def get_proceeding_name_by_id(self, id):
        match = next((p for p in self._proceedings if p["id"] == id), None)
        return match["name"] if match else "N/A"

    @property
    def proceedings(self):
        return self._proceedings

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, names):
        existing_names = self._names

        names_to_delete = [p["id"] for p in self._proceedings if p["name"] not in names]
        names_to_add = [name for name in names if name not in existing_names]

        if names_to_delete:
            self.model.delete_by_ids(names_to_delete)

        if names_to_add:
            self.model.add(names_to_add)
