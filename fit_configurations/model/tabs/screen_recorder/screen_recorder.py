#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from sqlalchemy import Boolean, Column, Integer, String, inspect, text

from fit_configurations.model.tabs.tab import TabModel


class ScreenRecorderModel(TabModel):
    __tablename__ = "configuration_screen_recorder"

    id = Column(Integer, primary_key=True)
    enabled_video = Column(Boolean)
    enabled_audio = Column(Boolean)
    filename = Column(String)

    def __init__(self) -> None:
        super().__init__()
        self._migrate_legacy_columns()

    def _migrate_legacy_columns(self) -> None:
        inspector = inspect(self.db.engine)
        if not inspector.has_table(self.__tablename__):
            return

        columns = {
            column["name"] for column in inspector.get_columns(self.__tablename__)
        }

        with self.db.engine.begin() as connection:
            if "enabled" in columns and "enabled_video" not in columns:
                connection.execute(
                    text(
                        "ALTER TABLE configuration_screen_recorder "
                        "RENAME COLUMN enabled TO enabled_video"
                    )
                )
                columns.remove("enabled")
                columns.add("enabled_video")
            if "enabled_audio" not in columns:
                connection.execute(
                    text(
                        "ALTER TABLE configuration_screen_recorder "
                        "ADD COLUMN enabled_audio BOOLEAN DEFAULT 0"
                    )
                )

    def set_default_values(self):
        self.enabled_video = True
        self.enabled_audio = True
        self.filename = "acquisition_video"

        self.db.session.add(self)
        self.commit()

    def update(self, options):
        self.update_by_id(options.get("id"), options)
