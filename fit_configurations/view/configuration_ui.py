#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_fit_configuration(object):
    def setupUi(self, fit_configuration):
        fit_configuration.setObjectName("fit_configuration")
        fit_configuration.resize(800, 600)
        fit_configuration.setMinimumSize(QtCore.QSize(800, 600))
        fit_configuration.setMaximumSize(QtCore.QSize(800, 600))
        self.styleSheet = QtWidgets.QFrame(parent=fit_configuration)
        self.styleSheet.setGeometry(QtCore.QRect(-1, -1, 800, 600))
        self.styleSheet.setMaximumSize(QtCore.QSize(800, 600))
        self.styleSheet.setStyleSheet(
            "\n"
            "QWidget{\n"
            "    color: rgb(221, 221, 221);\n"
            "    font: 13px;\n"
            "}\n"
            "\n"
            "/* Tooltip */\n"
            "QToolTip {\n"
            "    color: #e06133;\n"
            "    background-color: rgba(33, 37, 43, 180);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "    background-image: none;\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 2px solid rgb(224, 97, 51);\n"
            "    text-align: left;\n"
            "    padding-left: 8px;\n"
            "    margin: 0px;\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#title_right_info { font: 13px; }\n"
            "#title_right_info { padding-left: 10px; }\n"
            "\n"
            "/* Content App */\n"
            "#content_top_bg{    \n"
            "    background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#content_bottom{\n"
            "    border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#right_buttons_container .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#right_buttons_container .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#right_buttons_container .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottom_bar { background-color: rgb(44, 49, 58); }\n"
            "#bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* LineEdit */\n"
            "QLineEdit {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "QLineEdit::disabled {\n"
            "    color: rgba(255, 255, 255, 10%);\n"
            "}\n"
            "\n"
            "QLabel::disabled {\n"
            "    color: rgba(255, 255, 255, 10%);\n"
            "}\n"
            "\n"
            "/* PlainTextEdit */\n"
            "QPlainTextEdit {\n"
            "    background-color: rgb(27, 29, 35);\n"
            "    border-radius: 5px;\n"
            "    padding: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "    border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "    border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    width: 15px;\n"
            "    height: 15px;\n"
            "    border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "    margin:0px 3px 0px 3px;\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "    border: 3px solid rgb(52, 59, 72);    \n"
            "    background-image: url(:/icons/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "QCheckBox::disabled {color: rgba(255, 255, 255, 10%) }\n"
            "\n"
            "/* ComboBox */\n"
            "QComboBox{\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-bottom: 5px;\n"
            "    padding-top: 5px;\n"
            "    padding-left: 10px;\n"
            "\n"
            "}\n"
            "QComboBox:hover{\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 25px; \n"
            "    border-left-width: 3px;\n"
            "    border-left-color: rgba(39, 44, 54, 150);\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "\n"
            "QComboBox:!editable{\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    border: none;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "     padding:10px;\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
            "Button */\n"
            "#pages_container QPushButton {\n"
            "    border: 2px solid rgb(52, 59, 72);\n"
            "    border-radius: 5px;    \n"
            "    background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#pages_container QPushButton:hover {\n"
            "    background-color: rgb(57, 65, 80);\n"
            "    border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#pages_container QPushButton:pressed {    \n"
            "    background-color: rgb(35, 40, 49);\n"
            "    border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        self.styleSheet.setObjectName("styleSheet")
        self.styleSheetLayout = QtWidgets.QVBoxLayout(self.styleSheet)
        self.styleSheetLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize
        )
        self.styleSheetLayout.setContentsMargins(10, 10, 10, 10)
        self.styleSheetLayout.setObjectName("styleSheetLayout")
        self.bg_app = QtWidgets.QFrame(parent=self.styleSheet)
        self.bg_app.setStyleSheet("background-color: rgb(44, 49, 58);")
        self.bg_app.setObjectName("bg_app")
        self.bgAppLayout = QtWidgets.QVBoxLayout(self.bg_app)
        self.bgAppLayout.setContentsMargins(0, -1, 0, 0)
        self.bgAppLayout.setObjectName("bgAppLayout")
        self.content_box = QtWidgets.QFrame(parent=self.bg_app)
        self.content_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_box.setObjectName("content_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_box)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content_top_bg = QtWidgets.QFrame(parent=self.content_box)
        self.content_top_bg.setMinimumSize(QtCore.QSize(0, 50))
        self.content_top_bg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.content_top_bg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_top_bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_top_bg.setObjectName("content_top_bg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_top_bg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_box = QtWidgets.QFrame(parent=self.content_top_bg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_box.setObjectName("left_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.left_box)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_container = QtWidgets.QFrame(parent=self.left_box)
        self.logo_container.setMinimumSize(QtCore.QSize(60, 0))
        self.logo_container.setMaximumSize(QtCore.QSize(60, 16777215))
        self.logo_container.setObjectName("logo_container")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.logo_container)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.top_logo_label = QtWidgets.QLabel(parent=self.logo_container)
        self.top_logo_label.setMinimumSize(QtCore.QSize(42, 42))
        self.top_logo_label.setMaximumSize(QtCore.QSize(42, 42))
        self.top_logo_label.setText("")
        self.top_logo_label.setPixmap(QtGui.QPixmap(":/images/images/logo-42x42.png"))
        self.top_logo_label.setObjectName("top_logo_label")
        self.horizontalLayout_8.addWidget(self.top_logo_label)
        self.horizontalLayout_3.addWidget(self.logo_container)
        self.title_right_info_label = QtWidgets.QLabel(parent=self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_right_info_label.sizePolicy().hasHeightForWidth()
        )
        self.title_right_info_label.setSizePolicy(sizePolicy)
        self.title_right_info_label.setMaximumSize(QtCore.QSize(16777215, 45))
        self.title_right_info_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.title_right_info_label.setObjectName("title_right_info_label")
        self.horizontalLayout_3.addWidget(self.title_right_info_label)
        self.horizontalLayout.addWidget(self.left_box)
        self.right_buttons_container = QtWidgets.QFrame(parent=self.content_top_bg)
        self.right_buttons_container.setMinimumSize(QtCore.QSize(0, 28))
        self.right_buttons_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.right_buttons_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_buttons_container.setObjectName("right_buttons_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.right_buttons_container)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimize_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.minimize_button.setMinimumSize(QtCore.QSize(28, 28))
        self.minimize_button.setMaximumSize(QtCore.QSize(28, 28))
        self.minimize_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.minimize_button.setToolTip("")
        self.minimize_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_minimize.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QtCore.QSize(20, 20))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_2.addWidget(self.minimize_button)
        self.close_button = QtWidgets.QPushButton(parent=self.right_buttons_container)
        self.close_button.setMinimumSize(QtCore.QSize(28, 28))
        self.close_button.setMaximumSize(QtCore.QSize(28, 28))
        self.close_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.close_button.setToolTip("")
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_close-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QtCore.QSize(20, 20))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.horizontalLayout.addWidget(
            self.right_buttons_container, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout_2.addWidget(self.content_top_bg)
        self.content_bottom = QtWidgets.QFrame(parent=self.content_box)
        self.content_bottom.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bottom.setObjectName("content_bottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content_bottom)
        self.verticalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(parent=self.content_bottom)
        self.content.setStyleSheet("background-color: rgb(40, 44, 52);\n" "")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Left_menu = QtWidgets.QFrame(parent=self.content)
        self.Left_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.Left_menu.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Left_menu.setObjectName("Left_menu")
        self.LeftMenuLayout = QtWidgets.QVBoxLayout(self.Left_menu)
        self.LeftMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.LeftMenuLayout.setObjectName("LeftMenuLayout")
        self.menu_tabs = QtWidgets.QTreeWidget(parent=self.Left_menu)
        self.menu_tabs.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.menu_tabs.setIndentation(0)
        self.menu_tabs.setObjectName("menu_tabs")
        self.menu_tabs.headerItem().setText(0, "1")
        self.menu_tabs.header().setVisible(False)
        self.menu_tabs.header().setMinimumSectionSize(20)
        self.LeftMenuLayout.addWidget(self.menu_tabs)
        self.horizontalLayout_4.addWidget(self.Left_menu)
        self.pages_container = QtWidgets.QFrame(parent=self.content)
        self.pages_container.setMinimumSize(QtCore.QSize(0, 0))
        self.pages_container.setObjectName("pages_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pages_container)
        self.verticalLayout.setContentsMargins(1, 12, 12, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtWidgets.QStackedWidget(parent=self.pages_container)
        self.tabs.setMinimumSize(QtCore.QSize(0, 409))
        self.tabs.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tabs.setStyleSheet("background: transparent;")
        self.tabs.setObjectName("tabs")
        self.general = QtWidgets.QWidget()
        self.general.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.general.setObjectName("general")
        self.general_configuration = QtWidgets.QFrame(parent=self.general)
        self.general_configuration.setGeometry(QtCore.QRect(0, -2, 600, 409))
        self.general_configuration.setMaximumSize(QtCore.QSize(600, 16777215))
        self.general_configuration.setObjectName("general_configuration")
        self.caseInfo = QtWidgets.QHBoxLayout(self.general_configuration)
        self.caseInfo.setContentsMargins(20, 20, 1, 20)
        self.caseInfo.setObjectName("caseInfo")
        self.general_form = QtWidgets.QFrame(parent=self.general_configuration)
        self.general_form.setMinimumSize(QtCore.QSize(0, 0))
        self.general_form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.general_form.setObjectName("general_form")
        self.form_layout = QtWidgets.QVBoxLayout(self.general_form)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(6)
        self.form_layout.setObjectName("form_layout")
        self.cases_folder_layout = QtWidgets.QFrame(parent=self.general_form)
        self.cases_folder_layout.setMinimumSize(QtCore.QSize(0, 0))
        self.cases_folder_layout.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cases_folder_layout.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.cases_folder_layout.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.cases_folder_layout.setObjectName("cases_folder_layout")
        self.logo_layout = QtWidgets.QHBoxLayout(self.cases_folder_layout)
        self.logo_layout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.logo_layout.setContentsMargins(0, 10, 0, 0)
        self.logo_layout.setObjectName("logo_layout")
        self.cases_folder_path = QtWidgets.QLineEdit(parent=self.cases_folder_layout)
        self.cases_folder_path.setMinimumSize(QtCore.QSize(0, 30))
        self.cases_folder_path.setMaximumSize(QtCore.QSize(490, 16777215))
        self.cases_folder_path.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.cases_folder_path.setText("")
        self.cases_folder_path.setObjectName("cases_folder_path")
        self.logo_layout.addWidget(self.cases_folder_path)
        self.cases_folder_button = QtWidgets.QPushButton(
            parent=self.cases_folder_layout
        )
        self.cases_folder_button.setMinimumSize(QtCore.QSize(80, 30))
        self.cases_folder_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cases_folder_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.cases_folder_button.setStyleSheet("background-color: rgb(52, 59, 72);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("fit_configurations/ui/../icons/cil-folder-open.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.cases_folder_button.setIcon(icon2)
        self.cases_folder_button.setObjectName("cases_folder_button")
        self.logo_layout.addWidget(self.cases_folder_button)
        self.form_layout.addWidget(self.cases_folder_layout)
        self.home_page_url = QtWidgets.QLineEdit(parent=self.general_form)
        self.home_page_url.setMinimumSize(QtCore.QSize(0, 30))
        self.home_page_url.setMaximumSize(QtCore.QSize(490, 16777215))
        self.home_page_url.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.home_page_url.setObjectName("home_page_url")
        self.form_layout.addWidget(self.home_page_url)
        self.user_agent_layout = QtWidgets.QVBoxLayout()
        self.user_agent_layout.setContentsMargins(-1, 0, -1, -1)
        self.user_agent_layout.setSpacing(2)
        self.user_agent_layout.setObjectName("user_agent_layout")
        self.user_agent_layout_info = QtWidgets.QHBoxLayout()
        self.user_agent_layout_info.setContentsMargins(-1, 0, 0, 0)
        self.user_agent_layout_info.setSpacing(7)
        self.user_agent_layout_info.setObjectName("user_agent_layout_info")
        self.user_agent = QtWidgets.QPlainTextEdit(parent=self.general_form)
        self.user_agent.setMinimumSize(QtCore.QSize(490, 0))
        self.user_agent.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.user_agent.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.user_agent.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.user_agent.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.user_agent.setObjectName("user_agent")
        self.user_agent_layout_info.addWidget(self.user_agent)
        self.user_agent_button = QtWidgets.QPushButton(parent=self.general_form)
        self.user_agent_button.setMinimumSize(QtCore.QSize(80, 30))
        self.user_agent_button.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.user_agent_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.user_agent_button.setStyleSheet("background-color: rgb(52, 59, 72);")
        self.user_agent_button.setObjectName("user_agent_button")
        self.user_agent_layout_info.addWidget(self.user_agent_button)
        self.user_agent_layout.addLayout(self.user_agent_layout_info)
        self.form_layout.addLayout(self.user_agent_layout)
        self.types_proceedings_layout = QtWidgets.QVBoxLayout()
        self.types_proceedings_layout.setContentsMargins(-1, 0, -1, 0)
        self.types_proceedings_layout.setSpacing(2)
        self.types_proceedings_layout.setObjectName("types_proceedings_layout")
        self.types_proceedings = QtWidgets.QPlainTextEdit(parent=self.general_form)
        self.types_proceedings.setMinimumSize(QtCore.QSize(0, 0))
        self.types_proceedings.setMaximumSize(QtCore.QSize(490, 16777215))
        self.types_proceedings.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.types_proceedings.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )
        self.types_proceedings.setObjectName("types_proceedings")
        self.types_proceedings_layout.addWidget(self.types_proceedings)
        self.types_proceedings_info_label = QtWidgets.QLabel(parent=self.general_form)
        self.types_proceedings_info_label.setObjectName("types_proceedings_info_label")
        self.types_proceedings_layout.addWidget(self.types_proceedings_info_label)
        self.form_layout.addLayout(self.types_proceedings_layout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 10, -1, 0)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.db_path_layout = QtWidgets.QFrame(parent=self.general_form)
        self.db_path_layout.setMinimumSize(QtCore.QSize(0, 0))
        self.db_path_layout.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.db_path_layout.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.db_path_layout.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.db_path_layout.setObjectName("db_path_layout")
        self.db_layout = QtWidgets.QHBoxLayout(self.db_path_layout)
        self.db_layout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.db_layout.setContentsMargins(0, 0, 0, 0)
        self.db_layout.setSpacing(0)
        self.db_layout.setObjectName("db_layout")
        self.db_path = QtWidgets.QLineEdit(parent=self.db_path_layout)
        self.db_path.setMinimumSize(QtCore.QSize(0, 30))
        self.db_path.setMaximumSize(QtCore.QSize(490, 16777215))
        self.db_path.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.db_path.setText("")
        self.db_path.setReadOnly(True)
        self.db_path.setObjectName("db_path")
        self.db_layout.addWidget(self.db_path)
        spacerItem = QtWidgets.QSpacerItem(
            90,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.db_layout.addItem(spacerItem)
        self.verticalLayout_8.addWidget(self.db_path_layout)
        self.db_path_info_label = QtWidgets.QLabel(parent=self.general_form)
        self.db_path_info_label.setObjectName("db_path_info_label")
        self.verticalLayout_8.addWidget(self.db_path_info_label)
        self.form_layout.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.form_layout.addItem(spacerItem1)
        self.caseInfo.addWidget(self.general_form)
        self.tabs.addWidget(self.general)
        self.language = QtWidgets.QWidget()
        self.language.setObjectName("language")
        self.language_configuration = QtWidgets.QFrame(parent=self.language)
        self.language_configuration.setGeometry(QtCore.QRect(-1, -1, 600, 148))
        self.language_configuration.setMinimumSize(QtCore.QSize(600, 0))
        self.language_configuration.setMaximumSize(QtCore.QSize(600, 16777215))
        self.language_configuration.setObjectName("language_configuration")
        self.language_configuration_layout = QtWidgets.QVBoxLayout(
            self.language_configuration
        )
        self.language_configuration_layout.setContentsMargins(20, 20, 20, 20)
        self.language_configuration_layout.setObjectName(
            "language_configuration_layout"
        )
        self.report_language_layout = QtWidgets.QHBoxLayout()
        self.report_language_layout.setContentsMargins(-1, 0, 0, 0)
        self.report_language_layout.setObjectName("report_language_layout")
        self.language_label = QtWidgets.QLabel(parent=self.language_configuration)
        self.language_label.setObjectName("language_label")
        self.report_language_layout.addWidget(self.language_label)
        self.report_language = QtWidgets.QComboBox(parent=self.language_configuration)
        self.report_language.setMinimumSize(QtCore.QSize(300, 0))
        self.report_language.setMaximumSize(QtCore.QSize(300, 16777215))
        self.report_language.setMouseTracking(True)
        self.report_language.setAutoFillBackground(False)
        self.report_language.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.report_language.setEditable(True)
        self.report_language.setCurrentText("")
        self.report_language.setIconSize(QtCore.QSize(16, 16))
        self.report_language.setFrame(True)
        self.report_language.setObjectName("report_language")
        self.report_language_layout.addWidget(self.report_language)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.report_language_layout.addItem(spacerItem2)
        self.language_configuration_layout.addLayout(self.report_language_layout)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.language_configuration_layout.addItem(spacerItem3)
        self.tabs.addWidget(self.language)
        self.network = QtWidgets.QWidget()
        self.network.setObjectName("network")
        self.network_configuration = QtWidgets.QFrame(parent=self.network)
        self.network_configuration.setGeometry(QtCore.QRect(-1, -1, 600, 411))
        self.network_configuration.setMaximumSize(QtCore.QSize(600, 16777215))
        self.network_configuration.setObjectName("network_configuration")
        self.network_configuration_layout = QtWidgets.QVBoxLayout(
            self.network_configuration
        )
        self.network_configuration_layout.setContentsMargins(20, 20, 20, 20)
        self.network_configuration_layout.setObjectName("network_configuration_layout")
        self.enable_network_tools_box = QtWidgets.QVBoxLayout()
        self.enable_network_tools_box.setContentsMargins(-1, -1, -1, 0)
        self.enable_network_tools_box.setSpacing(10)
        self.enable_network_tools_box.setObjectName("enable_network_tools_box")
        self.enable_network_tools_box_label = QtWidgets.QLabel(
            parent=self.network_configuration
        )
        self.enable_network_tools_box_label.setObjectName(
            "enable_network_tools_box_label"
        )
        self.enable_network_tools_box.addWidget(self.enable_network_tools_box_label)
        self.whois = QtWidgets.QCheckBox(parent=self.network_configuration)
        self.whois.setObjectName("whois")
        self.enable_network_tools_box.addWidget(self.whois)
        self.nslookup = QtWidgets.QCheckBox(parent=self.network_configuration)
        self.nslookup.setObjectName("nslookup")
        self.enable_network_tools_box.addWidget(self.nslookup)
        self.headers = QtWidgets.QCheckBox(parent=self.network_configuration)
        self.headers.setObjectName("headers")
        self.enable_network_tools_box.addWidget(self.headers)
        self.traceroute = QtWidgets.QCheckBox(parent=self.network_configuration)
        self.traceroute.setObjectName("traceroute")
        self.enable_network_tools_box.addWidget(self.traceroute)
        self.ssl_keylog = QtWidgets.QCheckBox(parent=self.network_configuration)
        self.ssl_keylog.setObjectName("ssl_keylog")
        self.enable_network_tools_box.addWidget(self.ssl_keylog)
        self.ssl_certificate = QtWidgets.QCheckBox(parent=self.network_configuration)
        self.ssl_certificate.setObjectName("ssl_certificate")
        self.enable_network_tools_box.addWidget(self.ssl_certificate)
        self.network_configuration_layout.addLayout(self.enable_network_tools_box)
        self.nslookup_configuration_line = QtWidgets.QFrame(
            parent=self.network_configuration
        )
        self.nslookup_configuration_line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.nslookup_configuration_line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.nslookup_configuration_line.setObjectName("nslookup_configuration_line")
        self.network_configuration_layout.addWidget(self.nslookup_configuration_line)
        self.network_setting_box = QtWidgets.QVBoxLayout()
        self.network_setting_box.setContentsMargins(-1, 10, -1, -1)
        self.network_setting_box.setSpacing(10)
        self.network_setting_box.setObjectName("network_setting_box")
        self.network_check_box_row = QtWidgets.QFrame(parent=self.network_configuration)
        self.network_check_box_row.setObjectName("network_check_box_row")
        self.ntp_and_nslookup = QtWidgets.QHBoxLayout(self.network_check_box_row)
        self.ntp_and_nslookup.setContentsMargins(0, 0, 0, 0)
        self.ntp_and_nslookup.setSpacing(0)
        self.ntp_and_nslookup.setObjectName("ntp_and_nslookup")
        self.ntp_configuration_box = QtWidgets.QFrame(parent=self.network_check_box_row)
        self.ntp_configuration_box.setObjectName("ntp_configuration_box")
        self.ntp_box = QtWidgets.QHBoxLayout(self.ntp_configuration_box)
        self.ntp_box.setContentsMargins(0, 0, 10, 0)
        self.ntp_box.setSpacing(0)
        self.ntp_box.setObjectName("ntp_box")
        self.ntp_configuration_box_layout = QtWidgets.QFrame(
            parent=self.ntp_configuration_box
        )
        self.ntp_configuration_box_layout.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        self.ntp_configuration_box_layout.setObjectName("ntp_configuration_box_layout")
        self.ntp_layout = QtWidgets.QVBoxLayout(self.ntp_configuration_box_layout)
        self.ntp_layout.setContentsMargins(0, 0, 0, 0)
        self.ntp_layout.setSpacing(3)
        self.ntp_layout.setObjectName("ntp_layout")
        self.ntp_server_label = QtWidgets.QLabel(
            parent=self.ntp_configuration_box_layout
        )
        self.ntp_server_label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.ntp_server_label.setLineWidth(1)
        self.ntp_server_label.setObjectName("ntp_server_label")
        self.ntp_layout.addWidget(self.ntp_server_label)
        self.ntp_server_layout = QtWidgets.QFrame(
            parent=self.ntp_configuration_box_layout
        )
        self.ntp_server_layout.setMinimumSize(QtCore.QSize(0, 0))
        self.ntp_server_layout.setObjectName("ntp_server_layout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.ntp_server_layout)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.ntp_server = QtWidgets.QLineEdit(parent=self.ntp_server_layout)
        self.ntp_server.setMinimumSize(QtCore.QSize(0, 30))
        self.ntp_server.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.ntp_server.setObjectName("ntp_server")
        self.horizontalLayout_11.addWidget(self.ntp_server)
        self.ntp_layout.addWidget(self.ntp_server_layout)
        self.ntp_box.addWidget(self.ntp_configuration_box_layout)
        self.ntp_and_nslookup.addWidget(self.ntp_configuration_box)
        self.nslookup_configuration_box = QtWidgets.QFrame(
            parent=self.network_check_box_row
        )
        self.nslookup_configuration_box.setObjectName("nslookup_configuration_box")
        self.nslookup_box = QtWidgets.QHBoxLayout(self.nslookup_configuration_box)
        self.nslookup_box.setContentsMargins(0, 0, 0, 0)
        self.nslookup_box.setSpacing(0)
        self.nslookup_box.setObjectName("nslookup_box")
        self.nslookup_configuration_box_layout = QtWidgets.QFrame(
            parent=self.nslookup_configuration_box
        )
        self.nslookup_configuration_box_layout.setMaximumSize(
            QtCore.QSize(16777215, 16777215)
        )
        self.nslookup_configuration_box_layout.setObjectName(
            "nslookup_configuration_box_layout"
        )
        self.nslookup_layout = QtWidgets.QVBoxLayout(
            self.nslookup_configuration_box_layout
        )
        self.nslookup_layout.setContentsMargins(0, 0, 0, 0)
        self.nslookup_layout.setSpacing(3)
        self.nslookup_layout.setObjectName("nslookup_layout")
        self.nslookup_configuration_label = QtWidgets.QLabel(
            parent=self.nslookup_configuration_box_layout
        )
        self.nslookup_configuration_label.setMinimumSize(QtCore.QSize(0, 16))
        self.nslookup_configuration_label.setObjectName("nslookup_configuration_label")
        self.nslookup_layout.addWidget(self.nslookup_configuration_label)
        self.nslookup_dns_server_box = QtWidgets.QFrame(
            parent=self.nslookup_configuration_box_layout
        )
        self.nslookup_dns_server_box.setLineWidth(0)
        self.nslookup_dns_server_box.setObjectName("nslookup_dns_server_box")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.nslookup_dns_server_box)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.nslookup_dns_server = QtWidgets.QLineEdit(
            parent=self.nslookup_dns_server_box
        )
        self.nslookup_dns_server.setMinimumSize(QtCore.QSize(0, 30))
        self.nslookup_dns_server.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.nslookup_dns_server.setObjectName("nslookup_dns_server")
        self.horizontalLayout_14.addWidget(self.nslookup_dns_server)
        self.nslookup_enable_tcp = QtWidgets.QCheckBox(
            parent=self.nslookup_dns_server_box
        )
        self.nslookup_enable_tcp.setObjectName("nslookup_enable_tcp")
        self.horizontalLayout_14.addWidget(self.nslookup_enable_tcp)
        self.nslookup_enable_verbose_mode = QtWidgets.QCheckBox(
            parent=self.nslookup_dns_server_box
        )
        self.nslookup_enable_verbose_mode.setObjectName("nslookup_enable_verbose_mode")
        self.horizontalLayout_14.addWidget(self.nslookup_enable_verbose_mode)
        self.nslookup_layout.addWidget(self.nslookup_dns_server_box)
        self.nslookup_box.addWidget(self.nslookup_configuration_box_layout)
        self.ntp_and_nslookup.addWidget(self.nslookup_configuration_box)
        self.ntp_and_nslookup.setStretch(0, 1)
        self.ntp_and_nslookup.setStretch(1, 2)
        self.network_setting_box.addWidget(self.network_check_box_row)
        self.network_configuration_layout.addLayout(self.network_setting_box)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.network_configuration_layout.addItem(spacerItem4)
        self.tabs.addWidget(self.network)
        self.packetcapture = QtWidgets.QWidget()
        self.packetcapture.setObjectName("packetcapture")
        self.packet_capture_configuration = QtWidgets.QFrame(parent=self.packetcapture)
        self.packet_capture_configuration.setGeometry(QtCore.QRect(-1, -1, 621, 411))
        self.packet_capture_configuration.setMaximumSize(QtCore.QSize(16777215, 600))
        self.packet_capture_configuration.setObjectName("packet_capture_configuration")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.packet_capture_configuration)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.packet_capture_configuration_box = QtWidgets.QVBoxLayout()
        self.packet_capture_configuration_box.setObjectName(
            "packet_capture_configuration_box"
        )
        self.enable_packet_capture_recorder = QtWidgets.QCheckBox(
            parent=self.packet_capture_configuration
        )
        self.enable_packet_capture_recorder.setObjectName(
            "enable_packet_capture_recorder"
        )
        self.packet_capture_configuration_box.addWidget(
            self.enable_packet_capture_recorder
        )
        spacerItem5 = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.packet_capture_configuration_box.addItem(spacerItem5)
        self.packet_capture_recorder_filename = QtWidgets.QLineEdit(
            parent=self.packet_capture_configuration
        )
        self.packet_capture_recorder_filename.setEnabled(True)
        self.packet_capture_recorder_filename.setMinimumSize(QtCore.QSize(0, 30))
        self.packet_capture_recorder_filename.setMaximumSize(
            QtCore.QSize(490, 16777215)
        )
        self.packet_capture_recorder_filename.setStyleSheet(
            "background-color: rgb(33, 37, 43);"
        )
        self.packet_capture_recorder_filename.setObjectName(
            "packet_capture_recorder_filename"
        )
        self.packet_capture_configuration_box.addWidget(
            self.packet_capture_recorder_filename
        )
        spacerItem6 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.packet_capture_configuration_box.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.packet_capture_configuration_box)
        self.tabs.addWidget(self.packetcapture)
        self.pec = QtWidgets.QWidget()
        self.pec.setEnabled(True)
        self.pec.setObjectName("pec")
        self.pec_configuration = QtWidgets.QFrame(parent=self.pec)
        self.pec_configuration.setGeometry(QtCore.QRect(0, 0, 600, 411))
        self.pec_configuration.setMaximumSize(QtCore.QSize(600, 16777215))
        self.pec_configuration.setObjectName("pec_configuration")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pec_configuration)
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.enable_pec_layout = QtWidgets.QHBoxLayout()
        self.enable_pec_layout.setContentsMargins(-1, -1, 0, 20)
        self.enable_pec_layout.setSpacing(20)
        self.enable_pec_layout.setObjectName("enable_pec_layout")
        self.enable_pec = QtWidgets.QCheckBox(parent=self.pec_configuration)
        self.enable_pec.setEnabled(True)
        self.enable_pec.setChecked(False)
        self.enable_pec.setObjectName("enable_pec")
        self.enable_pec_layout.addWidget(self.enable_pec)
        self.verticalLayout_4.addLayout(self.enable_pec_layout)
        self.pec_settings = QtWidgets.QFrame(parent=self.pec_configuration)
        self.pec_settings.setEnabled(True)
        self.pec_settings.setObjectName("pec_settings")
        self.pec_settings_layout = QtWidgets.QVBoxLayout(self.pec_settings)
        self.pec_settings_layout.setContentsMargins(0, 0, 0, 0)
        self.pec_settings_layout.setSpacing(0)
        self.pec_settings_layout.setObjectName("pec_settings_layout")
        self.credentials_configuration = QtWidgets.QHBoxLayout()
        self.credentials_configuration.setContentsMargins(-1, 0, -1, 20)
        self.credentials_configuration.setSpacing(6)
        self.credentials_configuration.setObjectName("credentials_configuration")
        self.credentials_configuration_box = QtWidgets.QVBoxLayout()
        self.credentials_configuration_box.setContentsMargins(-1, 0, -1, -1)
        self.credentials_configuration_box.setSpacing(0)
        self.credentials_configuration_box.setObjectName(
            "credentials_configuration_box"
        )
        self.credentials_configuration_label = QtWidgets.QLabel(
            parent=self.pec_settings
        )
        self.credentials_configuration_label.setEnabled(True)
        self.credentials_configuration_label.setStyleSheet("")
        self.credentials_configuration_label.setObjectName(
            "credentials_configuration_label"
        )
        self.credentials_configuration_box.addWidget(
            self.credentials_configuration_label
        )
        self.username_and_password = QtWidgets.QHBoxLayout()
        self.username_and_password.setContentsMargins(-1, 5, 10, -1)
        self.username_and_password.setSpacing(10)
        self.username_and_password.setObjectName("username_and_password")
        self.pec_email = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.pec_email.setMinimumSize(QtCore.QSize(100, 30))
        self.pec_email.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.pec_email.setObjectName("pec_email")
        self.username_and_password.addWidget(self.pec_email)
        self.pec_password = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.pec_password.setMinimumSize(QtCore.QSize(100, 30))
        self.pec_password.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.pec_password.setObjectName("pec_password")
        self.username_and_password.addWidget(self.pec_password)
        self.credentials_configuration_box.addLayout(self.username_and_password)
        self.credentials_configuration.addLayout(self.credentials_configuration_box)
        self.retries_eml_download_box = QtWidgets.QVBoxLayout()
        self.retries_eml_download_box.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.retries_eml_download_box.setContentsMargins(0, -1, -1, -1)
        self.retries_eml_download_box.setSpacing(5)
        self.retries_eml_download_box.setObjectName("retries_eml_download_box")
        self.retries_eml_download_label = QtWidgets.QLabel(parent=self.pec_settings)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.retries_eml_download_label.sizePolicy().hasHeightForWidth()
        )
        self.retries_eml_download_label.setSizePolicy(sizePolicy)
        self.retries_eml_download_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.retries_eml_download_label.setObjectName("retries_eml_download_label")
        self.retries_eml_download_box.addWidget(self.retries_eml_download_label)
        self.retries_eml_download = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.retries_eml_download.setMinimumSize(QtCore.QSize(0, 30))
        self.retries_eml_download.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.retries_eml_download.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.retries_eml_download.setFrame(True)
        self.retries_eml_download.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.retries_eml_download.setObjectName("retries_eml_download")
        self.retries_eml_download_box.addWidget(self.retries_eml_download)
        self.credentials_configuration.addLayout(self.retries_eml_download_box)
        self.credentials_configuration.setStretch(0, 2)
        self.pec_settings_layout.addLayout(self.credentials_configuration)
        self.server_configuration_label = QtWidgets.QLabel(parent=self.pec_settings)
        self.server_configuration_label.setObjectName("server_configuration_label")
        self.pec_settings_layout.addWidget(self.server_configuration_label)
        self.imap_server_configuration = QtWidgets.QHBoxLayout()
        self.imap_server_configuration.setContentsMargins(-1, 5, -1, 10)
        self.imap_server_configuration.setSpacing(10)
        self.imap_server_configuration.setObjectName("imap_server_configuration")
        self.pec_imap_server = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.pec_imap_server.setMinimumSize(QtCore.QSize(0, 30))
        self.pec_imap_server.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.pec_imap_server.setObjectName("pec_imap_server")
        self.imap_server_configuration.addWidget(self.pec_imap_server)
        self.pec_imap_server_port = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.pec_imap_server_port.setMinimumSize(QtCore.QSize(0, 30))
        self.pec_imap_server_port.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pec_imap_server_port.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.pec_imap_server_port.setText("")
        self.pec_imap_server_port.setObjectName("pec_imap_server_port")
        self.imap_server_configuration.addWidget(self.pec_imap_server_port)
        self.verification_imap_button = QtWidgets.QPushButton(parent=self.pec_settings)
        self.verification_imap_button.setEnabled(True)
        self.verification_imap_button.setMinimumSize(QtCore.QSize(120, 30))
        self.verification_imap_button.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.verification_imap_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.verification_imap_button.setStyleSheet(
            "QPushButton {background-color: rgb(52, 59, 72); }\n"
            "QPushButton:disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.verification_imap_button.setObjectName("verification_imap_button")
        self.imap_server_configuration.addWidget(self.verification_imap_button)
        self.info_imap_img_label = QtWidgets.QLabel(parent=self.pec_settings)
        self.info_imap_img_label.setMinimumSize(QtCore.QSize(20, 20))
        self.info_imap_img_label.setMaximumSize(QtCore.QSize(20, 20))
        self.info_imap_img_label.setText("")
        self.info_imap_img_label.setPixmap(
            QtGui.QPixmap("fit_configurations/ui/../icons/green-mark.png")
        )
        self.info_imap_img_label.setObjectName("info_imap_img_label")
        self.imap_server_configuration.addWidget(self.info_imap_img_label)
        self.pec_settings_layout.addLayout(self.imap_server_configuration)
        self.smtp_server_configuration = QtWidgets.QHBoxLayout()
        self.smtp_server_configuration.setContentsMargins(-1, -1, -1, 0)
        self.smtp_server_configuration.setSpacing(10)
        self.smtp_server_configuration.setObjectName("smtp_server_configuration")
        self.pec_smtp_server = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.pec_smtp_server.setMinimumSize(QtCore.QSize(0, 30))
        self.pec_smtp_server.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.pec_smtp_server.setText("")
        self.pec_smtp_server.setObjectName("pec_smtp_server")
        self.smtp_server_configuration.addWidget(self.pec_smtp_server)
        self.pec_smtp_server_port = QtWidgets.QLineEdit(parent=self.pec_settings)
        self.pec_smtp_server_port.setMinimumSize(QtCore.QSize(0, 30))
        self.pec_smtp_server_port.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pec_smtp_server_port.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.pec_smtp_server_port.setObjectName("pec_smtp_server_port")
        self.smtp_server_configuration.addWidget(self.pec_smtp_server_port)
        self.verification_smtp_button = QtWidgets.QPushButton(parent=self.pec_settings)
        self.verification_smtp_button.setMinimumSize(QtCore.QSize(120, 30))
        self.verification_smtp_button.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.verification_smtp_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.verification_smtp_button.setStyleSheet(
            "QPushButton {background-color: rgb(52, 59, 72); }\n"
            "QPushButton:disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.verification_smtp_button.setObjectName("verification_smtp_button")
        self.smtp_server_configuration.addWidget(self.verification_smtp_button)
        self.info_smtp_img_label = QtWidgets.QLabel(parent=self.pec_settings)
        self.info_smtp_img_label.setMinimumSize(QtCore.QSize(20, 20))
        self.info_smtp_img_label.setMaximumSize(QtCore.QSize(20, 20))
        self.info_smtp_img_label.setText("")
        self.info_smtp_img_label.setPixmap(
            QtGui.QPixmap("fit_configurations/ui/../icons/green-mark.png")
        )
        self.info_smtp_img_label.setObjectName("info_smtp_img_label")
        self.smtp_server_configuration.addWidget(self.info_smtp_img_label)
        self.pec_settings_layout.addLayout(self.smtp_server_configuration)
        self.verticalLayout_4.addWidget(self.pec_settings)
        spacerItem7 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_4.addItem(spacerItem7)
        self.tabs.addWidget(self.pec)
        self.screenrecorder = QtWidgets.QWidget()
        self.screenrecorder.setObjectName("screenrecorder")
        self.screen_recorder_configuration = QtWidgets.QFrame(
            parent=self.screenrecorder
        )
        self.screen_recorder_configuration.setGeometry(QtCore.QRect(0, 0, 600, 411))
        self.screen_recorder_configuration.setMaximumSize(QtCore.QSize(600, 16777215))
        self.screen_recorder_configuration.setObjectName(
            "screen_recorder_configuration"
        )
        self.screen_recorder_configuration_layout = QtWidgets.QVBoxLayout(
            self.screen_recorder_configuration
        )
        self.screen_recorder_configuration_layout.setContentsMargins(20, 20, 20, 20)
        self.screen_recorder_configuration_layout.setObjectName(
            "screen_recorder_configuration_layout"
        )
        self.screen_recorder_configuration_box = QtWidgets.QVBoxLayout()
        self.screen_recorder_configuration_box.setObjectName(
            "screen_recorder_configuration_box"
        )
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.enable_screen_recorder = QtWidgets.QCheckBox(
            parent=self.screen_recorder_configuration
        )
        self.enable_screen_recorder.setObjectName("enable_screen_recorder")
        self.horizontalLayout_7.addWidget(self.enable_screen_recorder)
        self.screen_recorder_configuration_box.addLayout(self.horizontalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(
            20,
            10,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.screen_recorder_configuration_box.addItem(spacerItem8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.audio_recording_box = QtWidgets.QFrame(
            parent=self.screen_recorder_configuration
        )
        self.audio_recording_box.setObjectName("audio_recording_box")
        self.audio_recording_layout = QtWidgets.QHBoxLayout(self.audio_recording_box)
        self.audio_recording_layout.setContentsMargins(0, 0, 0, 0)
        self.audio_recording_layout.setObjectName("audio_recording_layout")
        self.enable_audio_recording = QtWidgets.QCheckBox(
            parent=self.audio_recording_box
        )
        self.enable_audio_recording.setEnabled(False)
        self.enable_audio_recording.setObjectName("enable_audio_recording")
        self.audio_recording_layout.addWidget(self.enable_audio_recording)
        spacerItem9 = QtWidgets.QSpacerItem(
            40,
            5,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.audio_recording_layout.addItem(spacerItem9)
        self.verify_audio_setting_button = QtWidgets.QPushButton(
            parent=self.audio_recording_box
        )
        self.verify_audio_setting_button.setEnabled(True)
        self.verify_audio_setting_button.setMinimumSize(QtCore.QSize(150, 30))
        self.verify_audio_setting_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.verify_audio_setting_button.setStyleSheet(
            "QPushButton {\n"
            "    background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton::disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.verify_audio_setting_button.setObjectName("verify_audio_setting_button")
        self.audio_recording_layout.addWidget(self.verify_audio_setting_button)
        spacerItem10 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.audio_recording_layout.addItem(spacerItem10)
        self.verticalLayout_5.addWidget(self.audio_recording_box)
        self.temporary_msg_label = QtWidgets.QLabel(
            parent=self.screen_recorder_configuration
        )
        self.temporary_msg_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.temporary_msg_label.setWordWrap(True)
        self.temporary_msg_label.setObjectName("temporary_msg_label")
        self.verticalLayout_5.addWidget(self.temporary_msg_label)
        self.screen_recorder_configuration_box.addLayout(self.verticalLayout_5)
        self.screen_recorder_filename = QtWidgets.QLineEdit(
            parent=self.screen_recorder_configuration
        )
        self.screen_recorder_filename.setMinimumSize(QtCore.QSize(0, 30))
        self.screen_recorder_filename.setStyleSheet(
            "background-color: rgb(33, 37, 43);"
        )
        self.screen_recorder_filename.setObjectName("screen_recorder_filename")
        self.screen_recorder_configuration_box.addWidget(self.screen_recorder_filename)
        spacerItem11 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.screen_recorder_configuration_box.addItem(spacerItem11)
        self.screen_recorder_configuration_layout.addLayout(
            self.screen_recorder_configuration_box
        )
        self.tabs.addWidget(self.screenrecorder)
        self.timestamp = QtWidgets.QWidget()
        self.timestamp.setObjectName("timestamp")
        self.timestamp_configuration = QtWidgets.QFrame(parent=self.timestamp)
        self.timestamp_configuration.setGeometry(QtCore.QRect(0, 0, 600, 411))
        self.timestamp_configuration.setMaximumSize(QtCore.QSize(600, 16777215))
        self.timestamp_configuration.setObjectName("timestamp_configuration")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.timestamp_configuration)
        self.verticalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.enable_timestamp_layout = QtWidgets.QHBoxLayout()
        self.enable_timestamp_layout.setContentsMargins(-1, -1, 0, 20)
        self.enable_timestamp_layout.setSpacing(0)
        self.enable_timestamp_layout.setObjectName("enable_timestamp_layout")
        self.enable_timestamp = QtWidgets.QCheckBox(parent=self.timestamp_configuration)
        self.enable_timestamp.setEnabled(True)
        self.enable_timestamp.setChecked(False)
        self.enable_timestamp.setObjectName("enable_timestamp")
        self.enable_timestamp_layout.addWidget(self.enable_timestamp)
        self.verticalLayout_7.addLayout(self.enable_timestamp_layout)
        self.timestamp_settings = QtWidgets.QFrame(parent=self.timestamp_configuration)
        self.timestamp_settings.setEnabled(True)
        self.timestamp_settings.setObjectName("timestamp_settings")
        self.pec_settings_layout_2 = QtWidgets.QVBoxLayout(self.timestamp_settings)
        self.pec_settings_layout_2.setContentsMargins(0, 0, 0, 0)
        self.pec_settings_layout_2.setSpacing(6)
        self.pec_settings_layout_2.setObjectName("pec_settings_layout_2")
        self.server_timestamp_configuration = QtWidgets.QHBoxLayout()
        self.server_timestamp_configuration.setContentsMargins(-1, 0, -1, 0)
        self.server_timestamp_configuration.setSpacing(6)
        self.server_timestamp_configuration.setObjectName(
            "server_timestamp_configuration"
        )
        self.timestamp_server_name_box = QtWidgets.QVBoxLayout()
        self.timestamp_server_name_box.setContentsMargins(-1, 0, -1, -1)
        self.timestamp_server_name_box.setSpacing(0)
        self.timestamp_server_name_box.setObjectName("timestamp_server_name_box")
        self.timestamp_server_name_box_label = QtWidgets.QLabel(
            parent=self.timestamp_settings
        )
        self.timestamp_server_name_box_label.setEnabled(True)
        self.timestamp_server_name_box_label.setStyleSheet("")
        self.timestamp_server_name_box_label.setObjectName(
            "timestamp_server_name_box_label"
        )
        self.timestamp_server_name_box.addWidget(self.timestamp_server_name_box_label)
        self.timestamp_server_name = QtWidgets.QLineEdit(parent=self.timestamp_settings)
        self.timestamp_server_name.setMinimumSize(QtCore.QSize(0, 30))
        self.timestamp_server_name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.timestamp_server_name.setObjectName("timestamp_server_name")
        self.timestamp_server_name_box.addWidget(self.timestamp_server_name)
        self.server_timestamp_configuration.addLayout(self.timestamp_server_name_box)
        self.timestamp_certificate_url_box = QtWidgets.QVBoxLayout()
        self.timestamp_certificate_url_box.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.timestamp_certificate_url_box.setContentsMargins(0, -1, -1, -1)
        self.timestamp_certificate_url_box.setSpacing(5)
        self.timestamp_certificate_url_box.setObjectName(
            "timestamp_certificate_url_box"
        )
        self.timestamp_certificate_url_box_label = QtWidgets.QLabel(
            parent=self.timestamp_settings
        )
        self.timestamp_certificate_url_box_label.setMaximumSize(
            QtCore.QSize(118, 16777215)
        )
        self.timestamp_certificate_url_box_label.setObjectName(
            "timestamp_certificate_url_box_label"
        )
        self.timestamp_certificate_url_box.addWidget(
            self.timestamp_certificate_url_box_label
        )
        self.timestamp_certificate_url = QtWidgets.QLineEdit(
            parent=self.timestamp_settings
        )
        self.timestamp_certificate_url.setMinimumSize(QtCore.QSize(0, 30))
        self.timestamp_certificate_url.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.timestamp_certificate_url.setStyleSheet(
            "background-color: rgb(33, 37, 43);"
        )
        self.timestamp_certificate_url.setFrame(True)
        self.timestamp_certificate_url.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.timestamp_certificate_url.setObjectName("timestamp_certificate_url")
        self.timestamp_certificate_url_box.addWidget(self.timestamp_certificate_url)
        self.server_timestamp_configuration.addLayout(
            self.timestamp_certificate_url_box
        )
        self.pec_settings_layout_2.addLayout(self.server_timestamp_configuration)
        self.verticalLayout_7.addWidget(self.timestamp_settings)
        spacerItem12 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_7.addItem(spacerItem12)
        self.tabs.addWidget(self.timestamp)
        self.verticalLayout.addWidget(self.tabs)
        self.buttons = QtWidgets.QFrame(parent=self.pages_container)
        self.buttons.setMaximumSize(QtCore.QSize(16777215, 40))
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem13 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem13)
        self.save_button = QtWidgets.QPushButton(parent=self.buttons)
        self.save_button.setEnabled(True)
        self.save_button.setMinimumSize(QtCore.QSize(80, 30))
        self.save_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.save_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_6.addWidget(self.save_button)
        spacerItem14 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem14)
        self.cancel_button = QtWidgets.QPushButton(parent=self.buttons)
        self.cancel_button.setEnabled(True)
        self.cancel_button.setMinimumSize(QtCore.QSize(80, 30))
        self.cancel_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.cancel_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.cancel_button.setStyleSheet(
            ":disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_6.addWidget(self.cancel_button)
        self.verticalLayout.addWidget(self.buttons)
        self.horizontalLayout_4.addWidget(self.pages_container)
        self.verticalLayout_6.addWidget(self.content)
        self.bottom_bar = QtWidgets.QFrame(parent=self.content_bottom)
        self.bottom_bar.setMinimumSize(QtCore.QSize(0, 22))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.credits_label = QtWidgets.QLabel(parent=self.bottom_bar)
        self.credits_label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.credits_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.credits_label.setObjectName("credits_label")
        self.horizontalLayout_5.addWidget(self.credits_label)
        self.version = QtWidgets.QLabel(parent=self.bottom_bar)
        self.version.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.version.setObjectName("version_label")
        self.horizontalLayout_5.addWidget(self.version)
        self.frame_size_grip = QtWidgets.QFrame(parent=self.bottom_bar)
        self.frame_size_grip.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottom_bar)
        self.verticalLayout_2.addWidget(self.content_bottom)
        self.bgAppLayout.addWidget(self.content_box)
        self.styleSheetLayout.addWidget(self.bg_app)

        self.retranslateUi(fit_configuration)
        self.tabs.setCurrentIndex(2)
        self.report_language.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(fit_configuration)

    def retranslateUi(self, fit_configuration):
        _translate = QtCore.QCoreApplication.translate
        fit_configuration.setWindowTitle(
            _translate("fit_configuration", "FIT Configuration")
        )
        self.title_right_info_label.setText(
            _translate("fit_configuration", "Configuration")
        )
        self.cases_folder_path.setPlaceholderText(
            _translate("fit_configuration", "Cases Folder")
        )
        self.cases_folder_button.setText(_translate("fit_configuration", "Open"))
        self.home_page_url.setPlaceholderText(
            _translate("fit_configuration", "Home page")
        )
        self.user_agent.setPlaceholderText(
            _translate("fit_configuration", "User Agent")
        )
        self.user_agent_button.setText(_translate("fit_configuration", "Defalut"))
        self.types_proceedings.setPlaceholderText(
            _translate(
                "fit_configuration",
                "Proceedings Type List (comma character is separator)",
            )
        )
        self.types_proceedings_info_label.setText(
            _translate(
                "fit_configuration",
                "Proceedings Type List (comma character is separator)",
            )
        )
        self.db_path.setPlaceholderText(_translate("fit_configuration", "DB Folder"))
        self.db_path_info_label.setText(
            _translate("fit_configuration", "DB path readOnly")
        )
        self.language_label.setText(_translate("fit_configuration", "Report Language"))
        self.enable_network_tools_box_label.setText(
            _translate("fit_configuration", "Enable network tools")
        )
        self.whois.setText(_translate("fit_configuration", "Whois"))
        self.nslookup.setText(_translate("fit_configuration", "Nslookup"))
        self.headers.setText(_translate("fit_configuration", "Headers"))
        self.traceroute.setText(_translate("fit_configuration", "Traceroute"))
        self.ssl_keylog.setText(_translate("fit_configuration", "SSLkeylog"))
        self.ssl_certificate.setText(_translate("fit_configuration", "SSLCertificate"))
        self.ntp_server_label.setText(_translate("fit_configuration", "NTP server"))
        self.ntp_server.setPlaceholderText(
            _translate("fit_configuration", "ntp.example.com")
        )
        self.nslookup_configuration_label.setText(
            _translate("fit_configuration", "Nslookup config")
        )
        self.nslookup_dns_server.setPlaceholderText(
            _translate("fit_configuration", "1.1.1.1")
        )
        self.nslookup_enable_tcp.setText(_translate("fit_configuration", "Enable TCP"))
        self.nslookup_enable_verbose_mode.setText(
            _translate("fit_configuration", "Verbose")
        )
        self.enable_packet_capture_recorder.setText(
            _translate("fit_configuration", "Enable packet capture recorder")
        )
        self.packet_capture_recorder_filename.setPlaceholderText(
            _translate("fit_configuration", "filename.pcap")
        )
        self.enable_pec.setText(_translate("fit_configuration", "Enable PEC"))
        self.credentials_configuration_label.setText(
            _translate("fit_configuration", "Credentials")
        )
        self.pec_email.setPlaceholderText(
            _translate("fit_configuration", "example@example.com")
        )
        self.pec_password.setPlaceholderText(
            _translate("fit_configuration", "password")
        )
        self.retries_eml_download_label.setText(
            _translate("fit_configuration", "Retries EML download")
        )
        self.server_configuration_label.setText(
            _translate("fit_configuration", "Server configuration")
        )
        self.pec_imap_server.setPlaceholderText(
            _translate("fit_configuration", "imap.server.com")
        )
        self.pec_imap_server_port.setPlaceholderText(
            _translate("fit_configuration", "993")
        )
        self.verification_imap_button.setText(
            _translate("fit_configuration", "Verify IMAP Server")
        )
        self.pec_smtp_server.setPlaceholderText(
            _translate("fit_configuration", "smtp.server.com")
        )
        self.pec_smtp_server_port.setPlaceholderText(
            _translate("fit_configuration", "465")
        )
        self.verification_smtp_button.setText(
            _translate("fit_configuration", "Verify SMTP Server")
        )
        self.enable_screen_recorder.setText(
            _translate("fit_configuration", "Enable screen recoder")
        )
        self.enable_audio_recording.setText(
            _translate("fit_configuration", "Enable audio recording")
        )
        self.verify_audio_setting_button.setText(
            _translate("fit_configuration", "Verify Audio Setting")
        )
        self.temporary_msg_label.setText(
            _translate(
                "fit_configuration",
                '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline; color:#fc0107;">Enable audio recording is temporary information and will not be saved, so once you quit from FIT it will be lost.</span><span style=" color:#fc0107;"/></p></body></html>',
            )
        )
        self.screen_recorder_filename.setPlaceholderText(
            _translate("fit_configuration", "filename.avi")
        )
        self.enable_timestamp.setText(
            _translate("fit_configuration", "Enable timestamp")
        )
        self.timestamp_server_name_box_label.setText(
            _translate("fit_configuration", "Sever name")
        )
        self.timestamp_certificate_url_box_label.setText(
            _translate("fit_configuration", "Certificate URL")
        )
        self.save_button.setText(_translate("fit_configuration", "Save"))
        self.cancel_button.setText(_translate("fit_configuration", "Cancel"))
        self.credits_label.setText(
            _translate("fit_configuration", "By: fit-project.org")
        )
        self.version.setText(_translate("fit_configuration", "v1.0.3"))
