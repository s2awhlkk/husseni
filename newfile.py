import websocket
from uuid import uuid4
import json
import gzip
import websocket
import ssl
import os
import json
import gzip
import requests
from time import sleep
import random
import concurrent.futures
import Config
#eoeowkwnsj
#jwowbeohs
from datetime import timedelta
import datetime 

Error,Exists,Done=0,0,0
def CreateSafeUM():
	token=''
	ID=''
	global Error,Exists,Done	
	user=open('name.text','r').readline()
	headers = {
		    "app": "com.safeum.android",
		    "host": None,
		    "remoteIp": "51.79.208.190",
		    "remotePort": str(8080),
		    "sessionId": str(uuid4()),
		    "time": "2023-09-5 12:13:32",
		    "url": "wss://51.79.208.190/Auth"
		}
	data=Config.data(user)			
	url = "wss://51.79.208.190/Auth"
	web=websocket.create_connection(url, header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})
	web.send(json.dumps(data))
	result = web.recv()
	response = gzip.decompress(result)
	#print(response)
	web.close()
	if '"comment":"Retry"' in str(response):
		Error+=1
		print(Error,user,' | ',str(response).split('comment":"')[1].split('",')[0])
	if '"comment":"Exists"' in str(response):
		
		Exists+=1
		print(Exists,user,' | ',str(response).split('comment":"')[1].split('",')[0])
		
		Us=''.join(random.choice('pqoeiytteolakshgsfksosoejsjsisis019352pqowhxus8282')for i in range(15))
		open("name.text","+w").write(str(Us))
		
		
	if '"status":"Success"' in str(response):

		Done+=1
		print(user,Done,' | ',str(response).split('status":"')[1].split('",')[0])
	
		Send_Tele=(f''' {user}''') 

		requests.post("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Send_Tele))
		
		Us=''.join(random.choice('pqoeiytteolak64313118sfksosoejsjsisis019352pqowhxus8282')for i in range(15))
		open("name.text","+w").write(str(Us))		

	if '"comment":"Symbols"' in str(response):
		print('\n\n')
		Us=''.join(random.choice('pqoeiytteolakshgsfksosoejsjsisis019352pqowhxus8282')for i in range(15))
		open("name.text","+w").write(str(Us))

	if Error == 15:
		Error=0
		Us=''.join(random.choice('pqoeiytteolakshgsfksosoejsjsisis019352pqowhxus8282')for i in range(15))
		open("name.text","+w").write(str(Us))		
while True:	
		CreateSafeUM()	
	
					