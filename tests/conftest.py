from __future__ import annotations

from pathlib import Path

import pytest
from PySide6 import QtWidgets


@pytest.fixture(scope="session")
def qapp() -> QtWidgets.QApplication:
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication([])
    return app


@pytest.fixture
def sqlite_db_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    db_path = tmp_path / "configuration-test.db"

    def _resolve_db_path(_: str) -> str:
        return str(db_path)

    monkeypatch.setattr("fit_configurations.model.db.resolve_db_path", _resolve_db_path)
    return db_path
