    function toBase64(data){
        var ByteString=Java.use("com.android.okhttp.okio.ByteString");
        console.log("ByteString:",ByteString);
        console.log(ByteString.of(data).base64());
    }