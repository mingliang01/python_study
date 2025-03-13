function hook_jni() {
    var _symbols = Process.getModuleByName("libart.so").enumerateSymbols();
    var newStringUtf = null;
    for (let i = 0; i < _symbols.length; i++) {
        var _symbol = _symbols[i];
        if(_symbol.name.indexOf("CheckJNI") == -1 && _symbol.name.indexOf("NewStringUTF") != -1){
            newStringUtf = _symbol.address;
        }
    }
    Interceptor.attach(newStringUtf, {
        onEnter: function (args) {
            console.log("newStringUtf  args: ", args[1].readCString());
        }, onLeave: function (retval) {
            console.log("newStringUtf  retval: ", retval);
        }
    });
}
hook_jni();
/*
newStringUtf args:  GB2312
newStringUtf retval:  0x81
newStringUtf args:  41bef1ce7fdc3e42c0e5d940ad74ac00
newStringUtf retval:  0xa9
*/