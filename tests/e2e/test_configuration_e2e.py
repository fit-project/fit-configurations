from __future__ import annotations

import pytest
from PySide6 import QtWidgets

from fit_configurations.view.configuration import Configuration


@pytest.fixture
def e2e_tab_modules(monkeypatch: pytest.MonkeyPatch) -> None:
    # Keep real UI/controller/model flow while limiting optional external dependencies.
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        [
            "fit_configurations.view.tabs.general.general",
            "fit_configurations.view.tabs.language.language",
        ],
    )


@pytest.fixture
def stable_general_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_platform", lambda: "lin"
    )
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_version", lambda: "1.2.3"
    )


@pytest.mark.e2e
def test_configuration_e2e_save_persists_between_dialog_instances(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    e2e_tab_modules,
    stable_general_defaults,
) -> None:
    dialog = Configuration()

    assert dialog.ui.menu_tabs.topLevelItemCount() == 2

    dialog.ui.cases_folder_path.setText("/tmp/e2e-cases")
    dialog.ui.home_page_url.setText("https://example.org/home")
    dialog.ui.user_agent.setPlainText("e2e-agent")
    dialog.ui.report_language.setCurrentText("English")

    dialog.ui.save_button.click()

    assert dialog.result() == QtWidgets.QDialog.DialogCode.Accepted

    reloaded = Configuration()

    assert reloaded.ui.cases_folder_path.text() == "/tmp/e2e-cases"
    assert reloaded.ui.home_page_url.text() == "https://example.org/home"
    assert reloaded.ui.user_agent.toPlainText() == "e2e-agent"
    assert reloaded.ui.report_language.currentText() == "English"


@pytest.mark.e2e
def test_configuration_e2e_cancel_does_not_persist_changes(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    e2e_tab_modules,
    stable_general_defaults,
) -> None:
    initial = Configuration()
    initial.ui.cases_folder_path.setText("/tmp/initial")
    initial.ui.home_page_url.setText("https://example.org/initial")
    initial.ui.save_button.click()
    assert initial.result() == QtWidgets.QDialog.DialogCode.Accepted

    cancel_dialog = Configuration()
    cancel_dialog.ui.cases_folder_path.setText("/tmp/cancelled")
    cancel_dialog.ui.home_page_url.setText("https://example.org/cancelled")
    cancel_dialog.ui.cancel_button.click()

    assert cancel_dialog.result() == QtWidgets.QDialog.DialogCode.Rejected

    reloaded = Configuration()
    assert reloaded.ui.cases_folder_path.text() == "/tmp/initial"
    assert reloaded.ui.home_page_url.text() == "https://example.org/initial"


@pytest.mark.e2e
def test_configuration_e2e_menu_click_changes_current_tab(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    e2e_tab_modules,
    stable_general_defaults,
) -> None:
    dialog = Configuration()

    assert dialog.ui.tabs.currentIndex() == 0

    language_item = dialog.ui.menu_tabs.topLevelItem(1)
    dialog.ui.menu_tabs.itemClicked.emit(language_item, 0)

    assert dialog.ui.tabs.currentIndex() == 1


@pytest.mark.e2e
def test_configuration_e2e_cross_tab_save_persists_combined_state(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        [
            "fit_configurations.view.tabs.general.general",
            "fit_configurations.view.tabs.language.language",
            "fit_configurations.view.tabs.timestamp.timestamp",
            "fit_configurations.view.tabs.packet_capture.packet_capture",
        ],
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.packet_capture.packet_capture.is_admin",
        lambda: True,
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.packet_capture.packet_capture.get_platform",
        lambda: "lin",
    )

    dialog = Configuration()

    dialog.ui.cases_folder_path.setText("/tmp/cross-cases")
    dialog.ui.home_page_url.setText("https://example.org/cross")
    dialog.ui.user_agent.setPlainText("cross-agent")
    dialog.ui.report_language.setCurrentText("English")
    dialog.ui.enable_timestamp.setChecked(True)
    dialog.ui.timestamp_server_name.setText("https://tsa.cross")
    dialog.ui.timestamp_certificate_url.setText("https://tsa.cross/cert.crt")
    dialog.ui.enable_packet_capture_recorder.setChecked(True)
    dialog.ui.packet_capture_recorder_filename.setText("cross.pcap")

    dialog.ui.save_button.click()

    reloaded = Configuration()
    assert reloaded.ui.cases_folder_path.text() == "/tmp/cross-cases"
    assert reloaded.ui.home_page_url.text() == "https://example.org/cross"
    assert reloaded.ui.user_agent.toPlainText() == "cross-agent"
    assert reloaded.ui.report_language.currentText() == "English"
    assert reloaded.ui.enable_timestamp.isChecked() is True
    assert reloaded.ui.timestamp_server_name.text() == "https://tsa.cross"
    assert reloaded.ui.timestamp_certificate_url.text() == "https://tsa.cross/cert.crt"
    assert reloaded.ui.enable_packet_capture_recorder.isChecked() is True
    assert reloaded.ui.packet_capture_recorder_filename.text() == "cross.pcap"


@pytest.mark.e2e
def test_configuration_e2e_cross_tab_cancel_does_not_persist(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        [
            "fit_configurations.view.tabs.general.general",
            "fit_configurations.view.tabs.language.language",
            "fit_configurations.view.tabs.timestamp.timestamp",
        ],
    )

    baseline = Configuration()
    baseline.ui.cases_folder_path.setText("/tmp/baseline")
    baseline.ui.report_language.setCurrentText("Italian")
    baseline.ui.enable_timestamp.setChecked(False)
    baseline.ui.save_button.click()

    cancelled = Configuration()
    cancelled.ui.cases_folder_path.setText("/tmp/cancel-cross")
    cancelled.ui.report_language.setCurrentText("English")
    cancelled.ui.enable_timestamp.setChecked(True)
    cancelled.ui.timestamp_server_name.setText("https://tsa.cancel")
    cancelled.ui.cancel_button.click()
    assert cancelled.result() == QtWidgets.QDialog.DialogCode.Rejected

    reloaded = Configuration()
    assert reloaded.ui.cases_folder_path.text() == "/tmp/baseline"
    assert reloaded.ui.report_language.currentText() == "Italian"
    assert reloaded.ui.enable_timestamp.isChecked() is False
