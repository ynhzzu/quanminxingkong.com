#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import random

file = "/etc/shadowsocks_test.json"
pwd_file = "/usr/share/nginx/html/pwd.html"
pwd = "against" + str(int(random.random() * 1000))
data = {
          "server" : "0.0.0.0",
          "port_password" : {
              "1082" : pwd
           },
           "timeout" : 300,
           "method" : "rc4-md5",
           "fast_open" : True
      }
dt = json.dumps(data)
print dt

with open(file, "w") as  f:
     f.write(dt)

with open(pwd_file, "w") as f:
     f.write(pwd)

