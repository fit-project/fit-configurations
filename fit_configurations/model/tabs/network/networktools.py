#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_configurations.model.db import Db
from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class NetworkTools(Base):
    __tablename__ = "configuration_option"
    id = Column(Integer, primary_key=True)
    whois = Column(Boolean)
    headers = Column(Boolean)
    traceroute = Column(Boolean)
    ssl_keylog = Column(Boolean)
    nslookup = Column(Boolean)
    ssl_certificate = Column(Boolean)

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)

    def get(self):
        if self.db.session.query(NetworkTools).first() is None:
            self.set_default_values()

        return self.db.session.query(NetworkTools).all()

    def update(self, configuration):
        self.db.session.query(NetworkTools).filter(
            NetworkTools.id == configuration.get("id")
        ).update(configuration)
        self.db.session.commit()

    def set_default_values(self):
        self.whois = True
        self.headers = True
        self.traceroute = True
        self.ssl_keylog = True
        self.nslookup = True
        self.ssl_certificate = True
        self.db.session.add(self)
        self.db.session.commit()
