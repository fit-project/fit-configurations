#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from sqlalchemy import Column, Integer, String, Boolean
from fit_configurations.model.tabs.tab import TabModel


class NetworkCheckModel(TabModel):
    __tablename__ = "configuration_network_checks"

    id = Column(Integer, primary_key=True)
    ntp_server = Column(String)
    nslookup_dns_server = Column(String)
    nslookup_enable_tcp = Column(Boolean)
    nslookup_enable_verbose_mode = Column(Boolean)

    def set_default_values(self):
        self.ntp_server = "ntp1.inrim.it"
        self.nslookup_dns_server = "1.1.1.1"
        self.nslookup_enable_tcp = False
        self.nslookup_enable_verbose_mode = False

        self.db.session.add(self)
        self.commit()

    def update(self, configuration):
        self.update_by_id(configuration.get("id"), configuration)
