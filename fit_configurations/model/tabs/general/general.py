#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_common.core import get_platform, get_version
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
        default_user_agent_by_os = {
            "lin": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "macos": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
            "win": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/6.5.0 Chrome/108.0.5359.220 Safari/537.36",
            "other": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/6.5.0 Chrome/108.0.5359.220 Safari/537.36",
        }

        platform = get_platform()
        self.cases_folder_path = default_path_by_os[platform]
        self.home_page_url = "http://fit-project.org/"
        base_user_agent = default_user_agent_by_os[platform]
        version = get_version()
        if version:
            self.user_agent = f"{base_user_agent} FreezingInternetTool/{version}"
        else:
            self.user_agent = base_user_agent
        self.language = "english"

        self.db.session.add(self)
        self.commit()

    def update(self, configuration):
        self.update_by_id(configuration.get("id"), configuration)
