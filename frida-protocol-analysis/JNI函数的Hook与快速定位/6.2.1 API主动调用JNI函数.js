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
            var cstr = Java.vm.tryGetEnv().getStringUtfChars(retval);
            console.log(hexdump(cstr));
            console.log("newStringUtf  retval: ", cstr.readCString());
        }
    });
}
hook_jni();
/*
newStringUtf  args:  GB2312
6f94653dc0  47 42 32 33 31 32 00 00 00 00 00 00 00 00 00 00  GB2312..........
6f94653dd0  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
newStringUtf  retval:  GB2312

newStringUtf  args:  41bef1ce7fdc3e42c0e5d940ad74ac00
6f96e081d0  34 31 62 65 66 31 63 65 37 66 64 63 33 65 34 32  41bef1ce7fdc3e42
6f96e081e0  63 30 65 35 64 39 34 30 61 64 37 34 61 63 30 30  c0e5d940ad74ac00
newStringUtf  retval:  41bef1ce7fdc3e42c0e5d940ad74ac00
*/