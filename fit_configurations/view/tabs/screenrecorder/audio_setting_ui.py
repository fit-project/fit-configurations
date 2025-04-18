#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: GPL-3.0-only
# -----
######

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


from fit_configurations.lang import load_translations


class Ui_audio_recording_checker_dialog(object):
    def setupUi(self, audio_recording_checker_dialog):
        if not audio_recording_checker_dialog.objectName():
            audio_recording_checker_dialog.setObjectName(
                "audio_recording_checker_dialog"
            )
        audio_recording_checker_dialog.resize(400, 304)
        audio_recording_checker_dialog.setMinimumSize(QSize(400, 0))
        audio_recording_checker_dialog.setMaximumSize(QSize(16777215, 16777215))
        audio_recording_checker_dialog.setStyleSheet(
            "QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            "}\n"
            "\n"
            "/* Content App */\n"
            "#content_top_bg{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#right_buttons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#right_buttons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#right_buttons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "	width: 15px;\n"
            "	height: 15px;\n"
            "	border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "    margin:0px 3px 0px 3px;\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "	border: 3px solid rgb(52, 59, 72);	\n"
            "	background-image: url(:/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            ""
            "QCheckBox::disabled {color: rgba(255, 255, 255, 10%) }\n"
            ""
        )
        self.content_box = QFrame(audio_recording_checker_dialog)
        self.content_box.setObjectName("content_box")
        self.content_box.setGeometry(QRect(0, 50, 400, 251))
        self.content_box.setMinimumSize(QSize(400, 0))
        self.content_box.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.content_box.setFrameShape(QFrame.Box)
        self.content_box.setFrameShadow(QFrame.Sunken)
        self.content_box_layout = QVBoxLayout(self.content_box)
        self.content_box_layout.setObjectName("content_box_layout")
        self.content_box_layout.setContentsMargins(12, 12, 12, 12)
        self.disclaimer = QLabel(self.content_box)
        self.disclaimer.setObjectName("disclaimer")
        self.disclaimer.setWordWrap(True)

        self.content_box_layout.addWidget(self.disclaimer)

        self.verticalSpacer = QSpacerItem(
            20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.content_box_layout.addItem(self.verticalSpacer)

        self.ffmpeg_box = QHBoxLayout()
        self.ffmpeg_box.setObjectName("ffmpeg_box")
        self.ffmpeg_box.setContentsMargins(-1, -1, 0, 0)
        self.ffmpeg_installed_img = QLabel(self.content_box)
        self.ffmpeg_installed_img.setObjectName("ffmpeg_installed_img")
        self.ffmpeg_installed_img.setMinimumSize(QSize(20, 20))
        self.ffmpeg_installed_img.setMaximumSize(QSize(20, 20))
        self.ffmpeg_installed_img.setPixmap(QPixmap(":/icons/icons/green-mark.png"))

        self.ffmpeg_box.addWidget(self.ffmpeg_installed_img)

        self.ffmpeg_text_box = QVBoxLayout()
        self.ffmpeg_text_box.setObjectName("ffmpeg_text_box")
        self.ffmpeg_text_box.setContentsMargins(10, -1, -1, 0)
        self.ffmpeg_installed_msg = QLabel(self.content_box)
        self.ffmpeg_installed_msg.setObjectName("ffmpeg_installed_msg")
        self.ffmpeg_installed_msg.setStyleSheet("font-size: 13px;")
        self.ffmpeg_installed_msg.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.ffmpeg_installed_msg.setWordWrap(True)

        self.ffmpeg_text_box.addWidget(self.ffmpeg_installed_msg)

        self.ffmpeg_box.addLayout(self.ffmpeg_text_box)

        self.content_box_layout.addLayout(self.ffmpeg_box)

        self.vb_cable_box_installed = QHBoxLayout()
        self.vb_cable_box_installed.setObjectName("vb_cable_box_installed")
        self.vb_cable_box_installed.setContentsMargins(-1, -1, 0, 0)
        self.vb_cable_installed_img = QLabel(self.content_box)
        self.vb_cable_installed_img.setObjectName("vb_cable_installed_img")
        self.vb_cable_installed_img.setMinimumSize(QSize(20, 20))
        self.vb_cable_installed_img.setMaximumSize(QSize(20, 20))
        self.vb_cable_installed_img.setPixmap(QPixmap(":/icons/icons/green-mark.png"))

        self.vb_cable_box_installed.addWidget(self.vb_cable_installed_img)

        self.vb_cable_text_box = QVBoxLayout()
        self.vb_cable_text_box.setObjectName("vb_cable_text_box")
        self.vb_cable_text_box.setContentsMargins(10, -1, -1, 0)
        self.vb_cable_installed_msg = QLabel(self.content_box)
        self.vb_cable_installed_msg.setObjectName("vb_cable_installed_msg")
        self.vb_cable_installed_msg.setStyleSheet("font-size: 13px;")
        self.vb_cable_installed_msg.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.vb_cable_installed_msg.setWordWrap(True)

        self.vb_cable_text_box.addWidget(self.vb_cable_installed_msg)

        self.vb_cable_box_installed.addLayout(self.vb_cable_text_box)

        self.content_box_layout.addLayout(self.vb_cable_box_installed)

        self.vb_cable_box_first_output_audio_device = QFrame(self.content_box)
        self.vb_cable_box_first_output_audio_device.setObjectName(
            "vb_cable_box_first_output_audio_device"
        )
        self.vb_cable_box_first_output_audio_device_layout = QHBoxLayout(
            self.vb_cable_box_first_output_audio_device
        )
        self.vb_cable_box_first_output_audio_device_layout.setObjectName(
            "vb_cable_box_first_output_audio_device_layout"
        )
        self.vb_cable_box_first_output_audio_device_layout.setContentsMargins(
            0, 0, 0, 0
        )
        self.vb_cable_first_output_audio_device_img = QLabel(
            self.vb_cable_box_first_output_audio_device
        )
        self.vb_cable_first_output_audio_device_img.setObjectName(
            "vb_cable_first_output_audio_device_img"
        )
        self.vb_cable_first_output_audio_device_img.setMinimumSize(QSize(20, 20))
        self.vb_cable_first_output_audio_device_img.setMaximumSize(QSize(20, 20))
        self.vb_cable_first_output_audio_device_img.setPixmap(
            QPixmap(":/icons/icons/green-mark.png")
        )

        self.vb_cable_box_first_output_audio_device_layout.addWidget(
            self.vb_cable_first_output_audio_device_img
        )

        self.vb_cable_text_box_first_output_audio_device = QVBoxLayout()
        self.vb_cable_text_box_first_output_audio_device.setObjectName(
            "vb_cable_text_box_first_output_audio_device"
        )
        self.vb_cable_text_box_first_output_audio_device.setContentsMargins(
            10, -1, -1, 0
        )
        self.vb_cable_first_output_audio_device_msg = QLabel(
            self.vb_cable_box_first_output_audio_device
        )
        self.vb_cable_first_output_audio_device_msg.setObjectName(
            "vb_cable_first_output_audio_device_msg"
        )
        self.vb_cable_first_output_audio_device_msg.setStyleSheet("font-size: 13px;")
        self.vb_cable_first_output_audio_device_msg.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.vb_cable_first_output_audio_device_msg.setWordWrap(True)

        self.vb_cable_text_box_first_output_audio_device.addWidget(
            self.vb_cable_first_output_audio_device_msg
        )

        self.vb_cable_box_first_output_audio_device_layout.addLayout(
            self.vb_cable_text_box_first_output_audio_device
        )

        self.content_box_layout.addWidget(self.vb_cable_box_first_output_audio_device)

        self.vertical_spacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.content_box_layout.addItem(self.vertical_spacer)

        self.navigation_buttons = QFrame(self.content_box)
        self.navigation_buttons.setObjectName("navigation_buttons")
        self.navigation_buttons.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_6 = QHBoxLayout(self.navigation_buttons)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.guide_link = QHBoxLayout()
        self.guide_link.setObjectName("guide_link")
        self.guide_link.setContentsMargins(-1, -1, -1, 0)

        self.horizontalLayout_6.addLayout(self.guide_link)

        self.left_spacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.left_spacer)

        self.ok_button = QPushButton(self.navigation_buttons)
        self.ok_button.setObjectName("ok_button")
        self.ok_button.setEnabled(True)
        self.ok_button.setMinimumSize(QSize(80, 30))
        self.ok_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ok_button.setLayoutDirection(Qt.LeftToRight)
        self.ok_button.setStyleSheet(
            ":disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )

        self.horizontalLayout_6.addWidget(self.ok_button)

        self.content_box_layout.addWidget(self.navigation_buttons)

        self.content_top_bg = QFrame(audio_recording_checker_dialog)
        self.content_top_bg.setObjectName("content_top_bg")
        self.content_top_bg.setGeometry(QRect(0, 0, 400, 50))
        self.content_top_bg.setMinimumSize(QSize(400, 50))
        self.content_top_bg.setMaximumSize(QSize(16777215, 50))
        self.content_top_bg.setFrameShape(QFrame.NoFrame)
        self.content_top_bg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_top_bg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.left_box = QFrame(self.content_top_bg)
        self.left_box.setObjectName("left_box")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setFrameShape(QFrame.NoFrame)
        self.left_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.left_box)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo_container = QFrame(self.left_box)
        self.logo_container.setObjectName("logo_container")
        self.logo_container.setMinimumSize(QSize(60, 0))
        self.logo_container.setMaximumSize(QSize(60, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.logo_container)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.top_logo = QLabel(self.logo_container)
        self.top_logo.setObjectName("top_logo")
        self.top_logo.setMinimumSize(QSize(42, 42))
        self.top_logo.setMaximumSize(QSize(42, 42))
        self.top_logo.setPixmap(QPixmap(":/images/images/logo-42x42.png"))

        self.horizontalLayout_8.addWidget(self.top_logo)

        self.horizontalLayout_3.addWidget(self.logo_container)

        self.title_right_info = QLabel(self.left_box)
        self.title_right_info.setObjectName("title_right_info")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.title_right_info.sizePolicy().hasHeightForWidth()
        )
        self.title_right_info.setSizePolicy(sizePolicy1)
        self.title_right_info.setMaximumSize(QSize(16777215, 45))
        self.title_right_info.setStyleSheet("font: 12pt;")
        self.title_right_info.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.horizontalLayout_3.addWidget(self.title_right_info)

        self.horizontalLayout.addWidget(self.left_box)

        self.right_buttons = QFrame(self.content_top_bg)
        self.right_buttons.setObjectName("right_buttons")
        self.right_buttons.setMinimumSize(QSize(0, 28))
        self.right_buttons.setFrameShape(QFrame.NoFrame)
        self.right_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.right_buttons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.right_buttons, 0, Qt.AlignRight)

        self.retranslateUi(audio_recording_checker_dialog)

        QMetaObject.connectSlotsByName(audio_recording_checker_dialog)

    # setupUi

    def retranslateUi(self, audio_recording_checker_dialog):
        self.translations = load_translations()
        audio_recording_checker_dialog.setWindowTitle(
            QCoreApplication.translate(
                "audio_recording_checker_dialog", "FIT Audio Recorder Checker", None
            )
        )
        self.disclaimer.setText(self.translations["AUDIO_VIDEO_SETTING_DISCLAIMER"])
        self.ffmpeg_installed_img.setText("")
        self.ffmpeg_installed_msg.setText(self.translations["FFMPEG_INSTALLED"])
        self.vb_cable_installed_img.setText("")
        self.vb_cable_installed_msg.setText(self.translations["VB_CABLE_INSTALLED"])
        self.vb_cable_first_output_audio_device_img.setText("")
        self.vb_cable_first_output_audio_device_msg.setText(
            self.translations["VB_CABLE_FIRST_OUPUT_AUDIO_DEVICE"]
        )
        self.ok_button.setText("Ok")
        self.top_logo.setText("")
        self.title_right_info.setText(
            self.translations["TITLE_RIGHT_INFO_LABEL_AUDIO_VIDEO_SETTING"]
        )

    # retranslateUi
