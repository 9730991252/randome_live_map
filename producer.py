import json
import time

from kafka import KafkaProducer

LAT_LON_KAFKA_TOPIC = "self_lat_lon"

producer = KafkaProducer(bootstrap_servers="localhost:9092")

start_latitude = 19.0760
starting_longitude = 72.8777
end_latitude = 18.5204
end_longitude = 73.8567

num_steps = 1000
step_size_lat = (end_latitude - start_latitude) / num_steps
step_size_lon = (end_longitude - starting_longitude) / num_steps
current_steps = 0

while True:
    latitude = start_latitude + step_size_lat * current_steps
    longitude = starting_longitude + step_size_lon * current_steps
    
    data = {
        "latitude": latitude,
        "longitude": longitude,
    }
    producer.send(
            LAT_LON_KAFKA_TOPIC,
            json.dumps(data).encode("utf-8")
        )
    
    
    current_steps += 1
    if current_steps > num_steps:
        current_steps = 0
        
    print(f"Done Sending.. {data}")
    time.sleep(1)