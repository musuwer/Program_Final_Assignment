"""
文件名：main.py
描述：项目入口，想要演示本项目，运行本文件即可
注意事项：在运行本文件之前确保已启动了Mysql服务，并且已成功运行过generate_data.py文件
"""

# 导入登录窗口类，这是自定义的视图类，用于显示登录界面
from view.login_window import LoginWindow
# 导入PyQt5框架的核心组件，QApplication是应用程序的核心对象
from PyQt5.QtWidgets import QApplication
# 导入sys模块，用于与Python解释器进行交互，获取命令行参数和退出应用程序
import sys#11

# 程序入口点，当直接运行此脚本时执行以下代码
if __name__ == '__main__':
    # 创建PyQt应用程序对象，sys.argv传递命令行参数给应用程序
    # 这是每个PyQt应用程序必须的第一步，负责管理应用程序的资源和设置
    app = QApplication(sys.argv)

    # 创建登录窗口实例，LoginWindow是自定义的窗口类，继承自QWidget或QMainWindow
    # 该窗口包含用户登录所需的UI元素（如用户名/密码输入框、登录按钮等）
    win = LoginWindow()

    # 显示登录窗口，默认情况下窗口是隐藏的，调用show()方法将其显示在屏幕上
    win.show()

    # 进入应用程序的主事件循环，这是一个阻塞调用，会持续运行直到应用程序退出
    # app.exec_()返回应用程序的退出状态码（通常0表示正常退出）
    # sys.exit()确保将状态码正确返回给操作系统，结束Python进程
    sys.exit(app.exec_())