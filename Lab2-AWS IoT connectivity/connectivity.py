# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

def IoT_core_init():
    # For certificate based connection
    myMQTTClient = AWSIoTMQTTClient("myClientID")
    
    myMQTTClient.configureEndpoint("a3afq7zrw2mcf4.ats.iot.cn-north-1.amazonaws.com.cn", 8883)
    # For Websocket
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    # For TLS mutual authentication with TLS ALPN extension
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myMQTTClient.configureCredentials(r'root-CA.crt', r'private.pem.key', r'device.pem.crt')
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    return myMQTTClient
    
    
def transmit_message_to_cloud(mytopicheader, mypayload, client):
    topicbody = json.dumps(mypayload)
    myMQTTClient.connect()
    myMQTTClient.publish(mytopicheader, topicbody, 0)
    myMQTTClient.disconnect()