from __future__ import annotations

import imaplib
import smtplib

import pytest
from PySide6 import QtWidgets

from fit_configurations.view.tabs.language.language import LanguageView
from fit_configurations.view.tabs.network.network import NetworkView
from fit_configurations.view.tabs.packet_capture.packet_capture import PacketCaptureView
from fit_configurations.view.tabs.pec.pec import PecView
from fit_configurations.view.tabs.timestamp.timestamp import TimestampView


class FakeController:
    saved_configuration: dict | None = None

    def __init__(self, initial: dict) -> None:
        self._configuration = dict(initial)

    @property
    def configuration(self) -> dict:
        return dict(self._configuration)

    @configuration.setter
    def configuration(self, values: dict) -> None:
        self.__class__.saved_configuration = dict(values)


class FakeNetworkToolController(FakeController):
    saved_configuration: dict | None = None

    def __init__(self) -> None:
        super().__init__(
            {
                "id": 1,
                "whois": True,
                "headers": True,
                "traceroute": True,
                "ssl_keylog": False,
                "nslookup": True,
                "ssl_certificate": False,
            }
        )


class FakeNetworkCheckController(FakeController):
    saved_configuration: dict | None = None

    def __init__(self) -> None:
        super().__init__(
            {
                "id": 1,
                "ntp_server": "ntp1.example.org",
                "nslookup_dns_server": "1.1.1.1",
                "nslookup_enable_tcp": False,
                "nslookup_enable_verbose_mode": True,
            }
        )


class FakeClickableLabel(QtWidgets.QLabel):
    def __init__(self, _link: str, label: str) -> None:
        super().__init__(label)


def _w(name: str, widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
    widget.setObjectName(name)
    return widget


def _build_language_tab() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    combo = _w("report_language", QtWidgets.QComboBox(tab))
    combo.setEditable(True)
    QtWidgets.QVBoxLayout(tab).addWidget(combo)
    return tab


def _build_packet_capture_tab() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(tab)
    layout.addWidget(_w("enable_packet_capture_recorder", QtWidgets.QCheckBox(tab)))
    layout.addWidget(_w("packet_capture_recorder_filename", QtWidgets.QLineEdit(tab)))
    return tab


def _build_timestamp_tab() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(tab)
    layout.addWidget(_w("enable_timestamp", QtWidgets.QCheckBox(tab)))
    layout.addWidget(_w("timestamp_server_name", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("timestamp_certificate_url", QtWidgets.QLineEdit(tab)))
    frame = _w("timestamp_settings", QtWidgets.QFrame(tab))
    layout.addWidget(frame)
    return tab


def _build_network_tab() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(tab)
    checkbox_names = [
        "whois",
        "headers",
        "traceroute",
        "ssl_keylog",
        "nslookup",
        "ssl_certificate",
        "nslookup_enable_tcp",
        "nslookup_enable_verbose_mode",
    ]
    for name in checkbox_names:
        layout.addWidget(_w(name, QtWidgets.QCheckBox(tab)))

    layout.addWidget(_w("ntp_server", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("nslookup_dns_server", QtWidgets.QLineEdit(tab)))
    return tab


def _build_pec_tab() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(tab)
    layout.addWidget(_w("enable_pec", QtWidgets.QCheckBox(tab)))
    layout.addWidget(_w("pec_settings", QtWidgets.QFrame(tab)))
    layout.addWidget(_w("pec_email", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("pec_password", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("retries_eml_download", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("pec_imap_server", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("pec_imap_server_port", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("pec_smtp_server", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("pec_smtp_server_port", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("verification_imap_button", QtWidgets.QPushButton(tab)))
    layout.addWidget(_w("verification_smtp_button", QtWidgets.QPushButton(tab)))
    layout.addWidget(_w("info_imap_img_label", QtWidgets.QLabel(tab)))
    layout.addWidget(_w("info_smtp_img_label", QtWidgets.QLabel(tab)))

    label_host = _w("enable_pec_layout", QtWidgets.QWidget(tab))
    link_layout = QtWidgets.QHBoxLayout()
    link_layout.setObjectName("enable_pec_layout")
    label_host.setLayout(link_layout)
    layout.addWidget(label_host)
    return tab


@pytest.mark.integration
def test_language_view_collects_current_language(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    class FakeLanguageController(FakeController):
        saved_configuration: dict | None = None

        def __init__(self) -> None:
            super().__init__({"id": 1, "language": "Italian"})

    monkeypatch.setattr(LanguageView, "controller_class", FakeLanguageController)
    monkeypatch.setattr(
        "fit_configurations.view.tabs.language.language.load_translations",
        lambda: {"ITALIAN": "Italian", "ENGLISH": "English", "REPORT_LANGUAGE": "Report language"},
    )

    view = LanguageView(_build_language_tab(), "Language")
    view.report_language.setCurrentText("English")
    view.accept()

    assert FakeLanguageController.saved_configuration == {"id": 1, "language": "English"}


@pytest.mark.integration
def test_packet_capture_view_applies_admin_rules_and_collects_data(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    class FakePacketController(FakeController):
        saved_configuration: dict | None = None

        def __init__(self) -> None:
            super().__init__({"id": 9, "enabled": True, "filename": "cap.pcap"})

    monkeypatch.setattr(PacketCaptureView, "controller_class", FakePacketController)
    monkeypatch.setattr(
        "fit_configurations.view.tabs.packet_capture.packet_capture.is_admin", lambda: False
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.packet_capture.packet_capture.get_platform", lambda: "lin"
    )

    view = PacketCaptureView(_build_packet_capture_tab(), "Packet")

    assert view.enable_checkbox.isEnabled() is False
    assert view.filename_input.isEnabled() is False

    view.enable_checkbox.setChecked(True)
    view.filename_input.setText(" new_name.pcap ")
    view.accept()

    assert FakePacketController.saved_configuration == {
        "id": 9,
        "enabled": True,
        "filename": "new_name.pcap",
    }


@pytest.mark.integration
def test_timestamp_view_toggle_and_collect(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    class FakeTimestampController(FakeController):
        saved_configuration: dict | None = None

        def __init__(self) -> None:
            super().__init__(
                {
                    "id": 4,
                    "enabled": False,
                    "server_name": "",
                    "cert_url": "",
                }
            )

    monkeypatch.setattr(TimestampView, "controller_class", FakeTimestampController)

    view = TimestampView(_build_timestamp_tab(), "Timestamp")
    assert view.timestamp_settings.isEnabled() is False

    view.enable_timestamp.setChecked(True)
    view.timestamp_server_name.setText(" https://tsa.example.org ")
    view.timestamp_certificate_url.setText(" https://tsa.example.org/cert.crt ")
    view.accept()

    assert FakeTimestampController.saved_configuration == {
        "id": 4,
        "enabled": True,
        "server_name": "https://tsa.example.org",
        "cert_url": "https://tsa.example.org/cert.crt",
    }


@pytest.mark.integration
def test_network_view_collect_and_accept(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    FakeNetworkToolController.saved_configuration = None
    FakeNetworkCheckController.saved_configuration = None

    monkeypatch.setattr(
        "fit_configurations.view.tabs.network.network.NetworkToolController",
        FakeNetworkToolController,
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.network.network.NetworkCheckController",
        FakeNetworkCheckController,
    )
    monkeypatch.setattr("fit_configurations.view.tabs.network.network.is_admin", lambda: True)
    monkeypatch.setattr("fit_configurations.view.tabs.network.network.get_platform", lambda: "lin")

    view = NetworkView(_build_network_tab(), "Network")

    view.whois.setChecked(False)
    view.nslookup_dns_server.setText("9.9.9.9")
    view.nslookup_enable_tcp.setChecked(True)
    view.accept()

    assert FakeNetworkToolController.saved_configuration is not None
    assert FakeNetworkToolController.saved_configuration["whois"] is False
    assert FakeNetworkCheckController.saved_configuration is not None
    assert FakeNetworkCheckController.saved_configuration["nslookup_dns_server"] == "9.9.9.9"
    assert FakeNetworkCheckController.saved_configuration["nslookup_enable_tcp"] is True


@pytest.mark.integration
def test_pec_view_collect_and_verify_error_paths(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    class FakePecController(FakeController):
        saved_configuration: dict | None = None

        def __init__(self) -> None:
            super().__init__(
                {
                    "id": 2,
                    "enabled": True,
                    "pec_email": "user@example.org",
                    "password": "pwd",
                    "smtp_server": "smtp.example.org",
                    "smtp_port": "465",
                    "imap_server": "imap.example.org",
                    "imap_port": "993",
                    "retries": 3,
                }
            )

    calls: list[tuple[str, str, str, str]] = []

    class FakeErrorView:
        def __init__(self, _icon, title: str, subtitle: str, msg: str) -> None:
            calls.append(("ctor", title, subtitle, msg))

        def exec(self) -> None:
            calls.append(("exec", "", "", ""))

    monkeypatch.setattr(PecView, "controller_class", FakePecController)
    monkeypatch.setattr(
        "fit_configurations.view.tabs.pec.pec.load_translations",
        lambda: {
            "TWO_FACTOR_AUTH_URL": "https://example.org/2fa",
            "TWO_FACTOR_AUTH": "2fa guide",
            "LOGIN_FAILED": "Login failed",
            "LOGIN_ERROR": "Wrong login credentials",
        },
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.pec.pec.ClickableLabelView",
        FakeClickableLabel,
    )
    monkeypatch.setattr("fit_configurations.view.tabs.pec.pec.ErrorView", FakeErrorView)

    def fail_imap(_server: str, _port: int):
        raise imaplib.IMAP4.error("imap failed")

    def fail_smtp(_server: str, _port: int):
        raise smtplib.SMTPException("smtp failed")

    monkeypatch.setattr("fit_configurations.view.tabs.pec.pec.imaplib.IMAP4_SSL", fail_imap)
    monkeypatch.setattr("fit_configurations.view.tabs.pec.pec.smtplib.SMTP_SSL", fail_smtp)

    view = PecView(_build_pec_tab(), "PEC")

    assert view.pec_settings.isEnabled() is True

    view.verification_imap_button.click()
    view.verification_smtp_button.click()
    assert view.info_imap_img.isHidden() is False
    assert view.info_smtp_img.isHidden() is False
    assert any(item[0] == "exec" for item in calls)

    view.retries_eml_download.setText("7")
    data = view.collect_form_data()
    assert data["id"] == 2
    assert data["retries"] == 7
