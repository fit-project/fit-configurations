#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from sqlalchemy import Column, Integer, String
from fit_configurations.model.tabs.tab import TabModel


class LanguageModel(TabModel):
    __tablename__ = "configuration_language"

    id = Column(Integer, primary_key=True)
    language = Column(String)

    def set_default_values(self):
        self.language = "Italian"
        self.db.session.add(self)
        self.commit()

    def update(self, options):
        self.update_by_id(options.get("id"), options)