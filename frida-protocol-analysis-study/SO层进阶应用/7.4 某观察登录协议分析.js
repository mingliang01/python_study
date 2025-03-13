objection -g com.xxxx explore

android hooking watch class_method java.lang.String.getBytes

android hooking watch class_method java.lang.String.getBytes --dump-args --dump-return --dump-backtrace

com.xxxx.util.SignManager.getSign(Native Method)

android hooking watch class_method com.sichuanol.cbgc.util.SignManager.getSign --dump-args --dump-return --dump-backtrace

// frida -U -f com.xxxx --no-pause -l sohook.js
var dlsymAddr = Module.findExportByName("libdl.so", "dlsym");
Interceptor.attach(dlsymAddr, {
    onEnter: function (args) {
        this.args1 = args[1];
    }, onLeave: function (retval) {
        var module = Process.findModuleByAddress(retval);
        if(module == null) return;
        console.log(this.args1.readCString(), module.name, retval, retval.sub(module.base));
    }
});
/*
......
Java_com_sichuanol_cbgc_util_SignManager_getSign libwtf.so 0xc7eec931 0x931
......
*/


var soAddr = Module.findBaseAddress("libwtf.so");
var funcAddr = soAddr.add(0xC90 + 1);
Interceptor.attach(funcAddr, {
    onEnter: function (args) {
        console.log(args[0].readCString());
        console.log(args[1].toInt32())
        this.args2 = args[2];
    }, onLeave: function (retval) {
        console.log(hexdump(this.args2));
    }
});
/*
0093CB6721DAF15D31CFBC9BBE3A2B791634889785234
45
fff1ba84  74 77 62 6e 52 51 a4 71 a5 b3 3e 63 40 31 c6 f3  twbnRQ.q..>c@1..
*/