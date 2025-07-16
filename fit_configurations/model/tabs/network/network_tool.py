#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from sqlalchemy import Column, Integer, Boolean
from fit_configurations.model.tabs.tab import TabModel


class NetworkToolModel(TabModel):
    __tablename__ = "configuration_network_tools"

    id = Column(Integer, primary_key=True)
    whois = Column(Boolean)
    headers = Column(Boolean)
    traceroute = Column(Boolean)
    ssl_keylog = Column(Boolean)
    nslookup = Column(Boolean)
    ssl_certificate = Column(Boolean)

    def set_default_values(self):
        self.whois = True
        self.headers = True
        self.traceroute = True
        self.ssl_keylog = True
        self.nslookup = True
        self.ssl_certificate = True

        self.db.session.add(self)
        self.commit()

    def update(self, configuration):
        self.update_by_id(configuration.get("id"), configuration)
