from __future__ import annotations

from types import SimpleNamespace

import pytest
from PySide6 import QtWidgets

from fit_configurations.view.configuration import Configuration


class FakeUiFitConfiguration:
    def setupUi(self, dialog: QtWidgets.QDialog) -> None:
        self.left_box = QtWidgets.QWidget(dialog)
        self.minimize_button = QtWidgets.QPushButton(dialog)
        self.close_button = QtWidgets.QPushButton(dialog)
        self.version = QtWidgets.QLabel(dialog)
        self.cancel_button = QtWidgets.QPushButton(dialog)
        self.save_button = QtWidgets.QPushButton(dialog)
        self.menu_tabs = QtWidgets.QTreeWidget(dialog)
        self.tabs = QtWidgets.QTabWidget(dialog)

        self.general = QtWidgets.QWidget(dialog)
        self.language = QtWidgets.QWidget(dialog)
        self.tabs.addTab(self.general, "general")
        self.tabs.addTab(self.language, "language")


class FakeGeneralView:
    __is_tab__ = True
    accept_calls = 0
    reject_calls = 0

    def __init__(self, tab: QtWidgets.QWidget, name: str) -> None:
        self.tab = tab
        self.name = name

    def accept(self) -> None:
        self.__class__.accept_calls += 1

    def reject(self) -> None:
        self.__class__.reject_calls += 1


class FakeLanguageView:
    __is_tab__ = True
    accept_calls = 0
    reject_calls = 0

    def __init__(self, tab: QtWidgets.QWidget, name: str) -> None:
        self.tab = tab
        self.name = name

    def accept(self) -> None:
        self.__class__.accept_calls += 1

    def reject(self) -> None:
        self.__class__.reject_calls += 1


class FakeGhostView:
    __is_tab__ = True

    def __init__(self, tab: QtWidgets.QWidget, name: str) -> None:
        self.tab = tab
        self.name = name


class NotATab:
    __is_tab__ = False


@pytest.mark.integration
def test_configuration_load_tabs_filters_modules_and_missing_ui(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("fit_configurations.view.configuration.Ui_fit_configuration", FakeUiFitConfiguration)
    monkeypatch.setattr("fit_configurations.view.configuration.translate_ui", lambda *_: None)
    monkeypatch.setattr("fit_configurations.view.configuration.get_version", lambda: "1.2.3")
    monkeypatch.setattr(
        "fit_configurations.view.configuration.load_translations",
        lambda: {"GENERAL": "General", "LANGUAGE": "Language", "GHOST": "Ghost"},
    )
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["ok_mod", "ghost_mod", "broken_mod"],
    )

    ok_mod = SimpleNamespace(GeneralView=FakeGeneralView, NotATab=NotATab)
    ghost_mod = SimpleNamespace(GhostView=FakeGhostView)

    def fake_import_module(modname: str):
        if modname == "ok_mod":
            return ok_mod
        if modname == "ghost_mod":
            return ghost_mod
        raise RuntimeError("broken")

    monkeypatch.setattr("fit_configurations.view.configuration.import_module", fake_import_module)

    config = Configuration()

    assert config.ui.version.text() == "v1.2.3"
    assert config.ui.menu_tabs.topLevelItemCount() == 1
    assert config.ui.menu_tabs.topLevelItem(0).text(0) == "General"
    assert len(config._Configuration__tabs) == 1


@pytest.mark.integration
def test_configuration_accept_reject_forwarded_to_each_tab(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    FakeGeneralView.accept_calls = 0
    FakeGeneralView.reject_calls = 0
    FakeLanguageView.accept_calls = 0
    FakeLanguageView.reject_calls = 0

    monkeypatch.setattr("fit_configurations.view.configuration.Ui_fit_configuration", FakeUiFitConfiguration)
    monkeypatch.setattr("fit_configurations.view.configuration.translate_ui", lambda *_: None)
    monkeypatch.setattr("fit_configurations.view.configuration.get_version", lambda: "1.2.3")
    monkeypatch.setattr(
        "fit_configurations.view.configuration.load_translations",
        lambda: {"GENERAL": "General", "LANGUAGE": "Language"},
    )
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["ok_mod"],
    )

    ok_mod = SimpleNamespace(GeneralView=FakeGeneralView, LanguageView=FakeLanguageView)
    monkeypatch.setattr(
        "fit_configurations.view.configuration.import_module", lambda _modname: ok_mod
    )

    config = Configuration()
    config.accept()
    config.reject()

    assert FakeGeneralView.accept_calls == 1
    assert FakeLanguageView.accept_calls == 1
    assert FakeGeneralView.reject_calls == 1
    assert FakeLanguageView.reject_calls == 1
