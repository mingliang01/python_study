function hookTest(username, passward){
var result;
Java.perform(function(){
var time = new Date().getTime();

var signData = 'equtype=ANDROID&loginImei=Android352689082129358&timeStamp=' + 
time + '&userPwd=' + passward + '&username=' + username + '&key=sdlkjsdljf0j2fsjk';

var Utils = Java.use('com.dodonew.online.util.Utils');
var sign = Utils.md5(signData).toUpperCase();
console.log('sign: ', sign);
    
var encryptData = '{"equtype":"ANDROID","loginImei":"Android352689082129358",
"sign":"'+sign +'","timeStamp":"'+ time +'","userPwd":"' + passward + '","username":"' 
+ username + '"}';

var RequestUtil = Java.use('com.dodonew.online.http.RequestUtil');
var Encrypt = RequestUtil.encodeDesMap(encryptData, '65102933', '32028092');
console.log('Encrypt: ', Encrypt);
result = Encrypt;
});
return result;

rpc.exports = {
   rpcfunc: hookTest
};
}

import requests, json
	import frida

	# 调用frida脚本
	process = frida.get_remote_device().attach("com.dodonew.online")
	script = process.create_script(jsCode)
	print('[*] Running')
	script.load()
	cipherText = script.exports.rpcfunc('123456', 'a123456')

	url = 'http://api.dodovip.com/api/user/login'
	data = json.dumps({"Encrypt": cipherText})
	headers = {
    "content-type": "application/json; charset=utf-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; Pixel Build/QP1A.191005.007.A3)"
	}
	html = requests.post(url=url, data=data, headers=headers)
	print(html.text)

pip install fastapi
pip install uvicorn

from fastapi import FastAPI
	import uvicorn
	import frida
	# 调用frida脚本
	process = frida.get_remote_device().attach("com.dodonew.online")
	script = process.create_script(jsCode)
	print('[*] Running')
	script.load()

	app = FastAPI()

	@app.get("/get")
	async def getEchoApi(item_id, item_user, item_pass):
    	result = script.exports.rpcfunc(item_user, item_pass)
    	return {"item_id": item_id, "item_retval": result}

	if __name__ == '__main__':
    	uvicorn.run(app, port=8080)