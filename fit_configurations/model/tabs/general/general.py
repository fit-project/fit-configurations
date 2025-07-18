#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_common.core.utils import get_platform
from sqlalchemy import Column, Integer, String

from fit_configurations.model.tabs.tab import TabModel


class GeneralModel(TabModel):
    __tablename__ = "configuration_general"

    id = Column(Integer, primary_key=True)
    cases_folder_path = Column(String)
    home_page_url = Column(String)
    language = Column(String)
    user_agent = Column(String)

    def set_default_values(self):
        default_path_by_os = {
            "lin": "~/Documents/FIT",
            "macos": "~/Documents/FIT",
            "win": "~/Documents/FIT",
            "other": "~/Documents/FIT",
        }

        self.cases_folder_path = default_path_by_os[get_platform()]
        self.home_page_url = "https://github.com/fit-project"
        self.user_agent = self.translations["DEFAULT_USER_AGENT"]
        self.language = "english"

        self.db.session.add(self)
        self.commit()

    def update(self, configuration):
        self.update_by_id(configuration.get("id"), configuration)
