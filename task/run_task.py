import json
import requests
from constant.constant import *
import os
import time

path = "../curriculum_table"


def get_request(url):
    r = requests.get(url, headers={'Cookie': cookie, 'User_Agent': User_Agent,
                                   "Host": "www.bjjnts.cn",
                                   "Referer": "https://www.bjjnts.cn/userCourse",
                                   "Sec-Fetch-Dest": "empty",
                                   "Sec-Fetch-Mode": "cors",
                                   "Sec-Fetch-Site": "same-origin",
                                   "Upgrade-Insecure-Requests": "1",
                                   "X-Requested-With": "XMLHttpRequest"
                                   })
    print(json.loads(r.text))


def post_request(url):
    r = requests.post(url, headers={'Cookie': cookie, 'User_Agent': User_Agent,
                                    "Host": "www.bjjnts.cn",
                                    "Referer": "https://www.bjjnts.cn/userCourse",
                                    "Sec-Fetch-Dest": "empty",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Upgrade-Insecure-Requests": "1",
                                    "X-Requested-With": "XMLHttpRequest"
                                    })
    result = json.loads(r.text)
    print(result)
    return result


def post_request_with_param(url, param):
    r = requests.post(url, headers={'Cookie': cookie, 'User_Agent': User_Agent,
                                    "Host": "www.bjjnts.cn",
                                    "Referer": "https://www.bjjnts.cn/userCourse",
                                    "Sec-Fetch-Dest": "empty",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Upgrade-Insecure-Requests": "1",
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "X-Requested-With": "XMLHttpRequest"
                                    }, data=param)
    result = json.loads(r.text)
    print(result)
    return result


def course_simulation(item):
    result = post_request(str(prefix) + "/lessonStudy/" + str(item["dataId"]) + "/" + str(item["data_lesson_id"]))
    if result["code"] != 200:
        return
    cur_time = 0
    total = item["total"]
    while cur_time < total:
        time.sleep(interval_time)
        cur_time += 60
        if cur_time > total:
            cur_time = total
        print(cur_time)
        post_request_with_param(
            str(prefix) + "/addstudentTaskVer2/" + str(item["dataId"]) + "/" + str(item["data_lesson_id"]),
            'learnTime=' + str(cur_time) + '&push_event=ended')


if __name__ == '__main__':
    # 读取目录下的文件
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            print("======= start simulation [ {} ] ===========".format(file))
            f = open(path + "/" + file)
            json_data = json.load(f)
            get_request(str(prefix) + "/idCardVerified")
            for item in json_data:
                course_simulation(item)
            print("======= end simulation [ {} ] ===========".format(file))
