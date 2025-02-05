
import pymysql  # 导入操作MySQL数据库模块

# 数据库字段
'''
id          编号
name        商品名称
jd_price    京东价格
jd_id       京东商品id
hot        热卖指数 
middle_time 中评最新的时间
poor_time   差评最新的时间
'''


class MySQL(object):
    # 连接数据库
    def connection_sql(self):
        # 连接数据库
        self.db = pymysql.connect(host="localhost", user="root",
                                  password="root", db="jd_peripheral", port=3306,charset='utf8')
        return self.db

    # 关闭数据库
    def close_sql(self):
        self.db.close()

    # 排行数据插入方法,该方法可以根据更换表名插入排行数据
    def insert_ranking(self, cur, value, table):
        # 插入数据的sql语句
        sql_insert = "insert into  {table} (id,name,jd_price,jd_id,hot)" \
                     " values(%s,%s,%s,%s,%s)on duplicate" \
                     " key update name=values(name),jd_price=values(jd_price)," \
                     "jd_id=values(jd_id),hot=values(hot)".format(table=table)
        try:
            # 执行sql语句
            cur.executemany(sql_insert, value)
            # 提交
            self.db.commit()
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            # 输出错误信息
            print(e)

    # 关注数据插入方法,该方法可以根据更换表名插入排行数据
    def insert_attention(self, cur, value, table):
        # 插入数据的sql语句
        sql_insert = "insert into  {table} (name,jd_price,jd_id,hot,middle_time,poor_time)" \
                             " values(%s,%s,%s,%s,%s,%s)".format(table=table)
        try:
            # 执行sql语句
            cur.executemany(sql_insert, value)
            # 提交
            self.db.commit()
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            # 输出错误信息
            print(e)

    # 查询排行数据表前10名商品名称,价格，热卖指数
    def query_top10_info(self, cur):
        query_sql = "select name,jd_price,hot from jd_ranking where id<=10"
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        return results  #返回所有数据

    # 根据id查询排行数据表数据内容
    def query_id_info(self, cur,id):
        query_sql = "select name,jd_price,jd_id,hot from jd_ranking where id={id}".format(id=id)
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchone()  # 获取查询的记录
        return results  # 返回所有数据

    # 查询关注商品的数据表中是否有相同的商品名称
    def query_is_name(self, cur, name):
        query_sql = "select count(*) from attention where name='{name}'".format(name=name)
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        return results[0][0]  # 返回所有数据

    # 查询排行的商品信息
    def query_rankings(self, cur, table):
        query_sql = "select id,name,jd_price,jd_id,hot from {table}".format(table=table)
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        row = len(results)  # 获取信息条数，作为表格的行
        column = len(results[0])  # 获取字段数量，作为表格的列
        return row, column, results  # 返回信息行与信息列（字段对应的信息）

    # 查询排行榜中所有的商品名称
    def query_rankings_name(self, cur, table):
        name_all_list =[]  # 保存所有商品名称的列表
        query_sql = "select name from {table}".format(table=table)
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        for r in results:
            name_all_list.append(r[0].replace(' ',''))
        return name_all_list      # 返回所有排行商品名称的列表

    # 查询已经关注的商品信息
    def query_evaluate_info(self, cur, table):
        query_sql = "select id,name,jd_price,jd_id,hot,middle_time,poor_time from {table}".format(table=table)
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        if len(results)!=0:
            row = len(results)  # 获取信息条数，作为表格的行
            column = len(results[0])  # 获取字段数量，作为表格的列
            return row, column, results  # 返回信息行与信息列（字段对应的信息）
        else:
            return 0,0,0




    # 更新关注商品信息
    def update_attention(self, cur, table, column, id):
        sql_update = "update {table} set {column} where id = {id}".format(table=table, column=column, id=id)
        try:
            cur.execute(sql_update)  # 执行sql语句
            # 提交
            self.db.commit()
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            # 输出错误信息
            print(e)

    # 删除关注商品的信息
    def delete_attention(self,cur,name):
        delete_sql = "delete from attention where name='{name}'".format(name=name)
        try:
            cur.execute(delete_sql)  # 执行sql语句
            # 提交
            self.db.commit()
        except Exception as e:
            # 错误回滚
            self.db.rollback()
            # 输出错误信息
            print(e)








