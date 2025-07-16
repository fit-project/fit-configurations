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


class PacketCaptureModel(TabModel):
    __tablename__ = "configuration_packet_capture"

    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean)
    filename = Column(String)

    def set_default_values(self):
        self.enabled = True
        self.filename = "acquisition.pcap"

        self.db.session.add(self)
        self.commit()

    def update(self, options):
        self.update_by_id(options.get("id"), options)
