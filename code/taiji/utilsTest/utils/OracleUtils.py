# -*- coding: utf-8 -*-

import cx_Oracle
import uuid
import random
import datetime
from ConfigUtils import Config

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Oracle():
    '''数据库连接'''
    __connect_info = ""
    __cof_file_name = "../config/config.txt"

    def __init__(self):
        self.__connect_info = Config().get_value("oracle_connect_info")

    def querySql(self, sql, param):
        conn = cx_Oracle.connect(self.__connect_info)
        cursor = conn.cursor()
        
        #执行查询 语句
        cursor.prepare(sql)
        x=cursor.execute(sql, param)
        dataList = []
        for row in x:
            dataList.append(row)
            
        print(dataList)
        cursor.close()
        conn.close()

    def insertManySql(self, sql, data_list):
        """
            data_list:
            [[],[],[]]
        """
        conn = cx_Oracle.connect(self.__connect_info)
        cursor = conn.cursor()
        cursor.prepare(sql)
        for data in data_list:
            cursor.executemany(None, tuple(data))
        conn.commit()
        cursor.close()
        conn.close()


def main():
    # o = Oracle()
    # try:
        # 查询测试
        # param = {}
        # sql = """ select * from DATA_TAG_INFO """
        # o.querySql(sql, param)

        # 插入测试
        # sql = "Insert into DATA_TAG_INFO (ID, TAG_CODE, TAG_PARENT_CODE, TAG_NAME, TAG_STATUS, TAG_TYPE, TAG_SENSITIVITY, TAG_LEVEL, CREATE_TIME, TAG_DES, CREATE_USER, IS_SYSTEM) Values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12)"
    # tag_info = {"tag_code":11001, "tag_num":11, "tag_name":u"地点", "tag_status":"0", "tag_types":"1", "tag_sen":"1", "tag_level":"2", "create_time":"", "create_user":"admin", "is_system":"1"}
    
    tag_num_name = [{"tag_num":10, "tag_name":u"人"}
            ,{"tag_num":11, "tag_name":u"地"}
            ,{"tag_num":12, "tag_name":u"物"}
            ,{"tag_num":13, "tag_name":u"组织"}
            ,{"tag_num":14, "tag_name":u"行为"}
            ,{"tag_num":20, "tag_name":u"人"}
            ,{"tag_num":21, "tag_name":u"地"}
            ,{"tag_num":22, "tag_name":u"物"}
            ,{"tag_num":23, "tag_name":u"组织"}
            ,{"tag_num":24, "tag_name":u"行为"}]
    sql = "Insert into DATA_TAG_INFO (ID, TAG_CODE, TAG_PARENT_CODE, TAG_NAME, TAG_STATUS, TAG_TYPE, TAG_SENSITIVITY, TAG_LEVEL, CREATE_TIME, TAG_DES, CREATE_USER, IS_SYSTEM) Values ({});\n"
    with open(r'../data/sql.txt', 'w', encoding="utf-8") as f:
            print(f.write("\n"))
    for num_name in tag_num_name:
        tag_info = {"tag_code":(num_name["tag_num"]*1000 + 1), "tag_num":num_name["tag_num"], "tag_name":num_name["tag_name"], "tag_status":"0", "tag_types":"1", "tag_sen":"1", "tag_level":"2", "create_time":"", "create_user":"admin", "is_system":"1"}
        print(tag_info)
        data_list = create_data(tag_info)
        # o.insertManySql(sql, data_list)
        # sql_datas = []
        for data in data_list:
            # sql_datas.append(sql.format(",".join(data)))
            with open(r'../data/sql.txt', 'a', encoding="utf-8") as f:
                print(f.write(sql.format(",".join(data))))
    # print(sql_datas)
    # except Exception as e:
    #     print(e)
    # input("回车退出！")


def create_data(tag_info):
    data_list = []
    tag_code = tag_info["tag_code"]
    tag_num = tag_info["tag_num"]
    tag_name = tag_info["tag_name"]
    tag_status = tag_info["tag_status"]
    tag_types = tag_info["tag_types"]
    tag_sen = tag_info["tag_sen"]
    tag_level = tag_info["tag_level"]
    create_time = tag_info["create_time"]
    create_user = tag_info["create_user"]
    is_system = tag_info["is_system"]
    for i in range(20):
        data_list_one = []
        tag_code += 1
        data_list_one.append("'" + str(uuid.uuid1()).replace("-", "") + "'")
        data_list_one.append("'" + str(tag_code) + "'")
        data_list_one.append("'" + str(tag_num) + "'")
        data_list_one.append("'" + str(tag_name + str(i+1)) + "'")
        data_list_one.append("'" + tag_status + "'")
        data_list_one.append("'" + tag_types + "'")
        data_list_one.append("'" + str(random.randint(1,10)) + "'")
        data_list_one.append("'" + tag_level + "'")
        data_list_one.append("TO_DATE('" + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + "', 'MM/DD/YYYY HH24:MI:SS')")
        data_list_one.append("'" + " " + "'")
        data_list_one.append("'" + create_user + "'")
        data_list_one.append("'" + is_system + "'")
        data_list.append(data_list_one)
    return data_list


if __name__ == '__main__':
    main()