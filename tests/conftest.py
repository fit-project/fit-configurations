from __future__ import annotations

import gc
import sys
from pathlib import Path

import pytest
from PySide6 import QtWidgets


def _add_local_venv_site_packages() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    site_packages = repo_root / ".venv" / "lib" / py_version / "site-packages"
    if site_packages.exists():
        sys.path.insert(0, str(site_packages))


_add_local_venv_site_packages()


def pytest_ignore_collect(collection_path: Path, config: pytest.Config) -> bool:
    markexpr = (config.option.markexpr or "").strip()
    if markexpr != "unit":
        return False

    normalized = collection_path.as_posix().rstrip("/")
    if normalized.endswith("tests") or normalized.endswith("tests/unit"):
        return False
    return "tests/unit/" not in normalized


@pytest.fixture(scope="session")
def qapp() -> QtWidgets.QApplication:
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication([])
    yield app
    # Explicit Qt teardown reduces sporadic crashes at interpreter shutdown in CI.
    app.closeAllWindows()
    app.processEvents()
    app.quit()
    app.processEvents()
    gc.collect()


@pytest.fixture
def sqlite_db_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    db_path = tmp_path / "configuration-test.db"

    def _resolve_db_path(_: str) -> str:
        return str(db_path)

    monkeypatch.setattr("fit_configurations.model.db.resolve_db_path", _resolve_db_path)
    return db_path
