import pymysql


class Mysql_Object():
    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def select_sql(self, sql, size=0):
        '''
        查询sql语句
        :param sql 传入查询的sql语句，字符串
        :param size 返回结果的记录条数，如果没有输入默认输出全部条数
        :return: self.count 返回查询的记录的总数，slef.res 返回查询的结果
        '''
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                   port=self.port, charset=self.charset)
        self.cur = self.con.cursor()  # 建立游标
        self.sql = sql
        # 判读是否是查询语句
        if self.sql.startswith('select'):
            self.cur.execute(self.sql)  # 获取数据库结果
            self.count = self.cur.rowcount  # 统计查询记录数
            # 通过if语句进行判断
            if size == 0:
                self.res = self.cur.fetchall()  # 输出全部结果
            elif size != 0:
                self.res = self.cur.fetchmany(size)  # 输出指定数值

            self.cur.close()
            self.con.close()  # 关闭连接
        return self.count, self.res

    def excute_sql(self, sql, x):
        '''
        :param sql 输入增删改的sql语句
        :return:
        '''
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                   database=self.database,
                                   charset=self.charset, autocommit=True)
        self.cur = self.con.cursor()  # 建立游标
        self.sql = sql
        self.x = x

        if self.sql.startswith('insert'):
            print('插入语句', self.sql, self.x)
            self.cur.execute(self.sql, self.x)  # 执行语句
            self.con.commit()
            self.cur.close()  # 关闭连接
            self.con.close()
        if self.sql.startswith('delete'):
            print('删除语句', self.sql)
            self.cur.execute(self.sql)  # 执行语句
            self.con.commit()
            self.cur.close()  # 关闭连接
            self.con.close()
        if self.sql.startswith('update'):
            print('更新语句', self.sql)
            self.cur.execute(self.sql, self.x)  # 执行语句
            self.con.commit()
            self.cur.close()  # 关闭连接
            self.con.close()

    def create_table(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                   port=self.port, charset=self.charset)
        self.cur = self.con.cursor()
        sql = '''create table words(
            SNO varchar(10),
            STEXT varchar(10000) NOT NULL,   
            primary key(SNO)
            )default charset=utf8;'''
        self.cur.execute(sql)

# 调用
# m = Mysql_Object('180.215.203.169', 'nodek40dym9wuqvr', 'Fy123456', 'nodek40dym9wuqvr')
# print(m.select_sql('select * from sscore', 0))  # 查询结果
# m.excute_sql('update sscore set name="王六"where `name`="张三"')  # 更新语句
# m.excute_sql('delete from sscore where name="李四"')  # 删除语句
# m.excute_sql('insert into sscore VALUES("赵七","英语","89")')  # 插入语句
# m.create_table()
