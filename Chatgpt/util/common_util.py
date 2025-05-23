import uuid
import datetime
import re
from PyQt5.QtWidgets import QMessageBox

ROLE_MAP = {
    '管理员': 0,
    '普通用户': 1
}

# “忆途”专用：搜索下拉菜单映射（对应事件、成就、目标模块字段）
SEARCH_CONTENT_MAP = {
    '事件标题': 'title',
    '事件类别': 'category',
    '事件时间': 'event_date',
    '成就名称': 'title',
    '成就类型': 'category',
    '成就得分': 'score',
    '成就日期': 'achieve_date',
    '心情日期': 'mood_date',
    '目标名称': 'title',
    '目标状态': 'status',
    '用户': 'username'
}

# 正则：仅允许字母数字、正整数、日期
PATTERNS = [
    r'^[A-Za-z0-9\u4e00-\u9fa5]+$',   # 字母数字和中文
    r'^[1-9]\d*$',                   # 正整数
    r'^\d{4}-\d{2}-\d{2}$',          # 日期 2022-12-31
]

def get_uuid():
    return str(uuid.uuid1()).replace('-', '')

def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def msg_box(parent, title, content):
    QMessageBox.information(parent, title, content)

def get_current_time():
    """
    获取当前时间
    :return: 格式化的当前时间
    """
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return dt


def read_qss(qss_file):
    """
    读取自定义样式文件
    :param qss_file: 文件路径
    :return: 文件内容
    """
    with open(qss_file, 'r', encoding='utf-8') as f:
        return f.read()


def get_return_day(day):
    """
    获取已知天数后的日期
    :param day: 离当天相差的天数
    :return: 计算后的日期
    """
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')


