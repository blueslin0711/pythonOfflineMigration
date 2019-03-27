# -*- coding: utf-8 -*-

import cx_Oracle
import uuid
import random
import datetime
from ConfigUtils import Config

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def main():

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
    with open(r'../data/tagSql.txt', 'w', encoding="utf-8") as f:
            f.write("\n")
    with open(r'../data/ruleSql.txt', 'w', encoding="utf-8") as f:
            f.write("\n")
    for num_name in tag_num_name:
        tag_info = {"tag_code":(num_name["tag_num"]*1000 + 1), "tag_num":num_name["tag_num"], "tag_name":num_name["tag_name"], "tag_status":"0", "tag_types":"1", "tag_sen":"1", "tag_level":"2", "create_time":"", "create_user":"admin", "is_system":"1"}
        data_list, rule_list = create_data(tag_info)
        with open(r'../data/tagSql.txt', 'a', encoding="utf-8") as f:
            for data in data_list:
                f.write(sql.format(",".join(data)))
        with open(r'../data/ruleSql.txt', 'a', encoding="utf-8") as f:
            for rule in rule_list:
                f.write(rule)



def create_data(tag_info):
    data_list = []
    rule_list = []
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
        tag_uuid = str(uuid.uuid1()).replace("-", "")
        data_list_one.append("'" + tag_uuid + "'")
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
        create_rule_list(tag_uuid, tag_code, tag_name, rule_list)
        data_list.append(data_list_one)
    return data_list, rule_list

def create_rule_list(tag_uuid, tag_code, tag_name, rule_list):
    rule_id = tag_code*100000000;
    rule_name = tag_name + "规则"
    for i in range(random.randint(2,6)):
        rule_uuid = str(uuid.uuid1()).replace("-", "")
        rule_id += 1
        rule_list.append("Insert into TAG_PLATFORM.DATA_TAG_RULE (ID, TAG_CODE, RULE_ID, RULE_NAME) Values ('{}', '{}', '{}', '{}');\n".format(rule_uuid, tag_uuid, str(rule_id), (rule_name+str(i+1))))


if __name__ == '__main__':
    main()