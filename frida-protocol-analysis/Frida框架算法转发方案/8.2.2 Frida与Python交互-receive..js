def Fun(message,data):
    	if message['type']=='send':
        	print("send:{}".format(message['payload']))
        	script.post({'data':"data from Python!"})
    	else:
        	print(message)


recv(function(obj){
   		console.log(obj.data);
	}).wait();