function hook_JNIOnload() {
    var JNI_OnLoad = Module.findExportByName("libxiaojianbang.so", "JNI_OnLoad");
    Interceptor.attach(JNI_OnLoad, {
        onEnter: function(args){
            console.log(args[0]);
        }, onLeave: function(retval){
            console.log(retval);
        }
    });
}
function hook_dlopen(addr, soName, callback) {
    Interceptor.attach(addr, {
        onEnter: function(args){
            var name = args[0].readCString();
            if(name.indexOf(soName) != -1) this.hook = true;
        }, onLeave: function(retval){
            if(this.hook) callback();
        }
    });
}
var dlopen = Module.findExportByName("libdl.so", "dlopen");
var android_dlopen_ext = Module.findExportByName("libdl.so", "android_dlopen_ext");
hook_dlopen(dlopen, "libxiaojianbang.so", hook_JNIOnload);
hook_dlopen(android_dlopen_ext, "libxiaojianbang.so", hook_JNIOnload);
/*
0x7a4faaf1c0
0x10006		// JNIOnload函数必须返回一个合理的jni版本号，这里返回的是1.6
*/ 