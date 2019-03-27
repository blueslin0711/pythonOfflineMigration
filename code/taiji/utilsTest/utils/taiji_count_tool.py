# -*- coding: utf-8 -*-
from ExcelUtils import Excel
from ConfigUtils import Config
import os

c = Config()
user_name_flag = c.get_value('user_name_flag')
host_start_flag = c.get_value('host_start_flag')
host_end_flag = c.get_value('host_end_flag')
pwd_flag = c.get_value('pwd_flag')
root_name = c.get_value('root_name')


def excel_text(file_name):
    excel = Excel()
    try:
        data_list = excel.read_excel("../input_excel/{}".format(file_name))
        host = file_name[:file_name.find('.xls')]
        # info_list = []
        # 域名 日期（日） 用户名 密码（拼接|） 上网账号 运营商 次数 最后时间
        excel_list = [["域名", "日期", "用户名", "上网账号", "密码", "次数"]]
        account_list = set()
        info_map = {}
        for i in data_list[0][1:]:
            title = i[4]
            if title.find(user_name_flag) > -1:
                user_name = title[(title.find(user_name_flag) + len(user_name_flag)):].split(' ')[0]
            else:
                user_name = ''
            # host_1 = title[(title.find(host_start_flag) + len(host_start_flag)):]
            # host = host_1[:host_1.find(host_end_flag)]
            if title.find(pwd_flag) > -1:
                pwd = title[(title.find(pwd_flag) + len(pwd_flag)):].split(' ')[0]
            else:
                pwd = ''
            account = i[6]
            time = i[5]
            date = time.split(' ')[0]
            # info = {'host': host, 'date': date, 'user_name': user_name, 'pwd': pwd, 'accout': account}
            info_key = '{}|{}|{}|{}'.format(host, date, user_name, account)
            if account is not None and len(account.strip()) > 0:
                account_list.add(account)
            if info_map.get(info_key) is None:
                info_map[info_key] = [1, pwd]
            else:
                if info_map[info_key][1].find(pwd) > -1:
                    info_map[info_key] = [info_map[info_key][0] + 1, info_map[info_key][1]]
                else:
                    info_map[info_key] = [info_map[info_key][0] + 1, '{}|{}'.format(info_map[info_key][1], pwd)]

        for key in info_map.keys():
            info_one_list = []
            for i in key.split(r'|'):
                info_one_list.append(i)
            info_one_list.append(info_map[key][1])
            info_one_list.append(info_map[key][0])
            excel_list.append(info_one_list)
            # print(info_one_list)
        # 导出excel
        excel.write_excel("../out_count_excel/{}_count.xls".format(host), excel_list, sheet_name="121")
        # 导出上网账号txt
        with open(r'../out_account_txt/{}.txt'.format(host), 'w', encoding="utf-8") as f:
            for rule in account_list:
                f.write('{}\n'.format(rule))
        # 测试修改excel
        # modify_data_list 格式：[(插入点行号,插入点列号, 数据数组->[[1,2,3],[2,3,4]]),()]
        # modify_data_list = [(11, 1, [["如何高效读懂一本书2", "22.3", "机械工业出版社", "中文"],["暗时间", "32.4", "人民邮电出版社", "中文"]])
        #         ,(16, 1, [["如何高效读懂一本书3", "22.3", "机械工业出版社", "中文1"]])]
        # excel.modify_excel("../data/111.xls", modify_data_list, sheet_index=1)

    except Exception as e:
        print(e)


def main():
    print('开始')
    for file_name in os.listdir('..\{}'.format(root_name)):
        excel_text(file_name)
    print('结束')


if __name__ == '__main__':
    main()

