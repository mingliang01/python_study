var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var addFunc = soAddr.add(0x1ACC);
Interceptor.attach(addFunc, {
    onEnter: function (args) {
        args[2] = ptr(100);
//this.context.x2 = 100;
        console.log(args[2].toInt32());
    }, onLeave: function (retval) {
        console.log(retval.toInt32());
        retval.replace(100);
//this.context.x0 = 100;
    }
});
/*
args[2]:  100
retval:  113
//logcat中的输出为
//CADD addResult: 100
*/