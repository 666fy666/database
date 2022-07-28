import pymysql

# 连接数据库，并打开数据库（数据库已创建）
db = pymysql.connect(host='180.215.203.169', port=3306,
                     user='nodek40dym9wuqvr', password='Fy123456',
                     charset='utf8', db='nodek40dym9wuqvr')

# 创建游标对象
cursor = db.cursor()

try:
    # 创建student表，并执行
    # sql = '''create table student(
    # SNO char(10),
    # SNAME varchar(20) NOT NULL,
    # SSEX varchar(1),
    # primary key(SNO)
    # )default charset=utf8;'''
    # cursor.execute(sql)
    try:
        sql = '''create table pm(
            SNO varchar(10),
            STEXT varchar(10000) NOT NULL,   
            primary key(SNO)
            )default charset=utf8;'''
        cursor.execute(sql)
    except:
        pass

    with open("pm.txt", 'r+', encoding='utf-8') as f_acc:
        acc_ar = f_acc.read().splitlines()
    for i in range(len(acc_ar)):
        # 插入一条数据，并执行
        b = acc_ar[i]
        print(b)
        insert_sql = '''
          insert into pm values(%s,%s)
          '''
        cursor.execute(insert_sql, (i,b))

        # 将数据提交给数据库（加入数据，修改数据要先提交）
        db.commit()

    # 执行查询语句
    cursor.execute('select * from pm')

    # 打印全部数据
    all = cursor.fetchall()
    for i in all:
        print(i)

# 发生错误时，打印报错原因
except Exception as e:
    print(e)

# 无论是否报错都执行
finally:
    cursor.close()
    db.close()
