#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaDevices

from fit_common.gui.clickable_label import ClickableLabel as ClickableLabelView
from fit_common.core.utility import is_cmd, resolve_path
from fit_configurations.lang import load_translations
from fit_configurations.view.tabs.screenrecorder.audio_setting_ui import (
    Ui_audio_recording_checker_dialog,
)

from fit_assets import resources


class AudioSetting(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.translations = load_translations()

        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui = Ui_audio_recording_checker_dialog()
        self.ui.setupUi(self)

        __icon_green = QPixmap(":/icons/icons/green-mark.png").scaled(20, 20)
        __icon_red = QPixmap(":/icons/icons/red-mark.png").scaled(20, 20)

        self.ui.ok_button.clicked.connect(self.accept)

        if self.is_installed_ffmpeg():
            self.ui.ffmpeg_installed_img.setPixmap(__icon_green)
            self.ui.ffmpeg_installed_msg.setText(self.translations["FFMPEG_INSTALLED"])
        else:
            self.ui.ffmpeg_installed_img.setPixmap(__icon_red)
            self.ui.ffmpeg_installed_msg.setText(
                self.translations["FFMPEG_NOT_INSTALLED"]
            )

        if self.get_vb_cable_virtual_audio_device() is not None:
            self.ui.vb_cable_installed_img.setPixmap(__icon_green)
            self.ui.vb_cable_installed_msg.setText(
                self.translations["VB_CABLE_INSTALLED"]
            )
            self.ui.vb_cable_box_first_output_audio_device.setVisible(True)
        else:
            self.ui.vb_cable_installed_img.setPixmap(__icon_red)
            self.ui.vb_cable_installed_msg.setText(
                self.translations["VB_CABLE_INSTALLED"]
            )
            self.ui.vb_cable_box_first_output_audio_device.setVisible(False)

        if self.is_vb_cable_first_ouput_audio_device():
            self.ui.vb_cable_first_output_audio_device_img.setPixmap(__icon_green)
            self.ui.vb_cable_first_output_audio_device_msg.setText(
                self.translations["VB_CABLE_FIRST_OUPUT_AUDIO_DEVICE"]
            )
        else:
            self.ui.vb_cable_first_output_audio_device_img.setPixmap(__icon_red)
            self.ui.vb_cable_first_output_audio_device_msg.setText(
                self.translations["VB_CABLE_NOT_FIRST_OUPUT_AUDIO_DEVICE"]
            )

        self.ui.guide_link.addWidget(
            ClickableLabelView(
                self.translations["AUDIO_RECORDING_MANAGEMENT_GUIDE_URL"],
                self.translations["AUDIO_RECORDING_MANAGEMENT_GUIDE"],
            )
        )

    def is_installed_ffmpeg(self):
        return is_cmd("ffmpeg")

    def get_vb_cable_virtual_audio_device(self):
        for dev in QMediaDevices().audioInputs():
            if any(
                x in dev.description()
                for x in ["Virtual Cable", "CABLE Output", "VB-Audio", "VB-Cable"]
            ):
                return dev
        return None

    def is_vb_cable_first_ouput_audio_device(self):
        for idx, dev in enumerate(QMediaDevices().audioOutputs()):
            if any(
                x in dev.description()
                for x in ["Virtual Cable", "CABLE Output", "VB-Audio", "VB-Cable"]
            ):
                return idx == 0
        return False

    def enable_audio_recording(self):
        return (
            self.is_installed_ffmpeg()
            and self.get_vb_cable_virtual_audio_device()
            and self.is_vb_cable_first_ouput_audio_device()
        )
