private void paraMap(Map<String, String> addMap) {
        String encrypt;
        String time = System.currentTimeMillis() + "";
        if (addMap == null) {
            addMap = new HashMap<>();
        }
        if (this.useDes) {
            addMap.put("timeStamp", time);
            if (DodonewOnlineApplication.loginUser != null) {
                addMap.put("userId", 											                    DodonewOnlineApplication.loginUser.getUserId());
                if (TextUtils.isEmpty(DodonewOnlineApplication.devId)) {
                    DodonewOnlineApplication.devId = 	
			 		Utils.getDevId(DodonewOnlineApplication.getAppContext());
                }
                addMap.put("imei", "Android" + DodonewOnlineApplication.devId);
            }
            encrypt = RequestUtil.encodeDesMap(RequestUtil.paraMap(addMap, 
Config.BASE_APPEND, "sign"), this.desKey, this.desIV);
        } else {
            encrypt = this.mGson.toJson(addMap);
        }
        JSONObject obj = new JSONObject();
        try {
            obj.put("Encrypt", encrypt);
            this.mRequestBody = obj + "";
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

// 第一次尝试，结果没有输出
Java.perform(function(){
    var josnRequest=Java.use("com.dodonew.online.http.JsonRequest");
    josnRequest.paraMap.implementation=function(a){
        console.log("jsonRequest.paraMap is called!");
        return this.paraMap(a);
    }})

// 换一个函数hook
    josnRequest.addRequestMap.overload('java.util.Map', 'int').implementation=function(a,b){
        console.log("jsonRequest.addRequestMap is called!");
        return this.addRequestMap(a,b);


  public void addRequestMap(Map<String, String> addMap, int a) {
        String time = System.currentTimeMillis() + "";
        if (addMap == null) {addMap = new HashMap<>();}
        addMap.put("timeStamp", time);
        String encrypt = RequestUtil.encodeDesMap(
RequestUtil.paraMap(addMap, Config.BASE_APPEND, "sign"), 
this.desKey, 
this.desIV);
        JSONObject obj = new JSONObject();
        try {
            obj.put("Encrypt", encrypt);
            this.mRequestBody = obj + "";
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }

// hook encodeDesMap 函数
    var encodeDesMap=Java.use("com.dodonew.online.http.RequestUtil");
    encodeDesMap.encodeDesMap.overload
('java.lang.String', 'java.lang.String', 'java.lang.String').implementation=function(a,b,c){
        console.log("encodeDesMap.encodeDesMap is called!");
        console.log("data:",a);
        console.log("deskey:",b);
        console.log("desiv:",c);
console.log("result:",this.encodeDesMap(a,b,c))
        return this.encodeDesMap(a,b,c);
    };


public static String paraMap(Map<String, String> addMap, String append, String sign) {
        try {
            Set<String> keyset = addMap.keySet();
            StringBuilder builder = new StringBuilder();
            List<String> list = new ArrayList<>();
            for (String keyName : keyset) {
                list.add(keyName + "=" + addMap.get(keyName));
            }
            Collections.sort(list);
            for (int i = 0; i < list.size(); i++) {
                builder.append(list.get(i));
                builder.append("&");
            }
            builder.append("key=" + append);
            addMap.put("sign", Utils.md5(builder.toString()).toUpperCase());
            String result = new Gson().toJson(sortMapByKey(addMap));
            Log.w(AppConfig.DEBUG_TAG, result + "   result");
            return result;
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    // hook md5 函数
    var md5Str=Java.use("com.dodonew.online.util.Utils");
    md5Str.md5.implementation=function(a){
        console.log("md5Str:",a);
        return this.md5(a);
    }