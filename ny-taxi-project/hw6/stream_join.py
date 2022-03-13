import faust

from taxi_rides import TaxiRide
from faust import current_event

app = faust.App('datatalksclub.stream.v4', broker='kafka://localhost:9092', consumer_auto_offset_reset="earliest")

# https://github.com/robinhood/faust/issues/644
topic = app.topic('datatalkclub.yellow_taxi_ride.01.json', "datatalkclub.yellow_taxi_ride.02.json", value_type=TaxiRide)

vendor_rides = app.Table('vendor_rides', default=int)

@app.agent(topic)
async def process(stream):
    async for event in stream.events():  # async for event in stream:
        print(event.message.topic)  # either "topic1" or "topic2" here
        print(event.value)  # an instance of myrecord

        # Both the stream data are joined to compute the vendor information
        vendor_rides[event.vendorId] += 1


if __name__ == '__main__':
    app.main()
