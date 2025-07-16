#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_configurations.model.db import Db

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class LegalProceedingTypeModel(Base):
    __tablename__ = "configuration_legal_proceeding_types"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)

    def get(self):
        if self.db.session.query(LegalProceedingTypeModel).first() is None:
            self.set_default_values()

        return self.db.session.query(LegalProceedingTypeModel).all()

    def add(self, names):
        rows = []
        for name in names:
            if name:
                proceedings = LegalProceedingTypeModel()
                proceedings.name = name.strip()
                rows.append(proceedings)

        self.db.session.add_all(rows)
        self.db.session.commit()

    def delete(self, ids):
        if ids:
            self.db.session.query(LegalProceedingTypeModel).filter(
                LegalProceedingTypeModel.id.in_(ids)
            ).delete(synchronize_session=False)
            self.db.session.commit()

    def set_default_values(self):
        self.add(["Civile", "Extragiudiziale", "Penale"])
