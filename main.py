from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import time
import random
import os

token = os.getenv("INFLUXDB_TOKEN")   # نقرأ التوكن من متغير بيئة بدل ما نكتبه في الكود مباشرة
org = "iot-org"
bucket = "sensors"
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)
query_api = client.query_api()


def send_readings(count=5, interval=2):
    for i in range(count):
        point = Point("sensor_readings") \
            .tag("device_id", "1") \
            .field("temperature", round(random.uniform(20, 35), 1)) \
            .field("humidity", round(random.uniform(30, 70), 1))
        write_api.write(bucket=bucket, record=point)
        print(f"Reading {i + 1} sent")
        time.sleep(interval)


def query_recent_readings():
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -1h)
      |> filter(fn: (r) => r._measurement == "sensor_readings")
    '''
    result = query_api.query(query)
    for table in result:
        for record in table.records:
            print(f"{record.get_time()} - {record.get_field()}: {record.get_value()}")


if __name__ == "__main__":
    send_readings()
    print("\n--- Recent Readings ---")
    query_recent_readings()