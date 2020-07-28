[TOC]

# 声明

本脚本只是用于学习爬虫，并进行相关实践，请不要用于刷视频，由于刷视频导致的问题由使用者个人承担。

# 使用

> 本项目运行在python 3 above

## 依赖安装

```shell script
sh init/install_depend_on.sh
```

## 配置说明

需要修改 `constant/constant.py`文件中的`cookie`和`interval_time`.

- `cookie`： 为`https://www.bjjnts.cn`网站上的对应用户登陆后的cookie信息
- `interval_time`： 为设定脚本模拟的浏览间隔时间，默认为60秒。

## 运行

- 爬取第一页所有的课程
```shell script
python creeper/bjjnts_web.py 
```

- 运行模拟观看脚本
```shell script
python task/run_task.py
```