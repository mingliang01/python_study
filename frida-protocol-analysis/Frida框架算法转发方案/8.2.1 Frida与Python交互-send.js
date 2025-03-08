import frida,sys

	def Fun(message,data):
    	if message['type']=='send':
        	print("send:{}".format(message['payload']))
   		else:
        	print(message)

	device=frida.get_remote_device().attach(12260)
	script=device.create_script(jsCode)
	script.on('message',Fun)
	script.load()#脚本加载
	sys.stdin.read()#CMD不会退出，便于控制台观察