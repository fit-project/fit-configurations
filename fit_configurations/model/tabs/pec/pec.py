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


class PecModel(TabModel):
    __tablename__ = "configuration_pec"

    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean)
    pec_email = Column(String)
    password = Column(String)
    smtp_server = Column(String)
    smtp_port = Column(String)
    imap_server = Column(String)
    imap_port = Column(String)
    retries = Column(Integer)

    def set_default_values(self):
        self.enabled = False
        self.pec_email = ""
        self.password = ""
        self.smtp_server = ""
        self.smtp_port = ""
        self.imap_server = ""
        self.imap_port = ""
        self.retries = 5

        self.db.session.add(self)
        self.commit()

    def update(self, options):
        self.update_by_id(options.get("id"), options)
