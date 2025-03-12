var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var sub_1ACC = soAddr.add(0x1C00);
Interceptor.attach(sub_1ACC, {
    onEnter: function (args) {
        console.log("sub_1ACC onEnter args[0]: ", args[0]);
        console.log("sub_1ACC onEnter args[1]: ", args[1]);
        console.log("sub_1ACC onEnter args[2]: ", args[2]);
        console.log("sub_1ACC onEnter args[3]: ", args[3]);
        console.log("sub_1ACC onEnter args[4]: ", args[4]);
    }, onLeave: function (retval) {
        console.log("sub_1ACC onLeave retval: ", retval);
    }
});