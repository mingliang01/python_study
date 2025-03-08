import frida,sys

	process=frida.get_usb_device().attach("com.dodonew.online")
	script=process.create_script(jsCode)
	script.load()		#脚本加载
	sys.stdin.read()	#CMD不会退出，便于控制台观察


jsCode="""
	Java.perform(function (){
    console.log("start hooking...");
    var jsonRequest = Java.use("com.dodonew.online.http.JsonRequest");
    var requestUtil = Java.use("com.dodonew.online.http.RequestUtil");
    var utils = Java.use("com.dodonew.online.util.Utils");
    jsonRequest.paraMap.implementation = function (a) {
        console.log("jsonRequest.paraMap is called");
        return this.paraMap(a);
    }
    jsonRequest.addRequestMap.overload('java.util.Map', 'int').implementation = function 	(addMap, a) {
        console.log("jsonRequest.addRequestMap is called");
        return this.addRequestMap(addMap, a);
    }
    requestUtil.encodeDesMap.overload('java.lang.String', 'java.lang.String', 	'java.lang.String').implementation = function (data, desKey, desIV) {
        console.log("data: ", data, desKey, desIV);
        var encodeDesMap = this.encodeDesMap(data, desKey, desIV);
        console.log("encodeDesMap: ", encodeDesMap);
        return encodeDesMap;
    }
    utils.md5.implementation = function (a) {
        console.log("sign data: ", a);
        var md5 = this.md5(a);
        console.log("sign: ", md5);
        return md5;
    }
});
"""