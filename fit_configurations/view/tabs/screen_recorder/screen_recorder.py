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
from fit_configurations.view.tabs.tab import TabView


class ScreenRecorderView(TabView):
    controller_class = ScreenRecorderController

    def init_ui(self):
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

        # Setup iniziale
        if get_platform() in ("lin", "other"):
            self.audio_recording_box.setVisible(False)

        # Signal
        self.enable_screen_recorder.stateChanged.connect(
            self._update_screen_recorder_state
        )

    def _update_screen_recorder_state(self):
        enabled = self.enable_screen_recorder.isChecked()
        self.screen_recorder_filename.setEnabled(enabled)
        self.enable_audio_recording.setEnabled(enabled)

    def set_form_data(self, data):
        self.enable_screen_recorder.setChecked(data.get("enabled_video", False))
        self.enable_audio_recording.setChecked(data.get("enabled_audio", False))
        self.screen_recorder_filename.setText(data.get("filename", ""))
        self._update_screen_recorder_state()

    def collect_form_data(self):
        return {
            "id": self._configuration["id"],
            "enabled_video": self.enable_screen_recorder.isChecked(),
            "enabled_audio": self.enable_audio_recording.isChecked(),
            "filename": self.screen_recorder_filename.text().strip(),
        }
