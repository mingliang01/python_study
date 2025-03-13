Java.perform(function () {
    var soAddr = Module.findBaseAddress("libxiaojianbang.so");
    var funAddr = soAddr.add(0x16BC);
    var jstr2cstr = new NativeFunction(funAddr, 'pointer', ['pointer','pointer']);
var env = Java.vm.tryGetEnv();
//主动调用jni函数newStringUtf，将JavaScript的字符串转为Java字符串
    var jstring = env.newStringUtf("xiaojianbang");
    var retval = jstr2cstr(env.handle, jstring);
    //var retval = jstr2cstr(env, jstring);
    console.log(retval.readCString());
});
//xiaojianbang