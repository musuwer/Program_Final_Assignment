from PyQt5.QtWidgets import QWidget
from ui.mood_calendar_window import Ui_Form
import calendar
from datetime import datetime

class MoodCalendarWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_month_calendar()

    def fill_month_calendar(self):
        now = datetime.now()
        year = now.year
        month = now.month
        day_today = now.day

        # 获取本月天数
        _, days_in_month = calendar.monthrange(year, month)  # 第一个返回本月1号是周几（0=周一）
        first_weekday = calendar.monthrange(year, month)[0]  # 0=周一, 6=周日

        # 构建控件列表，行优先
        textEdit_grid = [
            [self.textEdit,   self.textEdit_6,  self.textEdit_3,  self.textEdit_5,  self.textEdit_4,  self.textEdit_2,  self.textEdit_7],
            [self.textEdit_8, self.textEdit_9,  self.textEdit_10, self.textEdit_11, self.textEdit_12, self.textEdit_13, self.textEdit_14],
            [self.textEdit_15,self.textEdit_16, self.textEdit_17, self.textEdit_18, self.textEdit_19, self.textEdit_20, self.textEdit_21],
            [self.textEdit_22,self.textEdit_23, self.textEdit_24, self.textEdit_25, self.textEdit_26, self.textEdit_27, self.textEdit_28],
            [self.textEdit_35,self.textEdit_29, self.textEdit_30, self.textEdit_31, self.textEdit_32, self.textEdit_33, self.textEdit_34],
        ]
        # 全部清空
        for row in textEdit_grid:
            for cell in row:
                cell.clear()
                cell.setStyleSheet("")

        # 把每一天放入对应的格子（以周日为第一列，周六为最后一列）
        for day in range(1, days_in_month + 1):
            # 获取该天的星期，0=周一，6=周日。我们要把周日放到最左边
            dt = datetime(year, month, day)
            weekday = dt.weekday()  # 0=周一...6=周日
            # 让周日为0，周一为1，... 周六为6
            col = (weekday + 1) % 7  # 使得0=周日
            # 第几周（从0开始）：本月1号在第几天的星期（周一是0，周日是6）
            week = (day + (first_weekday + 1) % 7 - 1) // 7
            # week: 当前日期在第几行（从0开始）
            # col: 当前星期几（0=周日）

            # 显示内容和高亮
            if day == day_today:
                textEdit_grid[week][col].setText(f"{day}")
                textEdit_grid[week][col].setStyleSheet("background-color: yellow; font-weight: bold;")
            else:
                textEdit_grid[week][col].setText(str(day))
                textEdit_grid[week][col].setStyleSheet("")
