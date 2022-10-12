from django.shortcuts import render, redirect
# Create your views here.
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

normal_temp = 25.0
MQTT_Broker = "192.168.0.168"
topic = "dht/CCL"

class MyMqtt():
    def __init__(self):
        self.value = 0

my_data = MyMqtt()

def on_connect( client, userdata, flags, rc):
    print("Connect with result code" + str(rc))
    client.subscribe(topic) # Topic

def on_message( client, userdata, msg ):
    x = str(msg.payload.decode('utf-8'))
    my_data.value = eval(x)


import os
def getTemp(request):
    try:
        print(request.session['user_id'])
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT_Broker, 1883, 60)
        client.loop_start()

        print("hello")
        data = my_data.value
        print(data)
        try:
            print(data['temperature'])
            context = {'temperature': data['temperature'], 'humidity':data['humidity']}

        except Exception as e:
            print("error")
            context = {}
        print(context)
        return render(request, 'temp.html/',context)
    except Exception as e:
        return redirect('../../')

def getLight(request):
    try:
        print(request.session['user_id'])
        if (request.method == "POST"):
            print(type(request.POST.get('light',None)))
            light = int(request.POST.get('light',None))
            print(light)
            if(light==1):
                light = 0
            elif(light==0):
                light = 1
            client = mqtt.Client()
            client.connect(MQTT_Broker,1883,60)
            data = {'led_state':light}
            client.loop_start()
            client.publish(topic="dht/RECEIVE",payload=str(data))

            return render(request, 'light.html/', data)
        else:
            client = mqtt.Client()
            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(MQTT_Broker, 1883, 60)
            client.loop_start()

            print("hello")
            data = my_data.value
            print(data)
            try:
                print(data['led'])
                context = {'led_state': data['led']}

            except Exception as e:
                print("error")
                context = {}
            print(context)
            return render(request, 'light.html/', context)
    except Exception as e:
        return redirect('../../')

def getALert(request):
    try:
        print(request.session['user_id'])
        return render(request, 'alert.html/')

    except Exception as e:
        return redirect('../../')
