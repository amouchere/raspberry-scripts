#!/usr/bin/env python
# Python 3, prerequis : pip install pySerial influxdb



import serial
import logging
import time
import requests
from subprocess import check_output
from datetime import datetime
from influxdb import InfluxDBClient

# création du logguer
logging.basicConfig(filename='/home/pi/data/db-size-monitoring/db-size-monitoring.log', level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger()


# connexion a la base de données InfluxDB
client = InfluxDBClient('192.168.1.17', 8086)
db = "homedata"
connected = False
while not connected:
    try:
        # print ("Database %s exists?", db)
        if not {'name': db} in client.get_list_database():
            # print ("Database %s creation..", db)
            client.create_database(db)
            # print ("Database %s created!", db)
        client.switch_database(db)
        # print ("Connected to ", db)
    except requests.exceptions.ConnectionError:
        # print ('InfluxDB is not reachable. Waiting 5 seconds to retry.')
        time.sleep(5)
    else:
        connected = True


def add_measures(datasize):
    points = []
    point = {
                "measurement": "datasize",
                "tags": {
                    "host": "raspberry",
                    "region": "linky"
                },
                "time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "fields": {
                    "value": datasize
                }
            }
    
    logging.info("Data -> %s", point)
    # print ("Database point ", point)
    points.append(point)

    client.write_points(points)


datasize=check_output("sudo du -sh /home/pi | cut -d'M' -f1  | xargs", shell=True)

# insertion dans influxdb
add_measures(int(datasize.strip()))

# result = client.query('select value from datasize;')

# print("Result: {0}".format(result))
