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
logging.basicConfig(filename='/home/pi/data/log/db-size-monitoring.log', level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger()


# connexion a la base de données InfluxDB
client = InfluxDBClient('localhost', 8086)
db = "homedata"
connected = False
while not connected:
    try:
        logging.info("Database %s exists?", db)
        if not {'name': db} in client.get_list_database():
            logging.info("Database %s creation..", db)
            client.create_database(db)
            logging.info("Database %s created!", db)
        client.switch_database(db)
        logging.info("Connected to %s", db)
    except requests.exceptions.ConnectionError:
        logging.info('InfluxDB is not reachable. Waiting 5 seconds to retry.')
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
    
    logging.info("Database point ", point)
    points.append(point)

    client.write_points(points)


datasize=check_output("sudo du -sh /home/pi | cut -d'M' -f1  | xargs", shell=True)

# insertion dans influxdb
add_measures(int(datasize.strip()))

# result = client.query('select value from datasize;')

# logging.info("Result: {0}".format(result))
