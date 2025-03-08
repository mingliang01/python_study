Java.perform(function(){
    var ByteString = Java.use("com.android.okhttp.okio.ByteString");
    function toBase64(data) {
        console.log(" Base64: ", ByteString.of(data).base64());
    }
    function toHex(data) {
        console.log(" Hex: ", ByteString.of(data).hex());
    }
    function toUtf8(data) {
        console.log(" Utf8: ", ByteString.of(data).utf8());
    }
    toBase64([48,49,50,51,52]);
    toUtf8([48,49,50,51,52]);
    toHex([48,49,50,51,52]);
})