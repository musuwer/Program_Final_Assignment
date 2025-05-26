from PyQt5 import QtWidgets, QtCore
import sys
from test3 import Ui_MainWindow  # 替换成你的 py 文件名

class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self._isTracking = False
        self._startPos = None

    # 鼠标按下
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    # 鼠标移动
    def mouseMoveEvent(self, event):
        if self._isTracking and event.buttons() & QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self._startPos)
            event.accept()

    # 鼠标释放
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    # 设置无边框和透明背景
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    window.show()
    sys.exit(app.exec_())
