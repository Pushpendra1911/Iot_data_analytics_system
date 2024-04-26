import paho.mqtt.client as mqtt
import json
from message_processor import process_message

# MQTT broker configuration
broker_address = "localhost"
broker_port = 1883
topic = "iot_data"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Received message: " + str(payload))
    process_message(payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_forever()
