#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_configurations.model.db import Db

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Timestamp(Base):
    __tablename__ = "configuration_timestamp"

    id = Column(Integer, primary_key=True)
    enabled = Column(Boolean)
    server_name = Column(String)
    cert_url = Column(String)

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)

    def get(self):
        if self.db.session.query(Timestamp).first() is None:
            self.set_default_values()

        return self.db.session.query(Timestamp).all()

    def update(self, options):
        self.db.session.query(Timestamp).filter(
            Timestamp.id == options.get("id")
        ).update(options)
        self.db.session.commit()

    def set_default_values(self):
        self.enabled = True
        self.server_name = "https://freetsa.org/tsr"
        self.cert_url = "https://www.freetsa.org/files/tsa.crt"

        self.db.session.add(self)
        self.db.session.commit()
