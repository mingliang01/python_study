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
            console.log(Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join("\n") + "\n");
            console.log("newStringUtf  args: ", args[1].readCString());
        }, onLeave: function (retval) {
        }
    });
}
hook_jni();
/*
0x79ca9793a8 libart.so!_ZN3art12_GLOBAL__N_18CheckJNI12NewStringUTFEP7_JNIEnvPKc+0x2bc
0x79604347f8 libxiaojianbang.so!_ZN7_JNIEnv12NewStringUTFEPKc+0x2c
0x7960434fd0 libxiaojianbang.so!Java_com_xiaojianbang_ndk_NativeHelper_md5+0x194
0x79ca75a354 libart.so!art_quick_generic_jni_trampoline+0x94
0x79ca7515bc libart.so!art_quick_invoke_static_stub+0x23c
......
newStringUtf  args:  41bef1ce7fdc3e42c0e5d940ad74ac00
*/