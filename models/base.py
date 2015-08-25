#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-08-23
# Author: Master Yumi
# Email : yumi@meishixing.com

from datetime import datetime

class BaseModel(object):
    fields = []

    @classmethod
    def load(cls, data_list):
        model_list = []
        for data in data_list:
            model_obj = cls()
            for i in xrange(0, len(cls.fields)):
                setattr(model_obj, cls.fields[i], data[i])
            model_list.append(model_obj)
        return model_list

    @classmethod
    def dump(cls, model):
        if isinstance(model, (list, tuple)):
            return [cls.dump(m) for m in model]
        model_dict = {}
        for field in cls.fields:
            model_dict[field] = getattr(model, field)
            if isinstance(model_dict[field], datetime):
                model_dict[field] = model_dict[field].strftime("%Y-%m-%d %H:%M:%S")
        return model_dict
        
