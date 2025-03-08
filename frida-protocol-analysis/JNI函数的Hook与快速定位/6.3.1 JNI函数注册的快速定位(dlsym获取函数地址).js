var dlsymAddr = Module.findExportByName("libdl.so", "dlsym");
Interceptor.attach(dlsymAddr, {
    onEnter: function (args) {
        this.args1 = args[1];
    }, onLeave: function (retval) {
        console.log(this.args1.readCString(),  retval);
    }
});
/*
//app以spawn的方式启动，得到如下输出
oatdata 0x7d360c3000
......
oatdatabimgrelro 0x0
HMI 0x7d33c94018
//点击CADD按钮后输出，之后不再触发
JNI_OnLoad 0x7d337abe10
Java_com_xiaojianbang_ndk_NativeHelper_add 0x7d337abacc
//点击CMD5按钮后输出，之后不再触发
Java_com_xiaojianbang_ndk_NativeHelper_md5 0x7d337abf2c
*/

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
JNI_OnLoad libxiaojianbang.so 0x7d91131e10 0x1e10
Java_com_xiaojianbang_ndk_NativeHelper_add libxiaojianbang.so 0x7d91131acc 0x1acc
Java_com_xiaojianbang_ndk_NativeHelper_md5 libxiaojianbang.so 0x7d91131f2c 0x1f2c
*/