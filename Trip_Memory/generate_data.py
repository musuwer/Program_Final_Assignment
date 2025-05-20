"""
文件名：generate_data.py
描述：使用MySQL在本地连接，新建数据库book及相关表，包含表结构定义和可选的示例数据插入功能
注意事项：运行前需确保已安装pymysql库（可通过pip install pymysql安装），并正确配置数据库连接参数
"""

# 导入MySQL连接库，用于操作MySQL数据库
import pymysql
# 导入异常追踪模块，用于在出错时打印详细堆栈信息
import traceback

# ---------------------- 数据库连接参数配置 ---------------------- #
# 本地数据库主机地址（默认localhost）
host = 'localhost'
port = 3306# 数据库端口（默认3306）
user = 'root'# 数据库用户名（默认root）
password = '111111'  # 数据库密码（需根据实际环境修改，此处为示例密码）


# 以下为手动输入参数的注释代码（默认使用上方固定参数，如需动态输入可取消注释）
# print('Starting the create database operation, please enter the information required for the database.')
# print('------------------------------------')
# host = input('please input database host:')
# port = input('please input database port:')
# user = input('please input database user:')
# password = input('please input database password:')
# print('------------------------------------')


# ---------------------- 数据库与表结构创建逻辑 ---------------------- #
try:
    # 建立数据库连接（使用pymysql.connect方法，参数包括主机、端口、用户名、密码）
    conn = pymysql.connect(host=host, port=int(port), user=user, password=password)
    print('create database...')
    # 创建游标对象，用于执行SQL语句
    cur = conn.cursor()
    # 创建数据库book（if not exists确保数据库不存在时才创建）
    cur.execute('create database if not exists book')
    print('database created done.')
    print('------------------------------------')

    # 切换到book数据库（后续操作均在此数据库中执行）
    conn.select_db('dbchai1')

    # ---------------------- 创建用户表 ---------------------- #
    print('create user table...')
    # 用户表结构说明：
    # - id: 唯一标识（字符串类型，主键）
    # - username: 用户名（字符串）
    # - password: 密码（字符串，建议存储加密后的哈希值）
    # - role: 用户角色（0=管理员，1=普通用户）
    # - create_time: 创建时间（ datetime类型）
    # - delete_flag: 逻辑删除标志（0=未删除，1=已删除）
    # - current_login_time: 最后登录时间（ datetime类型）
    cur.execute("CREATE TABLE IF NOT EXISTS user ("
                "id varchar(50) PRIMARY KEY,"
                "username varchar(255),"
                "password varchar(255),"
                "role int(11),"
                "create_time datetime,"
                "delete_flag int(11),"
                "current_login_time datetime)")
    print('user table created done.')
    print('------------------------------------')

    # ---------------------- 创建书籍表 ---------------------- #
    print('create book table...')
    # 书籍表结构说明：
    # - id: 书籍唯一标识（字符串，主键）
    # - book_name: 书名（字符串）
    # - author: 作者（字符串）
    # - publish_company: 出版社（字符串）
    # - store_number: 库存量（整数）
    # - borrow_number: 已借阅数量（整数）
    # - create_time: 录入时间（ datetime类型）
    # - publish_date: 出版日期（ date类型）
    cur.execute("CREATE TABLE IF NOT EXISTS book("
                "id varchar(50) PRIMARY KEY,"
                "book_name varchar(255),"
                "author varchar(255),"
                "publish_company varchar(255),"
                "store_number int(11),"
                "borrow_number int(11),"
                "create_time datetime,"
                "publish_date date)")
    print('book table created done.')
    print('------------------------------------')

    # ---------------------- 创建借阅信息表 ---------------------- #
    print('create borrow_info table...')
    # 借阅信息表结构说明：
    # - id: 借阅记录唯一标识（字符串，主键）
    # - book_id: 书籍ID（关联book表的id）
    # - book_name: 书名（冗余存储，方便查询）
    # - borrow_user: 借阅用户（用户名）
    # - borrow_num: 借阅数量（整数）
    # - borrow_days: 借阅天数（用于计算归还时间）
    # - borrow_time: 借阅时间（ datetime类型）
    # - return_time: 归还时间（ datetime类型，未归还时为NULL）
    # - return_flag: 归还状态（0=未归还，1=已归还）
    cur.execute("CREATE TABLE IF NOT EXISTS borrow_info ("
                "id varchar(50) PRIMARY KEY,"
                "book_id varchar(50),"
                "book_name varchar(255),"
                "borrow_user varchar(255),"
                "borrow_num int(11),"
                "borrow_days int(11),"
                "borrow_time datetime,"
                "return_time datetime,"
                "return_flag int(11))")
    print('borrow_info table created done.')
    print('------------------------------------')

    # ---------------------- 创建消息表 ---------------------- #
    print('create message table...')
    # 消息表结构说明：
    # - id: 消息唯一标识（字符串，主键）
    # - sender_name: 发送者姓名（非空字符串）
    # - receiver_name: 接收者姓名（非空字符串）
    # - send_content: 消息内容（非空字符串）
    # - send_time: 发送时间（ datetime类型）
    # - is_replied: 是否回复（0=未回复，1=已回复）
    # - reply_content: 回复内容（字符串，未回复时为NULL）
    # - reply_time: 回复时间（ datetime类型，未回复时为NULL）
    cur.execute("create table if not exists message ("
                "id varchar(50) PRIMARY KEY,"
                "sender_name varchar(255) NOT NULL,"
                "receiver_name varchar(255) NOT NULL,"
                "send_content varchar(255) NOT NULL,"
                "send_time datetime,"
                "is_replied int(11),"
                "reply_content varchar(255),"
                "reply_time datetime)")
    print('message table created done.')

    # ---------------------- 创建公告表 ---------------------- #
    print('create annoucement table...')
    # 公告表结构说明：
    # - id: 公告唯一标识（字符串，主键）
    # - annouce_title: 公告标题（非空字符串）
    # - annouce_content: 公告内容（非空字符串）
    # - annouce_time: 发布时间（ datetime类型，默认NULL）
    cur.execute("create table if not exists annoucement ("
                "  `id` varchar(50) NOT NULL,"
                "`annouce_title` varchar(255) NOT NULL,"
                "`annouce_content` varchar(255) NOT NULL,"
                " `annouce_time` datetime DEFAULT NULL,"
                "PRIMARY KEY (`id`))")
    print('annoucement table created done.')

    # ---------------------- 创建豆瓣书籍表（用于存储外部数据） ---------------------- #
    print('create douban_book table...')
    # 豆瓣书籍表结构说明：
    # - img_href: 书籍封面链接（字符串，默认NULL）
    # - title: 书名（字符串，默认NULL）
    # - author: 作者（字符串，默认NULL）
    # - pub: 出版社（字符串，默认NULL）
    # - pub_year: 出版年份（字符串，默认NULL）
    # - price: 价格（字符串，默认NULL）
    # - grade: 评分（字符串，默认NULL）
    # - remark_num: 评论数（字符串，默认NULL）
    # - quote: 简介（字符串，默认NULL）
    cur.execute("create table if not exists douban_book ("
                ' `img_href` varchar(255) DEFAULT NULL,'
                ' `title` varchar(255) DEFAULT NULL,'
                ' `author` varchar(255) DEFAULT NULL,'
                '`pub` varchar(255) DEFAULT NULL,'
                '  `pub_year` varchar(255) DEFAULT NULL,'
                '  `price` varchar(255) DEFAULT NULL,'
                ' `grade` varchar(255) DEFAULT NULL,'
                ' `remark_num` varchar(255) DEFAULT NULL,'
                '  `quote` varchar(255) DEFAULT NULL)')
    print('douban_book table created done.')

    print('-' * 30)
    print('operate done.')
    print('create database successfully.')

# ---------------------- 异常处理 ---------------------- #
except Exception as e:
    print('数据库连接或表创建失败，请检查数据库配置和SQL语句是否正确:')
    print('错误信息:', e.args)         # 打印具体错误参数
    traceback.print_exc()              # 打印完整异常堆栈
    print('create database failed.')


# ---------------------- 可选的示例数据插入功能 ---------------------- #
print('是否向数据库中插入示例数据？（用于快速测试）')
print('1. 插入示例数据')
print('2. 退出')
insert_tag = input('请选择操作（输入数字）:')

if insert_tag == '1':
    print('------------------------------------')
    print('开始插入示例数据...')

    # ---------------------- 示例用户数据 ---------------------- #
    # 管理员账号（role=0）：
    # - 密码为"admin"的MD5哈希值（21232f297a57a5a743894a0e4a801fc3）
    # - delete_flag=0表示未删除，current_login_time为模拟时间
    admin_data = [
        '12644064935811ea9063d8c497639e371',  # 唯一ID（可使用UUID生成）
        'admin1',                            # 用户名
        '21232f297a57a5a743894a0e4a801fc31',  # 密码（admin的MD5）
        0,                                  # 角色（0=管理员）
        '2021-06-01 15:23:12',              # 创建时间
        0,                                  # 逻辑删除标志
        '2021-06-01 15:24:23'               # 最后登录时间
    ]

    # 普通用户账号（role=1）：
    # - 密码为"123456"的MD5哈希值（e10adc3949ba59abbe56e057f20f883e）
    user_data = [
        '99477a9e935811ea8171d8c497639e371',  # 唯一ID
        'zhangsan1',                         # 用户名
        'e10adc3949ba59abbe56e057f20f883e1',  # 密码（123456的MD5）
        1,                                  # 角色（1=普通用户）
        '2021-06-03 15:23:12',              # 创建时间
        0,                                  # 逻辑删除标志
        '2021-06-03 15:24:23'               # 最后登录时间
    ]

    # ---------------------- 执行插入操作 ---------------------- #
    # SQL语句使用参数化查询，防止SQL注入
    sql = 'insert into user (id, username, password, role, create_time, delete_flag, current_login_time) values(%s,%s,%s,%s,%s,%s,%s)'
    cur.execute(sql, admin_data)  # 插入管理员数据
    cur.execute(sql, user_data)    # 插入普通用户数据

    conn.commit()       # 提交事务（确保数据持久化）
    cur.close()         # 关闭游标
    conn.close()        # 关闭数据库连接

    print('insert operation done.')
    print('------------------------------------')
    print('示例账号信息：')
    print(' - 管理员：用户名=admin，密码=admin')
    print(' - 普通用户：用户名=zhangsan，密码=123456')

    #这里Print应该改成和系统插入的数据一致
else:
    print('system exit.')