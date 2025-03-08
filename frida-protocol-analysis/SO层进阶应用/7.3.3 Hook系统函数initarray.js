function hook_dlopen(addr, soName, callback) {
    Interceptor.attach(addr, {
        onEnter: function (args) {
            var soPath = args[0].readCString();
            if(soPath.indexOf(soName) != -1) callback();
        }, onLeave: function (retval) {
        }
    });
}
var dlopen = Module.findExportByName("libdl.so", "dlopen");
var android_dlopen_ext = Module.findExportByName("libdl.so", "android_dlopen_ext");
hook_dlopen(dlopen, "libxiaojianbang.so", hook_call_constructors);
hook_dlopen(android_dlopen_ext, "libxiaojianbang.so", hook_call_constructors);

function hook_call_constructors() {
    var _symbols = Process.getModuleByName("linker64").enumerateSymbols();
    var call_constructors_addr = null;
    for (let i = 0; i < _symbols.length; i++) {
        var _symbol = _symbols[i];
        if(_symbol.name.indexOf("call_constructors") != -1){
            call_constructors_addr = _symbol.address;
        }
    }
    Interceptor.attach(call_constructors_addr, {
        onEnter: function (args) {
        	hook_initarray();
        }, onLeave: function (retval) {
        }
    });
}

function hook_initarray(){
    var xiaojianbangAddr = Module.findBaseAddress("libxiaojianbang.so");
    var func1_addr = xiaojianbangAddr.add(0x1D14);
    var func2_addr = xiaojianbangAddr.add(0x1D3C);
    var func3_addr = xiaojianbangAddr.add(0x1CEC);
    Interceptor.replace(func1_addr, new NativeCallback(function () {
        console.log("func1 is replaced!!!");
    }, 'void', []));
    Interceptor.replace(func2_addr, new NativeCallback(function () {
        console.log("func2 is replaced!!!");
    }, 'void', []));
    Interceptor.replace(func3_addr, new NativeCallback(function () {
        console.log("func3 is replaced!!!");
    }, 'void', []));
    Interceptor.detachAll();
}