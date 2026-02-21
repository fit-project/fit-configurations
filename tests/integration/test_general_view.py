from __future__ import annotations

import pytest
from PySide6 import QtWidgets

from fit_configurations.view.tabs.general.general import GeneralView


class FakeGeneralController:
    saved_configuration: dict | None = None

    def __init__(self) -> None:
        self._configuration = {
            "id": 7,
            "cases_folder_path": "/start/cases",
            "home_page_url": "https://fit-project.org/",
            "language": "english",
            "user_agent": "initial-agent",
        }

    @property
    def configuration(self) -> dict:
        return self._configuration

    @configuration.setter
    def configuration(self, values: dict) -> None:
        self.__class__.saved_configuration = values


class FakeLegalProceedingTypeController:
    shared_names = ["Civile", "Penale"]

    @property
    def names(self) -> list[str]:
        return self.__class__.shared_names

    @names.setter
    def names(self, values: list[str]) -> None:
        self.__class__.shared_names = values


class FakeClickableLabel(QtWidgets.QLabel):
    def __init__(self, link: str, label: str) -> None:
        super().__init__(label)
        self.link = link


def _build_general_tab_widget() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    root_layout = QtWidgets.QVBoxLayout(tab)

    cases_folder_path = QtWidgets.QLineEdit(tab)
    cases_folder_path.setObjectName("cases_folder_path")
    root_layout.addWidget(cases_folder_path)

    cases_folder_button = QtWidgets.QPushButton(tab)
    cases_folder_button.setObjectName("cases_folder_button")
    root_layout.addWidget(cases_folder_button)

    home_page_url = QtWidgets.QLineEdit(tab)
    home_page_url.setObjectName("home_page_url")
    root_layout.addWidget(home_page_url)

    user_agent = QtWidgets.QPlainTextEdit(tab)
    user_agent.setObjectName("user_agent")
    root_layout.addWidget(user_agent)

    user_agent_button = QtWidgets.QPushButton(tab)
    user_agent_button.setObjectName("user_agent_button")
    root_layout.addWidget(user_agent_button)

    user_agent_layout_widget = QtWidgets.QWidget(tab)
    user_agent_layout = QtWidgets.QVBoxLayout(user_agent_layout_widget)
    user_agent_layout.setObjectName("user_agent_layout")
    root_layout.addWidget(user_agent_layout_widget)

    types_proceedings = QtWidgets.QPlainTextEdit(tab)
    types_proceedings.setObjectName("types_proceedings")
    root_layout.addWidget(types_proceedings)

    db_path = QtWidgets.QLineEdit(tab)
    db_path.setObjectName("db_path")
    root_layout.addWidget(db_path)

    return tab


@pytest.mark.integration
def test_general_view_collects_and_applies_form_data(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    FakeGeneralController.saved_configuration = None
    FakeLegalProceedingTypeController.shared_names = ["Civile", "Penale"]

    monkeypatch.setattr(GeneralView, "controller_class", FakeGeneralController)
    monkeypatch.setattr(
        "fit_configurations.view.tabs.general.general.LegalProceedingTypeController",
        FakeLegalProceedingTypeController,
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.general.general.load_translations",
        lambda: {
            "USER_AGENT_SITE": "https://example.org/ua",
            "USER_AGENT_SITE_LABEL": "ua label",
            "SELECT_CASE_FOLDER": "Select",
            "DEFAULT_USER_AGENT": "default ua",
        },
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.general.general.resolve_db_path",
        lambda _: "/tmp/configurations.db",
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.general.general.ClickableLabelView",
        FakeClickableLabel,
    )

    tab = _build_general_tab_widget()
    view = GeneralView(tab, "General")

    assert view.cases_folder_path.text() == "/start/cases"
    assert view.types_proceedings.toPlainText() == "Civile,Penale"

    view.cases_folder_path.setText("/new/cases")
    view.home_page_url.setText("https://example.org")
    view.user_agent.setPlainText("ua-test")
    view.types_proceedings.setPlainText("A,B")

    view.accept()

    assert FakeGeneralController.saved_configuration == {
        "id": 7,
        "cases_folder_path": "/new/cases",
        "home_page_url": "https://example.org",
        "language": "english",
        "user_agent": "ua-test",
    }
    assert FakeLegalProceedingTypeController.shared_names == ["A", "B"]
