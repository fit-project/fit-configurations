from __future__ import annotations

import pytest

from fit_configurations.controller.tabs.general.legal_proceeding_type import (
    LegalProceedingTypeController,
)
from fit_configurations.model.tabs.general.general import GeneralModel
from fit_configurations.model.tabs.language.language import LanguageModel
from fit_configurations.model.tabs.network.network_check import NetworkCheckModel
from fit_configurations.model.tabs.network.network_tool import NetworkToolModel
from fit_configurations.model.tabs.packet_capture.packet_capture import PacketCaptureModel
from fit_configurations.model.tabs.pec.pec import PecModel
from fit_configurations.model.tabs.screen_recorder.screen_recorder import (
    ScreenRecorderModel,
)
from fit_configurations.model.tabs.timestamp.timestamp import TimestampModel


@pytest.mark.integration
def test_model_defaults_for_all_tabs(sqlite_db_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_platform", lambda: "lin"
    )
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_version", lambda: "1.0.0"
    )

    models = [
        GeneralModel(),
        LanguageModel(),
        NetworkToolModel(),
        NetworkCheckModel(),
        PacketCaptureModel(),
        PecModel(),
        ScreenRecorderModel(),
        TimestampModel(),
    ]

    for model in models:
        rows = model.get_first_or_default()
        assert len(rows) == 1

    general_row = GeneralModel().get_first_or_default()[0]
    assert general_row.cases_folder_path == "~/Documents/FIT"
    assert general_row.home_page_url == "http://fit-project.org/"
    assert "FreezingInternetTool/1.0.0" in general_row.user_agent

    language_row = LanguageModel().get_first_or_default()[0]
    assert language_row.language == "Italian"

    network_tool_row = NetworkToolModel().get_first_or_default()[0]
    assert all(
        [
            network_tool_row.whois,
            network_tool_row.headers,
            network_tool_row.traceroute,
            network_tool_row.ssl_keylog,
            network_tool_row.nslookup,
            network_tool_row.ssl_certificate,
        ]
    )

    network_check_row = NetworkCheckModel().get_first_or_default()[0]
    assert network_check_row.ntp_server == "ntp1.inrim.it"
    assert network_check_row.nslookup_dns_server == "1.1.1.1"

    packet_row = PacketCaptureModel().get_first_or_default()[0]
    assert packet_row.enabled is True
    assert packet_row.filename == "acquisition.pcap"

    pec_row = PecModel().get_first_or_default()[0]
    assert pec_row.enabled is False
    assert pec_row.retries == 5

    recorder_row = ScreenRecorderModel().get_first_or_default()[0]
    assert recorder_row.enabled is True
    assert recorder_row.filename == "acquisition_video"

    timestamp_row = TimestampModel().get_first_or_default()[0]
    assert timestamp_row.enabled is True
    assert timestamp_row.server_name == "https://freetsa.org/tsr"


@pytest.mark.integration
def test_models_update_roundtrip(sqlite_db_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_platform", lambda: "lin"
    )
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_version", lambda: None
    )

    model = TimestampModel()
    row = model.get_first_or_default()[0]

    model.update({
        "id": row.id,
        "enabled": False,
        "server_name": "https://tsa.example.org",
        "cert_url": "https://tsa.example.org/cert.crt",
    })

    updated = TimestampModel().get_first_or_default()[0]
    assert updated.enabled is False
    assert updated.server_name == "https://tsa.example.org"
    assert updated.cert_url == "https://tsa.example.org/cert.crt"


@pytest.mark.integration
def test_legal_proceeding_type_controller_names_add_and_delete(
    sqlite_db_path,
) -> None:
    controller = LegalProceedingTypeController()

    assert controller.get_proceeding_name_by_id(-1) == "N/A"
    assert controller.names == ["Civile", "Extragiudiziale", "Penale"]

    controller.names = ["Penale", "Nuova"]

    names_after = [p["name"] for p in LegalProceedingTypeController().proceedings]
    assert sorted(names_after) == ["Nuova", "Penale"]
