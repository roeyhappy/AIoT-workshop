# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import datetime
import time

def IoT_core_init(url,port,root_cert,private_key,device_cert):
    # For certificate based connection
    myMQTTClient = AWSIoTMQTTClient("myClientID")
    
    myMQTTClient.configureEndpoint(url, port)
    # For Websocket
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    # For TLS mutual authentication with TLS ALPN extension
    # myMQTTClient.configureEndpoint("YOUR.ENDPOINT", 443)
    myMQTTClient.configureCredentials(root_cert, private_key, device_cert)
    # For Websocket, we only need to configure the root CA
    # myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
    myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    return myMQTTClient
    
    
def transmit_message_to_cloud(mytopicheader, image_name, groupid, group_member_count, member_names,blessing, client):
    now_time = datetime.datetime.now()
    group = groupid + '/'
    year = now_time.strftime("%Y") + '/'
    month = now_time.strftime("%m") + '/'
    date = now_time.strftime("%d") + '/'
    s3_pic_url =  group + year + month + date
    picurl = s3_pic_url + image_name
    
    now_time = datetime.datetime.utcnow()
    publish_time = now_time.strftime("%Y-%m-%dT%H:%M:%S")
    ct = time.time()
    date_ms = (ct - int(ct))*1000
    publish_time_2 = "%s.%03d" %(publish_time, date_ms)
    
    mypayload = {
        "groupId": groupid,
        "memberCount": group_member_count,
        "memberNames": member_names,
        "eventId": "1",
        "pictureId": picurl,
        "publishTime": publish_time_2,
        "blessings":blessing
        }
       
    
    topicbody = json.dumps(mypayload)
    client.connect()
    client.publish(mytopicheader, topicbody, 0)
    #client.disconnect()