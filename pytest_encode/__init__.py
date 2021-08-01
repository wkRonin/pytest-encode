# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 22:25
# @Author  : wkRonin
# @File    :__init__.py.py
import logging
from typing import List

logger = logging.getLogger(__name__)  # 定义对应的程序模块名name，默认是root
# 指定最低的日志级别 critical > error > warning > info > debug
logger.setLevel(logging.DEBUG)
# 日志输出到屏幕控制台
consol_haddler = logging.StreamHandler()
# 设置日志等级
consol_haddler.setLevel(logging.INFO)

#  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题
if not logger.handlers:
    # 向文件report.log输出日志信息，encoding="utf-8",防止输出log文件中文乱码
    file_haddler = logging.FileHandler("report.log", encoding="utf-8")
    file_haddler.setLevel(logging.INFO)  # 设置输出到文件最低日志级别

    formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
    # 选择一个输出格式
    consol_haddler.setFormatter(formatter)
    file_haddler.setFormatter(formatter)
    # 增加指定的handler
    logger.addHandler(file_haddler)
    logger.addHandler(consol_haddler)


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    """
    测试用例收集完成时，将收集到的item的name（用例的名字）和nodeid(用例的路径)的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")