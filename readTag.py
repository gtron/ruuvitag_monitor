#!/usr/bin/python3
import json
import sys
import errno
import datetime
from time import sleep
from ruuvitag_sensor.ruuvi import RuuviTagSensor

mac = sys.argv[1] 
macs = [ mac ]
sleepTime = 2.5

datas = RuuviTagSensor.get_data_for_sensors(macs, sleepTime)

#print(str(datas))

# convert json to string
dump = json.dumps(datas)
data = json.loads(dump)

#
print(str(data[mac]))
