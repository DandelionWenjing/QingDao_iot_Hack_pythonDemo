import random
import time
import thread
import sys
import uuid
import iothub_client
from datetime import datetime, timedelta
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

# String containing Hostname, Device Id & Device Key in the format
CONNECTION_STRING = "HostName=iotzwj.azure-devices.net;DeviceId=visitorDevice1;SharedAccessKey=RaRWfP3WGAj1kzG7OqVmoGiI2WFXLtmzWRIudoPb1QY="
# choose HTTP, AMQP or MQTT as transport protocol
PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 10000
SEND_CALLBACKS = 0
GPS_DATA = "{\"rideId\":\"%s\",\"trainId\":\"%s\",\"correlationId\":\"%s\",\"lat\":%.4f,\"long\":%.4f,\"alt\":%.3f,\"speed\":%.2f,\"vertAccuracy\":%d,\"horizAccuracy\":%d,\"deviceTime\":\"%s\"}"
ACCE_DATA="{\"rideId\":\"%s\",\"trainId\":\"%s\",\"correlationId\":\"%s\",\"accelX\":%.6f,\"accelY\":%.6f,\"accelZ\":%.6f,\"deviceTime\":\"%s\"}"
EVENTS_DATA="{\"rideId\":\"%s\",\"trainId\":\"%s\",\"correlationId\":\"%s\",\"passengerCount\":%d,\"eventType\":\"%s\",\"deviceTime\":\"%s\"}"

def send_confirmation_callback(message, result, user_context):
    global SEND_CALLBACKS
    print ( "Confirmation[%d] received for message with result = %s" % (user_context, result) )
    map_properties = message.properties()
    print ( "    message_id: %s" % message.message_id )
    print ( "    correlation_id: %s" % message.correlation_id )
    key_value_pair = map_properties.get_internals()
    print ( "    Properties: %s" % key_value_pair )
    SEND_CALLBACKS += 1
    print ( "    Total calls confirmed: %d" % SEND_CALLBACKS )

def iothub_client_init():
    # prepare iothub client
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    # set the time until a message times out
    client.set_option("messageTimeout", MESSAGE_TIMEOUT)
    client.set_option("logtrace", 0)
    client.set_option("product_info", "HappyPath_Simulated-Python")
    return client

def client_run(TRAINID, delay):
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        message_counter = 0           
        currenttime = datetime.now()

        while True:
            print ( "Train %s start ride") % TRAINID
            
            msg_GPS = GPS_DATA % (str(uuid.uuid4()), TRAINID, str(uuid.uuid4()), round(random.uniform(0, 100), 4), round(random.uniform(-100, 100), 4),
            round(random.uniform(0, 300), 2), round(random.uniform(0, 10), 2), random.randint(0,10), random.randint(0,50), str(currenttime) )
            msg_ACCE = ACCE_DATA % (str(uuid.uuid4()), TRAINID, str(uuid.uuid4()), round(random.uniform(0, 1)), round(random.uniform(0, 3)), round(random.uniform(0, 2)), str(currenttime) )
            msg_EVENT1 = EVENTS_DATA % (str(uuid.uuid4()), TRAINID, str(uuid.uuid4()), random.randint(0,50), "RideStart", str(currenttime) )
            msg_EVENT2 = EVENTS_DATA % (str(uuid.uuid4()), TRAINID, str(uuid.uuid4()), random.randint(0,50), "RideEnd", str(currenttime+timedelta(minutes=1)) )
            msg_EVENT3 = EVENTS_DATA % (str(uuid.uuid4()), TRAINID, str(uuid.uuid4()), random.randint(0,50), "PhotoTriggered", str(currenttime+timedelta(seconds=30)) )

            currenttime = currenttime + timedelta(minutes=1)
            currenttime = currenttime + timedelta(seconds=20)

            message_GPS = IoTHubMessage(msg_GPS)
            message_ACCE = IoTHubMessage(msg_ACCE)
            message_EVENT1 = IoTHubMessage(msg_EVENT1)
            message_EVENT2 = IoTHubMessage(msg_EVENT2)
            message_EVENT3 = IoTHubMessage(msg_EVENT3)

            client.send_event_async(message_GPS, send_confirmation_callback, message_counter)
            print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            time.sleep(delay)
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            message_counter += 1

            client.send_event_async(message_ACCE, send_confirmation_callback, message_counter)
            print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            time.sleep(delay)
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            message_counter += 1

            client.send_event_async(message_EVENT1, send_confirmation_callback, message_counter)
            print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            time.sleep(delay)
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            message_counter += 1

            client.send_event_async(message_EVENT2, send_confirmation_callback, message_counter)
            print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            time.sleep(delay)
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            message_counter += 1

            client.send_event_async(message_EVENT3, send_confirmation_callback, message_counter)
            print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            time.sleep(delay)
            status = client.get_send_status()
            print ( "Send status: %s" % status )
            message_counter += 1

    except IoTHubError as iothub_error:
        print ( "Unexpected error %s from IoTHub" % iothub_error )
        return
    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )


def iothub_client_telemetry_sample_run():
    # TRAINID = ["", "", "", "", ""]
    # for i in range(1, 5) :
    #     TRAINID[i] = str(uuid.uuid4())
    #     client_run(TRAINID[i], 30)
    client_run(str(uuid.uuid4()), 30)
        
    
if __name__ == '__main__':
    print ( "Simulating a device using the Azure IoT Hub Device SDK for Python" )
    print ( "    Protocol %s" % PROTOCOL )
    print ( "    Connection string=%s" % CONNECTION_STRING )

    iothub_client_telemetry_sample_run()