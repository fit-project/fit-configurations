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


class LegalProceedingTypeModel(TabModel):
    __tablename__ = "configuration_legal_proceeding_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def set_default_values(self):
        self.add(["Civile", "Extragiudiziale", "Penale"])

    def add(self, names):
        rows = []
        for name in names:
            if name:
                row = self.__class__()
                row.name = name.strip()
                rows.append(row)

        self.db.session.add_all(rows)
        self.commit()

    def delete(self, ids):
        if ids:
            self.db.session.query(self.__class__).filter(
                self.__class__.id.in_(ids)
            ).delete(synchronize_session=False)
            self.commit()
