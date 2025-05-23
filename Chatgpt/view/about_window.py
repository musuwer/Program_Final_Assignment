"""
文件名：about_window.py
描述：关于页面
"""

# view/about_window.py

from PyQt5.QtWidgets import QWidget
from ui.about_window import Ui_Form

class AboutWindow(Ui_Form, QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)
        # 修改为忆途软件的介绍
        self.textBrowser.setText(
            "忆途 - 人生成长与成就记录软件\n\n"
            "功能简介：\n"
            "- 事件记录：随时记录人生每一个重要时刻\n"
            "- 成就记录：详细保存你获得的每项成就与心得\n"
            "- 心情日历：用可视化日历标记每天的心情\n"
            "- 目标设定：设定和追踪你的成长目标\n"
            "\n"
            "本软件致力于帮助你更好地回顾和规划自己的人生旅程。"
        )
