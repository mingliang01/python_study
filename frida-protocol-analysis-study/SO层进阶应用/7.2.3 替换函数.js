declare namespace Interceptor {
    function replace(target: NativePointerValue, replacement: NativePointerValue,
        data?: NativePointerValue): void;
}

declare class NativeCallback extends NativePointer {
constructor(func: NativeCallbackImplementation, retType: NativeType, argTypes:
 NativeType[], abi?: NativeABI);
}

function hook_func() {
    var md5Func = Module.findBaseAddress("libxiaojianbang.so").add(0x1F2C);
    Interceptor.replace(md5Func, new NativeCallback(function () {
        
    }, "void", [ ]));
}
hook_func();
//logcat中的输出为
//CMD5 md5Result: null

function hook_func() {
    var md5Func = Module.findBaseAddress("libxiaojianbang.so").add(0x1F2C);
    Interceptor.replace(md5Func, new NativeCallback(function () {
        return 100;
    }, "int", []));
}
hook_func();
//该函数触发后，app崩溃


function hook_func() {
    var md5Func = Module.findBaseAddress("libxiaojianbang.so").add(0x1F2C);
    Interceptor.replace(md5Func, new NativeCallback(function (env, jclass, data) {
        console.log(env);
        console.log(jclass);
        console.log(Java.vm.tryGetEnv().getStringUtfChars(data).readCString());
        return Java.vm.tryGetEnv().newStringUtf("this is return value");
    }, "pointer", ["pointer", "int", "pointer"]));
}
hook_func();
/*
0x7a4fb206c0
-420895324
xiaojianbang
//logcat中的输出为
CMD5 md5Result: this is return value
*/

function hook_func() {
    var md5Addr = Module.findBaseAddress("libxiaojianbang.so").add(0x1F2C);
    var md5Func = new NativeFunction(md5Addr, "pointer", ["pointer", "pointer", "pointer"]);
    Interceptor.replace(md5Addr, new NativeCallback(function (env, jclass, data) {
        var fridaEnv = Java.vm.tryGetEnv();
        console.log(env, jclass, fridaEnv.getStringUtfChars(data).readCString());
        var retval = md5Func(env, jclass, data);
        console.log(fridaEnv.getStringUtfChars(retval).readCString());
        return retval;
    }, "pointer", ["pointer", "pointer", "pointer"]));
}
hook_func();
/*
0x7a4fb206c0 0x7fe6e9a5a4 xiaojianbang
41bef1ce7fdc3e42c0e5d940ad74ac00
//logcat中的输出为
CMD5 md5Result: 41bef1ce7fdc3e42c0e5d940ad74ac00
*/