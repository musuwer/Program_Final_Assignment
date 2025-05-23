import sqlite3
from util.common_util import get_uuid, get_current_time

class DBHelp(object):
    instance = None

    def __init__(self, db_path='data.db'):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def db_commit(self):
        self.conn.commit()

    def db_rollback(self):
        self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()

    # 通用插入
    def insert(self, table, fields, values):
        sql = f"INSERT INTO {table} ({', '.join(fields)}) VALUES ({', '.join(['?' for _ in values])})"
        self.cur.execute(sql, values)

    # 查询全部
    def query_all(self, table):
        self.cur.execute(f"SELECT * FROM {table}")
        rows = self.cur.fetchall()
        return len(rows), rows

    # 条件查询
    def query_super(self, table, col, value):
        self.cur.execute(f"SELECT * FROM {table} WHERE {col} = ?", (value,))
        rows = self.cur.fetchall()
        return len(rows), rows

    # 搜索（模糊）
    def query_search(self, table, col, key):
        self.cur.execute(f"SELECT * FROM {table} WHERE {col} LIKE ?", (f"%{key}%",))
        rows = self.cur.fetchall()
        return len(rows), rows

    # 更新
    def update(self, table, update_dict, key_col, key_val):
        set_clause = ', '.join([f"{k}=?" for k in update_dict.keys()])
        values = list(update_dict.values())
        values.append(key_val)
        sql = f"UPDATE {table} SET {set_clause} WHERE {key_col}=?"
        self.cur.execute(sql, values)

    # 删除
    def delete(self, table, key_col, key_val):
        self.cur.execute(f"DELETE FROM {table} WHERE {key_col} = ?", (key_val,))

    # 用户相关
    def add_user(self, user_info):
        sql = "INSERT INTO user (id, username, password, role, create_time, delete_flag, current_login_time) VALUES (?, ?, ?, ?, ?, ?, ?)"
        self.cur.execute(sql, user_info)

    # 成就相关
    def add_achievement(self, ach_info):
        sql = "INSERT INTO achievement (id, username, title, category, score, feelings, achieve_date, record_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cur.execute(sql, ach_info)

    # 事件相关
    def add_event(self, evt_info):
        sql = "INSERT INTO event (id, username, title, content, event_date, category) VALUES (?, ?, ?, ?, ?, ?)"
        self.cur.execute(sql, evt_info)

    # 心情记录
    def add_mood(self, mood_info):
        sql = "INSERT INTO mood (id, username, mood_name, proportion, mood_date) VALUES (?, ?, ?, ?, ?)"
        self.cur.execute(sql, mood_info)

    # 目标
    def add_goal(self, goal_info):
        sql = "INSERT INTO goal (id, username, title, description, due_date, status) VALUES (?, ?, ?, ?, ?, ?)"
        self.cur.execute(sql, goal_info)

    # 公告
    def insert_announcement(self, ann_info):
        sql = "INSERT INTO announcement (id, title, content, time) VALUES (?, ?, ?, ?)"
        self.cur.execute(sql, ann_info)

    # 消息
    def insert_message(self, msg_info):
        sql = "INSERT INTO message (id, sender_name, receiver_name, send_content, send_time, is_replied, reply_content, reply_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cur.execute(sql, msg_info)

    # 查询所有公告
    def query_announcement(self):
        self.cur.execute("SELECT * FROM announcement ORDER BY time DESC")
        return self.cur.fetchall()

    # 查询所有消息
    def query_message_super(self):
        self.cur.execute("SELECT * FROM message ORDER BY send_time DESC")
        return self.cur.fetchall()

    def query_user_message(self, username):
        self.cur.execute("SELECT * FROM message WHERE receiver_name=? ORDER BY send_time DESC", (username,))
        return self.cur.fetchall()

    # 修改密码
    def update_password(self, username, new_password):
        self.cur.execute("UPDATE user SET password=? WHERE username=?", (new_password, username))

    # 单个字段查重
    def check_exist(self, table, field, value):
        self.cur.execute(f"SELECT COUNT(1) FROM {table} WHERE {field} = ?", (value,))
        return self.cur.fetchone()[0]

    # 单字段唯一查
    def get_one(self, table, key_col, key_val):
        self.cur.execute(f"SELECT * FROM {table} WHERE {key_col} = ?", (key_val,))
        return self.cur.fetchone()

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass
