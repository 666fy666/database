import random

from db import Mysql_Object

m = Mysql_Object('180.215.203.169', 'nodek40dym9wuqvr', 'Fy123456', 'nodek40dym9wuqvr')
print(m.select_sql('select * from am', 0)[0])
print(m.select_sql('select * from pm', 0)[0])
a = random.randint(0,m.select_sql('select * from am', 0)[0])
b = random.randint(0,m.select_sql('select * from pm', 0)[0])
print(m.select_sql('select * from am', 0)[1][a])
print(m.select_sql('select * from pm', 0)[1][b])