from __future__ import annotations

import pytest
from PySide6 import QtCore, QtWidgets

from fit_configurations.view.tabs.screen_recorder.screen_recorder import ScreenRecorderView


class FakeController:
    saved_configuration: dict | None = None

    def __init__(self) -> None:
        self._configuration = {"id": 5, "enabled": True, "filename": "video.avi"}

    @property
    def configuration(self) -> dict:
        return dict(self._configuration)

    @configuration.setter
    def configuration(self, values: dict) -> None:
        self.__class__.saved_configuration = dict(values)


class FakeAudioSetting(QtCore.QObject):
    accepted = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()
        self.exec_calls = 0
        self._enabled_audio = True

    def exec(self) -> int:
        self.exec_calls += 1
        self.accepted.emit()
        return 0

    def enable_audio_recording(self):
        return self._enabled_audio


def _w(name: str, widget: QtWidgets.QWidget) -> QtWidgets.QWidget:
    widget.setObjectName(name)
    return widget


def _build_screen_tab() -> QtWidgets.QWidget:
    tab = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(tab)
    layout.addWidget(_w("enable_screen_recorder", QtWidgets.QCheckBox(tab)))
    layout.addWidget(_w("enable_audio_recording", QtWidgets.QCheckBox(tab)))
    layout.addWidget(_w("audio_recording_box", QtWidgets.QFrame(tab)))
    layout.addWidget(_w("screen_recorder_filename", QtWidgets.QLineEdit(tab)))
    layout.addWidget(_w("verify_audio_setting_button", QtWidgets.QPushButton(tab)))
    layout.addWidget(_w("temporary_msg_label", QtWidgets.QLabel(tab)))
    return tab


@pytest.mark.integration
def test_screen_recorder_view_flow(
    qapp: QtWidgets.QApplication, monkeypatch: pytest.MonkeyPatch
) -> None:
    FakeController.saved_configuration = None

    monkeypatch.setattr(ScreenRecorderView, "controller_class", FakeController)
    monkeypatch.setattr(
        "fit_configurations.view.tabs.screen_recorder.screen_recorder.AudioSetting",
        FakeAudioSetting,
    )
    monkeypatch.setattr(
        "fit_configurations.view.tabs.screen_recorder.screen_recorder.get_platform",
        lambda: "macos",
    )

    view = ScreenRecorderView(_build_screen_tab(), "Screen")

    assert view.enable_screen_recorder.isChecked() is True
    assert view.screen_recorder_filename.isEnabled() is True

    view.verify_audio_setting.click()
    assert view.audio_setting.exec_calls == 1
    assert view.enable_audio_recording.isEnabled() is True

    view.enable_audio_recording.setChecked(True)
    assert view.temporary_msg.isHidden() is False

    view.screen_recorder_filename.setText(" capture.avi ")
    view.accept()

    assert FakeController.saved_configuration == {
        "id": 5,
        "enabled": True,
        "filename": "capture.avi",
    }
