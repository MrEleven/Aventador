#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Date  : 2015-08-25
# Author: Master Yumi
# Email : yumi@meishixing.com

import sys, os, MySQLdb
from importlib import import_module

configfile = sys.argv[-1]
dirname, basename = os.path.split(configfile)
module_name = basename.split(".")[0]
sys.path.append(dirname)
cm = import_module(module_name)

mysql_conf = cm.mysql_conf
conn = MySQLdb.connect(**mysql_conf)
conn.autocommit(1)
cursor = conn.cursor()


