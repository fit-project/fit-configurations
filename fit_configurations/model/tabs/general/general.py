#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_configurations.model.db import Db

from fit_common.core.utils import get_platform

from fit_configurations.lang import load_translations
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class GeneralModel(Base):
    __tablename__ = "configuration_general"

    id = Column(Integer, primary_key=True)
    cases_folder_path = Column(String)
    home_page_url = Column(String)
    language = Column(String)
    user_agent = Column(String)

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)
        self.translations = load_translations()

    def get(self):
        if self.db.session.query(GeneralModel).first() is None:
            self.set_default_values()

        return self.db.session.query(GeneralModel).all()

    def update(self, configuration):
        self.db.session.query(GeneralModel).filter(
            GeneralModel.id == configuration.get("id")
        ).update(configuration)
        self.db.session.commit()

    def set_default_values(self):
        default_path_by_os = {
            "lin": "~/Documents/FIT",
            "macos": "~/Documents/FIT",
            "win": "~/Documents/FIT",
            "other": "~/Documents/FIT",
        }
        self.cases_folder_path = default_path_by_os[get_platform()]
        self.home_page_url = "https://www.google.it"
        self.user_agent = self.translations["DEFAULT_USER_AGENT"]
        self.language = "english"

        self.db.session.add(self)
        self.db.session.commit()
