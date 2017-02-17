#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
from datetime import datetime

conn = MongoClient("127.0.0.1",27017) 
db = conn["Shadowsocks-Manager"]
db.authenticate("shadowsocks","shadowsocks123")

historyhours = db.historyhours
historyoriginals = db.historyoriginals
mails = db.mails
oneseconds = db.oneseconds
options = db.options
sessions = db.sessions
users = db.users

time = {"time":{"$lt":datetime(datetime.now().year, datetime.now().month, 1)}}
sendTime = {"sendTime":{"$lt":datetime(datetime.now().year, datetime.now().month, 1)}}

print historyhours.remove(time)
print historyoriginals.remove(time)
print mails.remove(sendTime)
print oneseconds.remove(time)
#print historyhours.find({"time":{"$gte":datetime(datetime.now().year, datetime.now().month, 1)}}).count()

