Log.getStackTraceString(new Throwable());

function showStacks(){
    Java.perform(function(){
        console.log(
            Java.use("android.util.Log").getStackTraceString(
                    Java.use("java.lang.Throwable").$new()));
    });
}

var hashMap = Java.use("java.util.HashMap");
hashMap.put.implementation = function (a, b) {
    if(a == "username"){
        showStacks();
        console.log("hashMap.put: ", a, b);
    }
    return this.put(a, b);
}

private void login(String userName, String pwd) {
	this.DEFAULT_TYPE = new TypeToken<RequestResult<User>>() {
	}.getType();
	this.para.clear();
	this.para.put("username", userName);
	this.para.put("userPwd", pwd);
	if (TextUtils.isEmpty(DodonewOnlineApplication.devId)) {
		DodonewOnlineApplication.devId = Utils.getDevId(DodonewOnlineApplication.getAppContext());
	}
	this.para.put("equtype", Config.equtype);
	this.para.put("loginImei", "Android" + DodonewOnlineApplication.devId);
	requestNetwork("user/login", this.para, this.DEFAULT_TYPE);
}