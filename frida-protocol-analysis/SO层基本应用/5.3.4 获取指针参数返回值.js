var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var MD5Final = soAddr.add(0x3A78);
Interceptor.attach(MD5Final, {
    onEnter: function (args) {
        this.args1 = args[1];
    }, onLeave: function (retval) {
        console.log(hexdump(this.args1));
    }
});
/*
7ffc689cc8  41 be f1 ce 7f dc 3e 42 c0 e5 d9 40 ad 74 ac 00  A.....>B...@.t..
//logcat中的输出结果
//CMD5 md5Result: 41bef1ce7fdc3e42c0e5d940ad74ac00
*/