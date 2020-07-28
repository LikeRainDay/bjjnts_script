import json
import requests
from constant.constant import *
from lxml import etree


def get_content_from_url(url):
    # 爬取的网页链接
    r = requests.get(url, headers={'Cookie': cookie, 'User_Agent': User_Agent,
                                   "Host": "www.bjjnts.cn",
                                   "Sec-Fetch-Dest": "document",
                                   "Sec-Fetch-Mode": "navigate",
                                   "Sec-Fetch-Site": "origin",
                                   "Sec-Fetch-User": "?1",
                                   "Upgrade-Insecure-Requests": "1"
                                   })
    r.encoding = None
    return etree.HTML(r.text)


def download_cursors():
    html = get_content_from_url(str(prefix) + "/userCourse")
    block = html.xpath("//ul[@class='user_courselist']//div")
    for item in block:
        json_dic = []
        # print(etree.tostring(item))
        dataId = item.xpath('..//a[1][contains(@href,"javascript:;")]//@data-id')
        dataCId = item.xpath('..//a[1][contains(@href,"javascript:;")]//@data-cid')
        title = item.xpath("h2[1][@class='user_coursetit']//text()")
        if len(title) != 0:
            dataId = dataId[0]
            dataCId = dataCId[0]
            # print("title is {} ==== dataId is {} ==== dataCId is {}".format(title, dataId, dataCId))
            address = "{}/lessonStudy/{}/{}".format(prefix, dataId, dataCId)
            html = get_content_from_url(address)
            block = html.xpath("//ul[@class='new_demoul']//div")
            for item in block:
                data_lessonid = item.xpath('..//a[1][contains(@href,"javascript:;")]//@data-lessonid')
                menutitle = item.xpath("..//h4[1][@class='course_study_menutitle']//text()")
                menudate = item.xpath("..//p[1][@class='course_study_menudate']//text()")
                if len(data_lessonid) != 0:
                    # 字符串正则提取
                    menutitle = menutitle[0]
                    menudate = menudate[0]
                    nums = menudate.replace("(", "").replace(")", "").split(":")
                    hour = int(nums[0]) * 60 * 60
                    min = int(nums[1]) * 60
                    sec = int(nums[2])
                    total = hour + min + sec
                    json_dic.append({
                        "dataId": dataId,
                        "dataCId": dataCId,
                        "title": title[0],
                        "data_lesson_id": data_lessonid[0],
                        "menutitle": menutitle,
                        "menudate": menudate,
                        "total": total,
                    })
            # 写入json至
            with open("../curriculum_table/" + str(title[0]) + ".json", "w") as fp:
                fp.write(json.dumps(json_dic))
                fp.close()


"""
将课程列表放置在 curiculum_table目录下
"""
if __name__ == '__main__':
    download_cursors()
