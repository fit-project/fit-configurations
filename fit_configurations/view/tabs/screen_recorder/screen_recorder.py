#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_common.core import get_platform
from PySide6 import QtWidgets

from fit_configurations.controller.tabs.screen_recorder.screen_recorder import (
    ScreenRecorderController,
)
from fit_configurations.view.tabs.screen_recorder.audio_setting import AudioSetting
from fit_configurations.view.tabs.tab import TabView


class ScreenRecorderView(TabView):
    controller_class = ScreenRecorderController

    def init_ui(self):
        self.audio_setting = AudioSetting()
        self.audio_setting.accepted.connect(self._enable_audio_recording)

        # Widget
        self.enable_screen_recorder = self.find(
            QtWidgets.QCheckBox, "enable_screen_recorder"
        )
        self.enable_audio_recording = self.find(
            QtWidgets.QCheckBox, "enable_audio_recording"
        )
        self.audio_recording_box = self.find(QtWidgets.QFrame, "audio_recording_box")
        self.screen_recorder_filename = self.find(
            QtWidgets.QLineEdit, "screen_recorder_filename"
        )
        self.verify_audio_setting = self.find(
            QtWidgets.QPushButton, "verify_audio_setting_button"
        )
        self.temporary_msg = self.find(QtWidgets.QLabel, "temporary_msg_label")

        # Setup iniziale
        if get_platform() in ("lin", "other"):
            self.audio_recording_box.setVisible(False)

        self.temporary_msg.setVisible(False)

        # Signal
        self.enable_screen_recorder.stateChanged.connect(
            self._update_screen_recorder_state
        )
        self.enable_audio_recording.stateChanged.connect(
            self._on_audio_recording_changed
        )
        self.verify_audio_setting.clicked.connect(self._show_audio_setting)

    def _show_audio_setting(self):
        self.audio_setting.exec()

    def _enable_audio_recording(self):
        if (
            self.enable_screen_recorder.isChecked()
            and self.audio_setting.enable_audio_recording()
        ):
            self.verify_audio_setting.setEnabled(True)
            self.enable_audio_recording.setEnabled(True)
            app = QtWidgets.QApplication.instance()
            if hasattr(app, "is_enabled_audio_recording"):
                value = getattr(app, "is_enabled_audio_recording")
                self.enable_audio_recording.setChecked(value)
                self.temporary_msg.setVisible(value)
        else:
            self.enable_audio_recording.setEnabled(False)

    def _update_screen_recorder_state(self):
        enabled = self.enable_screen_recorder.isChecked()
        self.screen_recorder_filename.setEnabled(enabled)
        self.verify_audio_setting.setEnabled(enabled)
        self._enable_audio_recording()

    def _on_audio_recording_changed(self):
        app = QtWidgets.QApplication.instance()
        value = self.enable_audio_recording.isChecked()
        self.temporary_msg.setVisible(value)
        setattr(app, "is_enabled_audio_recording", value)

    def set_form_data(self, data):
        self.enable_screen_recorder.setChecked(data.get("enabled", False))
        self.screen_recorder_filename.setText(data.get("filename", ""))
        self._update_screen_recorder_state()
        self._enable_audio_recording()

    def collect_form_data(self):
        return {
            "id": self._configuration["id"],
            "enabled": self.enable_screen_recorder.isChecked(),
            "filename": self.screen_recorder_filename.text().strip(),
        }
