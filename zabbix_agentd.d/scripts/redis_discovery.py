#!/usr/bin/env python
import os
import json
t=os.popen("""sudo netstat -nltp|awk -F: '/redis-server/&&/LISTEN/{print $2}'|awk '{print $1}'| grep -v grep | grep -v '^$'   """)
ports = []
for port in  t.readlines():
        r = os.path.basename(port.strip())
        ports += [{'{#REDISPORT}':r}]
print json.dumps({'data':ports},sort_keys=True,indent=4,separators=(',',':'))
