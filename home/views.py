from django.shortcuts import render
from django.http import JsonResponse
from kafka import KafkaConsumer, KafkaProducer
import json

def index(request):
    return render(request, 'index.html')

def delivery_boy(request):
    return render(request, 'delivery_boy.html')

def produce_lat_lon(request):
    if request.method == 'GET':
        lat = request.GET['lat']
        lon = request.GET['lon']
        
        LAT_LON_KAFKA_TOPIC = "self_lat_lon"
        
        producer = KafkaProducer(bootstrap_servers="103.150.136.82:9092")
        
        data = {
            "latitude": lat,
            "longitude": lon,
        }
        producer.send(
                LAT_LON_KAFKA_TOPIC,
                json.dumps(data).encode("utf-8")
            )
    return JsonResponse({'latitude': 'status'})


def data(request):
    c = get_latitude_longitude()
    da = c[0]
    return JsonResponse({
        'latitude':da['latitude'],
        'longitude':da['longitude']
    })
    

def get_latitude_longitude():
    
    LAT_LON_KAFKA_TOPIC = "self_lat_lon"
    consumer = KafkaConsumer(
        LAT_LON_KAFKA_TOPIC, 
        bootstrap_servers="103.150.136.82:9092"
    )
    consumed_message = []
    for m in consumer:
        c = json.loads(m.value.decode())
        consumed_message.append(c)
        break
    return consumed_message

