from __future__ import annotations

import pytest
from PySide6 import QtWidgets

from fit_configurations.view.tabs.tab import TabView


class FakeController:
    def __init__(self) -> None:
        self._configuration = {"id": 1, "value": "initial"}
        self.saved = None

    @property
    def configuration(self) -> dict:
        return self._configuration

    @configuration.setter
    def configuration(self, values: dict) -> None:
        self.saved = values


class DummyTab(TabView):
    controller_class = FakeController

    def init_ui(self) -> None:
        self.initialized = True

    def set_form_data(self, data: dict) -> None:
        self.last_set_data = data

    def collect_form_data(self) -> dict:
        return {"id": 1, "value": "updated"}


@pytest.mark.contract
def test_tab_view_initialization_and_accept_reject_contract(qapp: QtWidgets.QApplication) -> None:
    tab_widget = QtWidgets.QWidget()
    tab = DummyTab(tab_widget, "dummy")

    assert tab.initialized is True
    assert tab.last_set_data == {"id": 1, "value": "initial"}

    tab.accept()
    assert tab.controller.saved == {"id": 1, "value": "updated"}

    tab.last_set_data = {}
    tab.reject()
    assert tab.last_set_data == {"id": 1, "value": "initial"}
