from __future__ import annotations

import pytest

from fit_configurations.controller.tabs.general.general import GeneralController


@pytest.mark.integration
def test_general_controller_persists_configuration(
    sqlite_db_path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_platform", lambda: "lin"
    )
    monkeypatch.setattr(
        "fit_configurations.model.tabs.general.general.get_version", lambda: "9.9.9"
    )

    controller = GeneralController()
    current = controller.configuration

    assert current["id"] > 0
    assert current["cases_folder_path"] == "~/Documents/FIT"
    assert "FreezingInternetTool/9.9.9" in current["user_agent"]

    controller.configuration = {
        "id": current["id"],
        "cases_folder_path": "/tmp/cases",
        "home_page_url": "https://example.org/",
        "language": "english",
        "user_agent": "custom-agent",
    }

    reloaded = GeneralController().configuration

    assert reloaded["cases_folder_path"] == "/tmp/cases"
    assert reloaded["home_page_url"] == "https://example.org/"
    assert reloaded["user_agent"] == "custom-agent"
