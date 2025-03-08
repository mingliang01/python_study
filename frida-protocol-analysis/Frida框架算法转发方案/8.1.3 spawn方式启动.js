import frida,sys

	device=frida.get_usb_device()
	pid=device.spawn(["com.dodonew.online"])
	process=device.attach(pid)

	script=process.create_script(jsCode)
	script.load()#脚本加载
	device.resume(pid)#加载完脚本，恢复进程运行
	sys.stdin.read()#CMD不会退出，便于控制台观察