import sqlite3
import os
import uuid
from datetime import datetime

def get_uuid():
    return str(uuid.uuid4())

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

db_path = os.path.abspath("data.db")

# ----------- 目标初始数据 -----------
init_goals = [
    [get_uuid(), "考研上岸",      "每天学习6小时",       "已坚持60天",     "获得保研资格",      get_current_time()],
    [get_uuid(), "健康减重",      "每天健身打卡1小时",   "已完成20%",      "体重下降5kg",       get_current_time()],
    [get_uuid(), "阅读50本书",    "每周完成一本",        "已读10本",       "知识储备增加",      get_current_time()],
    [get_uuid(), "省内游遍",      "每月游一个城市",      "已打卡3市",      "发现美丽家乡",      get_current_time()],
    [get_uuid(), "开发忆途软件",  "每周完成一个模块",    "UI与数据已实现", "获得编程能力提升",   get_current_time()]
]

# ----------- 公告初始数据 -----------
init_annouce = [
    [get_uuid(), "欢迎使用忆途",   "记录人生每一个重要瞬间，成就更好的自己。", get_current_time()],
    [get_uuid(), "功能更新通知",   "新增目标、事件、心情、成就多模块，欢迎体验！", get_current_time()],
    [get_uuid(), "数据安全提醒",   "请定期备份数据，防止丢失。",               get_current_time()]
]

def main():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    # 初始化goals表
    c.execute('''CREATE TABLE IF NOT EXISTS goals (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    plan TEXT,
                    progress TEXT,
                    achievement TEXT,
                    create_time TEXT
                )''')
    # 初始化公告表
    c.execute('''CREATE TABLE IF NOT EXISTS annoucement (
                    id TEXT PRIMARY KEY,
                    title TEXT,
                    content TEXT,
                    create_time TEXT
                )''')
    # 插入目标
    c.executemany('INSERT INTO goals (id, name, plan, progress, achievement, create_time) VALUES (?, ?, ?, ?, ?, ?)', init_goals)
    # 插入公告
    c.executemany('INSERT INTO annoucement (id, title, content, create_time) VALUES (?, ?, ?, ?)', init_annouce)
    conn.commit()
    conn.close()
    print("已初始化目标和公告数据！")

if __name__ == "__main__":
    main()
