#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-08-23
# Author: Master Yumi
# Email : yumi@meishixing.com

from models.base import BaseModel

class TodoModel(BaseModel):
    """代办事项"""
    fields = ["id", "title", "remind", "priority", "deadline"]
    def __init__(self):
        self.id = 0
        # 主题
        self.title = ""
        # 是否提醒
        self.remind = 1
        # 优先级
        self.priority = 0
        # 截止日期
        self.deadline = "1991-11-11 11:11:11"
        # 创建时间
        self.create_time = "1991-11-11 11:11:11"

