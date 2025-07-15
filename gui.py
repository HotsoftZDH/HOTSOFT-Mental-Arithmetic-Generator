# -*- coding: utf-8 -*-
"""
HOTSOFT火热口算题生成器Beta1.0
主界面GUI程序
"""

import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (QApplication, QWidget, QCheckBox, QDialogButtonBox,
                               QLabel, QRadioButton, QDoubleSpinBox, QButtonGroup)


class MainWindowUI:
    """主界面UI类"""

    def setupUi(self, Form):
        """初始化UI界面"""
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 287)

        # 控件初始化
        self._create_widgets(Form)
        self._setup_button_groups()
        self._translate_ui(Form)
        QMetaObject.connectSlotsByName(Form)

    def _create_widgets(self, Form):
        """创建所有控件"""
        # 生成答案复选框
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(160, 230, 271, 20))

        # 按钮组
        self.buttonBox = QDialogButtonBox(Form)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(120, 260, 161, 21))
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok
        )

        # 题目类型设置
        self._setup_question_type_controls(Form)
        # 运算符设置
        self._setup_operator_controls(Form)
        # 数值范围设置
        self._setup_range_controls(Form)

    def _setup_question_type_controls(self, Form):
        """设置题目类型控件"""
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 81, 16))

        # 题目类型单选按钮
        self.radioButton = QRadioButton(Form)  # 整数
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 40, 98, 20))
        self.radioButton.setChecked(True)

        self.radioButton_2 = QRadioButton(Form)  # 小数
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(170, 40, 98, 20))

        self.radioButton_3 = QRadioButton(Form)  # 分数
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(310, 40, 98, 20))

    def _setup_operator_controls(self, Form):
        """设置运算符控件"""
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 80, 51, 16))

        # 运算符单选按钮
        self.radioButton_4 = QRadioButton(Form)  # 加
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(40, 110, 98, 20))
        self.radioButton_4.setChecked(True)

        self.radioButton_5 = QRadioButton(Form)  # 减
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(110, 110, 98, 20))

        self.radioButton_6 = QRadioButton(Form)  # 乘
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(180, 110, 98, 20))

        self.radioButton_7 = QRadioButton(Form)  # 除
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(250, 110, 98, 20))

        self.radioButton_8 = QRadioButton(Form)  # 平方
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(310, 110, 98, 20))

    def _setup_range_controls(self, Form):
        """设置数值范围控件"""
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 140, 54, 16))

        # 数值范围设置
        self.doubleSpinBox = QDoubleSpinBox(Form)  # 最大值
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(80, 170, 87, 22))
        self.doubleSpinBox.setRange(0, 1000)
        self.doubleSpinBox.setValue(100)

        self.doubleSpinBox_2 = QDoubleSpinBox(Form)  # 最小值
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setGeometry(QRect(260, 170, 87, 22))
        self.doubleSpinBox_2.setRange(0, 1000)
        self.doubleSpinBox_2.setValue(0)

        # 标签
        self.label_4 = QLabel(Form)  # 最大
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 170, 54, 16))

        self.label_5 = QLabel(Form)  # 最小
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(230, 170, 54, 16))

        self.label_6 = QLabel(Form)  # 其它选项
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 200, 54, 16))

    def _setup_button_groups(self):
        """设置按钮分组"""
        # 题目类型按钮组
        self.typeButtonGroup = QButtonGroup()
        self.typeButtonGroup.addButton(self.radioButton, 1)
        self.typeButtonGroup.addButton(self.radioButton_2, 2)
        self.typeButtonGroup.addButton(self.radioButton_3, 3)

        # 运算符按钮组
        self.operatorButtonGroup = QButtonGroup()
        self.operatorButtonGroup.addButton(self.radioButton_4, 1)
        self.operatorButtonGroup.addButton(self.radioButton_5, 2)
        self.operatorButtonGroup.addButton(self.radioButton_6, 3)
        self.operatorButtonGroup.addButton(self.radioButton_7, 4)
        self.operatorButtonGroup.addButton(self.radioButton_8, 5)

    def _translate_ui(self, Form):
        """翻译UI文本"""
        Form.setWindowTitle(QCoreApplication.translate("Form", u"HOTSOFT火热口算题生成器 Beta1.0", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"答案（没做）", None))
        self.label.setText(QCoreApplication.translate("Form", u"题目类型设置", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"整数", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"小数", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"分数", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"运算符号", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"加", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"减", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"乘", None))
        self.radioButton_7.setText(QCoreApplication.translate("Form", u"除", None))
        self.radioButton_8.setText(QCoreApplication.translate("Form", u"平方", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"大小限制", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"最大", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"最小", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"其它选项", None))


class MainWindow(QWidget):
    """主窗口类"""

    def __init__(self):
        super().__init__()
        self.ui = MainWindowUI()
        self.ui.setupUi(self)
        self.user_settings = None
        self.ui.buttonBox.accepted.connect(self._on_ok_clicked)

    def _on_ok_clicked(self):
        """确定按钮点击事件处理"""
        self.user_settings = self._get_user_settings()
        self.close()

    def _get_user_settings(self):
        """获取用户设置"""
        settings = []

        # 题目类型
        if self.ui.radioButton.isChecked():
            settings.append(1)  # 整数
        elif self.ui.radioButton_2.isChecked():
            settings.append(2)  # 小数
        else:
            settings.append(3)  # 分数

        # 运算符
        if self.ui.radioButton_4.isChecked():
            settings.append(1)  # 加
        elif self.ui.radioButton_5.isChecked():
            settings.append(2)  # 减
        elif self.ui.radioButton_6.isChecked():
            settings.append(3)  # 乘
        elif self.ui.radioButton_7.isChecked():
            settings.append(4)  # 除
        else:
            settings.append(5)  # 平方

        # 数值范围
        settings.append(float(self.ui.doubleSpinBox.value()))
        settings.append(float(self.ui.doubleSpinBox_2.value()))

        # 是否生成答案
        settings.append(bool(self.ui.checkBox.isChecked()))

        return settings


def userlist():
    """获取用户设置"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    return window.user_settings
