# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

def mycallback():
    print("it seems OK!!!!")



# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("myClientID")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
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

mytopicheader = "pg/d-1a2d3a2ea4f84eb6b8197a3a3e4a6ad8:2eaa3bcbce2d49f0adf7b3edc3cc4638:sn001/data"

mypayload = {
	"groupId": "group001",
	"memberCount": "3",
	"memberNames": ["m1","m2","m3"],
	"eventId": "1",
	"pictureId": "pic1",
	"publishTime": "2019-12-24T20:40:43.181"
}

#topicbody = json.dumps(mypayload)

# myMQTTClient.connect()
# myMQTTClient.publish("myTopic", mytopicheader + topicbody, 0)
# myMQTTClient.subscribe("myTopic", 1, mycallback)
# myMQTTClient.unsubscribe("myTopic")
# myMQTTClient.disconnect()

topicbody = json.dumps(mypayload)
myMQTTClient.connect()
myMQTTClient.publish(mytopicheader, topicbody, 0)
# myMQTTClient.subscribe(mytopicheader, 1, mycallback)
# myMQTTClient.unsubscribe(mytopicheader)
myMQTTClient.disconnect()

