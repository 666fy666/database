import pymysql

# 连接数据库，并打开数据库（数据库已创建）
db = pymysql.connect(host='180.215.203.169', port=3306,
                     user='nodek40dym9wuqvr', password='Fy123456',
                     charset='utf8', db='nodek40dym9wuqvr')

# 创建游标对象
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM am"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        num = row[0]
        name = row[1]
        print(name)
        # 打印结果

except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()