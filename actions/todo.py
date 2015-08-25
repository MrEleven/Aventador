#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-08-23
# Author: Master Yumi
# Email : yumi@meishixing.com

from modules.AvenUOM import AvenHandler
from modules.todo_ctrl import TodoCtrl
from models.todo_model import TodoModel
import json

class todo(AvenHandler):
    def __init__(self):
        self.todo_ctrl = TodoCtrl()
        
    def list(self, todo_id):
        """获取所有代办事项"""
        todo_list = self.todo_ctrl.get_todo_list()
        self.tornado.write(json.dumps(TodoModel.dump(todo_list)))

    def add(self):
        """增加待办事项"""
        self.write("add")
