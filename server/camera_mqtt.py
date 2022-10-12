import paho.mqtt.client as mqtt
from PIL import Image
import numpy as np
import io

def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))
    client.subscribe("camera/CCL")
def on_publish(client, userdata, mid):
    print("message publish..")

def on_message(client, userdata, msg):

    data = msg.payload
    print(len(data))
    print(type(data))
    io.BytesIO(data)

    image = Image.open(io.BytesIO(data))

    image.save('../smart_iot_home/static/ALERT.png')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.0.168",1883, 60)
client.loop_forever()