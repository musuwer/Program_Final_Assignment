import sqlite3
import os
from util.common_util import get_uuid, get_current_time

DB_PATH = 'data.db'

def create_tables(conn):
    cur = conn.cursor()

    # 用户表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id TEXT PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        role INTEGER,
        create_time TEXT,
        delete_flag INTEGER,
        current_login_time TEXT
    )''')

    # 成就记录表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS achievement (
        id TEXT PRIMARY KEY,
        username TEXT,
        title TEXT,
        category TEXT,
        score INTEGER,
        feelings TEXT,
        achieve_date TEXT,
        record_time TEXT
    )''')

    # 事件记录表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS event (
        id TEXT PRIMARY KEY,
        username TEXT,
        title TEXT,
        content TEXT,
        event_date TEXT,
        category TEXT
    )''')

    # 心情日历表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS mood (
        id TEXT PRIMARY KEY,
        username TEXT,
        mood_name TEXT,
        proportion INTEGER,
        mood_date TEXT
    )''')

    # 目标表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS goal (
        id TEXT PRIMARY KEY,
        username TEXT,
        title TEXT,
        description TEXT,
        due_date TEXT,
        status INTEGER
    )''')

    # 公告表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS announcement (
        id TEXT PRIMARY KEY,
        title TEXT,
        content TEXT,
        time TEXT
    )''')

    # 消息表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS message (
        id TEXT PRIMARY KEY,
        sender_name TEXT,
        receiver_name TEXT,
        send_content TEXT,
        send_time TEXT,
        is_replied INTEGER,
        reply_content TEXT,
        reply_time TEXT
    )''')

    conn.commit()


def insert_sample_data(conn):
    cur = conn.cursor()

    # 管理员用户
    cur.execute('INSERT OR IGNORE INTO user VALUES (?, ?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'admin', 'admin', 0, get_current_time(), 0, get_current_time()))
    # 普通用户
    cur.execute('INSERT OR IGNORE INTO user VALUES (?, ?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '123456', 1, get_current_time(), 0, get_current_time()))

    # 成就记录
    cur.execute('INSERT OR IGNORE INTO achievement VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '大学毕业', '教育', 100, '非常自豪', '2020-06-30', get_current_time()))
    cur.execute('INSERT OR IGNORE INTO achievement VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '完成10公里跑步', '运动', 80, '挑战自己', '2021-04-01', get_current_time()))

    # 事件记录
    cur.execute('INSERT OR IGNORE INTO event VALUES (?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '去北京旅游', '登上长城', '2021-10-01', '旅游'))
    cur.execute('INSERT OR IGNORE INTO event VALUES (?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '获得奖学金', '大学期间获得优秀奖学金', '2020-09-01', '教育'))

    # 心情日历
    cur.execute('INSERT OR IGNORE INTO mood VALUES (?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '开心', 70, '2024-05-21'))
    cur.execute('INSERT OR IGNORE INTO mood VALUES (?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '焦虑', 30, '2024-05-21'))

    # 目标
    cur.execute('INSERT OR IGNORE INTO goal VALUES (?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '考研成功', '顺利考上目标研究生院校', '2025-07-01', 0))
    cur.execute('INSERT OR IGNORE INTO goal VALUES (?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'zhangsan', '坚持锻炼半年', '每周至少三次运动', '2024-12-31', 1))

    # 公告
    cur.execute('INSERT OR IGNORE INTO announcement VALUES (?, ?, ?, ?)',
                (get_uuid(), '系统公告', '欢迎使用忆途软件！', get_current_time()))
    cur.execute('INSERT OR IGNORE INTO announcement VALUES (?, ?, ?, ?)',
                (get_uuid(), '重要更新', '新增目标与心情日历模块', get_current_time()))

    # 消息
    cur.execute('INSERT OR IGNORE INTO message VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                (get_uuid(), 'admin', 'zhangsan', '欢迎使用忆途，如有问题随时联系管理员。', get_current_time(), 0, '', ''))

    conn.commit()


def main():
    if not os.path.exists(DB_PATH):
        print("正在创建数据库和表...")
    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)
    insert_sample_data(conn)
    conn.close()
    print('数据库初始化完成，样例数据已插入。')


if __name__ == '__main__':
    main()
