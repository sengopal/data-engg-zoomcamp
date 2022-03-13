import csv
from json import dumps
from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         key_serializer=lambda x: dumps(x).encode('utf-8'),
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

file01 = open('data/rides01.csv')
file02 = open('data/rides02.csv')

csvreader01 = csv.reader(file01)
csvreader02 = csv.reader(file02)

next(csvreader01)
next(csvreader02)
for row01, row02 in zip(csvreader01, csvreader02):
    key = {"vendorId": int(row01[0])}
    value = {"vendorId": int(row01[0]), "passenger_count": int(row01[3]), "trip_distance": float(row01[4]), "payment_type": int(row01[9]), "total_amount": float(row01[16])}
    producer.send('datatalkclub.yellow_taxi_ride.01.json', value=value, key=key)

    key = {"vendorId": int(row02[0])}
    value = {"vendorId": int(row02[0]), "passenger_count": int(row02[3]), "trip_distance": float(row02[4]), "payment_type": int(row02[9]), "total_amount": float(row02[16])}
    producer.send('datatalkclub.yellow_taxi_ride.02.json', value=value, key=key)

    print("producing")
    sleep(1)
