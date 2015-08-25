#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-08-25
# Author: Master Yumi
# Email : yumi@meishixing.com

from config import cursor
from models.todo_model import TodoModel

class TodoCtrl(object):
    def get_todo_list(self):
        sql = "select * from todo;"
        n = cursor.execute(sql)
        if not n:
            return []
        data = cursor.fetchall()
        return TodoModel.load(data)

    def get_todo_detail(self, todo_id):
        sql = "select * from todo where id = %s;"
        n = cursor.execute(sql)
        if not n:
            return None
        data = cursor.fetchall()
        return TodoModel.load(data)[0]
