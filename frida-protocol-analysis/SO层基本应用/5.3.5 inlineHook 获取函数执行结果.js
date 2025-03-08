var hookAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x1AF4);
Interceptor.attach(hookAddr, {
    onEnter: function (args) {
        console.log("onEnter x8: ", this.context.x8.toInt32());
        console.log("onEnter x9: ", this.context.x9.toInt32());
    }, onLeave: function (retval) {
        console.log("onLeave x0: ", this.context.x0.toInt32());
    }
});
/*
onEnter x8:  11
onEnter x9:  7
onLeave x0:  18
*/

var hookAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x1FF4);
Interceptor.attach(hookAddr, {
    onEnter: function (args) {
        console.log("onEnter: ", this.context.x1);
        console.log("onEnter: ", hexdump(this.context.x1));
    }, onLeave: function (retval) {
    }
});
/*
onEnter:  0x7d9016ae80
7d9016ae80  78 69 61 6f 6a 69 61 6e 62 61 6e 67 00 00 c0 41  xiaojianbang...A
*/