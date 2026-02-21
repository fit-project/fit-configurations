from __future__ import annotations

import json
from pathlib import Path

import pytest

from fit_configurations import lang


@pytest.mark.unit
def test_load_translations_uses_requested_language(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(lang, "LANG_DIR", tmp_path)
    monkeypatch.setattr(lang, "DEFAULT_LANG", "en")

    (tmp_path / "en.json").write_text(json.dumps({"value": "default"}), encoding="utf-8")
    (tmp_path / "it.json").write_text(json.dumps({"value": "italiano"}), encoding="utf-8")

    loaded = lang.load_translations("it")

    assert loaded == {"value": "italiano"}


@pytest.mark.unit
def test_load_translations_falls_back_to_default(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(lang, "LANG_DIR", tmp_path)
    monkeypatch.setattr(lang, "DEFAULT_LANG", "en")
    monkeypatch.setattr(lang, "get_system_lang", lambda: "es")

    (tmp_path / "en.json").write_text(json.dumps({"fallback": True}), encoding="utf-8")

    loaded = lang.load_translations()

    assert loaded == {"fallback": True}
