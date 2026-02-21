from __future__ import annotations

import pytest
from PySide6 import QtCore, QtWidgets

from fit_configurations.view.configuration import Configuration


@pytest.fixture
def stable_general_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_platform", lambda: "lin"
    )
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_version", lambda: "1.2.3"
    )


@pytest.mark.e2e
def test_packet_capture_e2e_save_and_reload(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["fit_configurations.view.tabs.packet_capture.packet_capture"],
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.packet_capture.packet_capture.is_admin", lambda: True
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.packet_capture.packet_capture.get_platform", lambda: "lin"
    )

    dialog = Configuration()
    dialog.ui.enable_packet_capture_recorder.setChecked(True)
    dialog.ui.packet_capture_recorder_filename.setText("e2e-capture.pcap")
    dialog.ui.save_button.click()

    reloaded = Configuration()
    assert reloaded.ui.enable_packet_capture_recorder.isChecked() is True
    assert reloaded.ui.packet_capture_recorder_filename.text() == "e2e-capture.pcap"


@pytest.mark.e2e
def test_network_e2e_save_and_reload(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["fit_configurations.view.tabs.network.network"],
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.network.network.is_admin", lambda: True
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.network.network.get_platform", lambda: "lin"
    )

    dialog = Configuration()
    dialog.ui.whois.setChecked(False)
    dialog.ui.ntp_server.setText("pool.ntp.org")
    dialog.ui.nslookup_dns_server.setText("9.9.9.9")
    dialog.ui.nslookup_enable_tcp.setChecked(True)
    dialog.ui.save_button.click()

    reloaded = Configuration()
    assert reloaded.ui.whois.isChecked() is False
    assert reloaded.ui.ntp_server.text() == "pool.ntp.org"
    assert reloaded.ui.nslookup_dns_server.text() == "9.9.9.9"
    assert reloaded.ui.nslookup_enable_tcp.isChecked() is True


@pytest.mark.e2e
def test_timestamp_e2e_save_and_reload(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["fit_configurations.view.tabs.timestamp.timestamp"],
    )

    dialog = Configuration()
    dialog.ui.enable_timestamp.setChecked(True)
    dialog.ui.timestamp_server_name.setText("https://tsa.example.org")
    dialog.ui.timestamp_certificate_url.setText("https://tsa.example.org/cert.crt")
    dialog.ui.save_button.click()

    reloaded = Configuration()
    assert reloaded.ui.enable_timestamp.isChecked() is True
    assert reloaded.ui.timestamp_server_name.text() == "https://tsa.example.org"
    assert (
        reloaded.ui.timestamp_certificate_url.text()
        == "https://tsa.example.org/cert.crt"
    )


@pytest.mark.e2e
def test_pec_e2e_save_and_reload(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["fit_configurations.view.tabs.pec.pec"],
    )

    dialog = Configuration()
    dialog.ui.enable_pec.setChecked(True)
    dialog.ui.pec_email.setText("user@example.org")
    dialog.ui.pec_password.setText("pw")
    dialog.ui.pec_imap_server.setText("imap.example.org")
    dialog.ui.pec_imap_server_port.setText("993")
    dialog.ui.pec_smtp_server.setText("smtp.example.org")
    dialog.ui.pec_smtp_server_port.setText("465")
    dialog.ui.retries_eml_download.setText("4")
    dialog.ui.save_button.click()

    reloaded = Configuration()
    assert reloaded.ui.enable_pec.isChecked() is True
    assert reloaded.ui.pec_email.text() == "user@example.org"
    assert reloaded.ui.pec_imap_server.text() == "imap.example.org"
    assert reloaded.ui.pec_smtp_server.text() == "smtp.example.org"
    assert reloaded.ui.retries_eml_download.text() == "4"


class _FakeAudioSetting(QtCore.QObject):
    accepted = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()
        self.exec_calls = 0

    def exec(self) -> int:
        self.exec_calls += 1
        self.accepted.emit()
        return 0

    def enable_audio_recording(self):
        return True


@pytest.mark.e2e
def test_screen_recorder_e2e_save_and_reload(
    qapp: QtWidgets.QApplication,
    sqlite_db_path,
    monkeypatch: pytest.MonkeyPatch,
    stable_general_defaults,
) -> None:
    monkeypatch.setattr(
        "fit_configurations.view.configuration.TAB_MODULES",
        ["fit_configurations.view.tabs.screen_recorder.screen_recorder"],
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.screen_recorder.screen_recorder.get_platform",
        lambda: "macos",
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.screen_recorder.screen_recorder.AudioSetting",
        _FakeAudioSetting,
    )

    dialog = Configuration()
    dialog.ui.enable_screen_recorder.setChecked(True)
    dialog.ui.verify_audio_setting_button.click()
    dialog.ui.enable_audio_recording.setChecked(True)
    dialog.ui.screen_recorder_filename.setText("e2e-video.avi")
    dialog.ui.save_button.click()

    reloaded = Configuration()
    assert reloaded.ui.enable_screen_recorder.isChecked() is True
    assert reloaded.ui.screen_recorder_filename.text() == "e2e-video.avi"
