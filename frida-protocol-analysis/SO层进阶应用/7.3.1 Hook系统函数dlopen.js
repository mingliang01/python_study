function hook_func() {
    var myInit = Module.findBaseAddress("libxiaojianbang.so").add(0x1DE8);
    Interceptor.replace(myInit,  new NativeCallback(function () {
        console.log("replace myInit success");
    }, "void",  [ ]));
}
function hook_dlopen() {
    var android_dlopen_ext = Module.findExportByName("libdl.so", "android_dlopen_ext");
    Interceptor.attach(android_dlopen_ext, {
        onEnter: function (args) {
            var soPath = args[0].readCString();
            if(soPath.indexOf("libxiaojianbang.so") != -1) this.hook = true;
        }, onLeave: function (retval) {
            if(this.hook)  hook_func();
        }
    });
}
hook_dlopen();
// replace myInit success


function hook_func() {
    var myInit = Module.findBaseAddress("libxiaojianbang.so").add(0x1DE8);
    Interceptor.replace(myInit,  new NativeCallback(function () {
        console.log("replace myInit success");
    }, "void",  [ ]));
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
hook_dlopen(dlopen, "libxiaojianbang.so", hook_func);
hook_dlopen(android_dlopen_ext, "libxiaojianbang.so", hook_func);
// replace myInit success