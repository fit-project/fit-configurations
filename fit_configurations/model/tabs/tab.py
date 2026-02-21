#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from __future__ import annotations

from typing import Any

from sqlalchemy.orm import DeclarativeBase

from fit_configurations.lang import load_translations
from fit_configurations.model.db import Db


class Base(DeclarativeBase):
    pass


class TabModel(Base):
    __abstract__ = True

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)
        self.translations = load_translations()

    def commit(self) -> None:
        self.db.session.commit()

    def add_all(self, items: list[Any]) -> None:
        self.db.session.add_all(items)
        self.commit()

    def update_by_id(self, id_: int, data: dict[str, Any]) -> None:
        self.db.session.query(self.__class__).filter_by(id=id_).update(data)
        self.commit()

    def delete_by_ids(self, ids: list[int]) -> None:
        model_id_col = getattr(self.__class__, "id")
        self.db.session.query(self.__class__).filter(model_id_col.in_(ids)).delete(
            synchronize_session=False
        )
        self.commit()

    def get_all(self) -> list[Any]:
        return self.db.session.query(self.__class__).all()

    def get_first_or_default(self) -> list[Any]:
        if self.db.session.query(self.__class__).first() is None:
            self.set_default_values()
        return self.get_all()

    def set_default_values(self) -> None:
        pass
