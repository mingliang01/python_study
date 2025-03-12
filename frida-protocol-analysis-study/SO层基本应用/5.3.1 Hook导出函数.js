// 汇编和架构有关
var funcAddr = Module.findExportByName("libxiaojianbang.so", "Java_com_xiaojianbang_ndk_NativeHelper_add");
Interceptor.attach(funcAddr, {
    onEnter: function (args) {
        console.log(args[0]);
        console.log(args[1]);
        console.log(args[2]);
        console.log(this.context.rax);
        console.log(this.context.rcx);
        console.log(this.context.rdx);
        console.log(this.context.rbx);
        console.log(this.context.rsp);
        console.log(this.context.rbp);
        console.log(this.context.rsi);
        console.log(this.context.rdi);
        console.log(this.context.r8.toInt32());
        console.log(this.context.r9.toInt32());
        console.log(args[4].toUInt32());
    }, onLeave: function (retval) {
        console.log(retval.toInt32());
        console.log(this.context.r8);
        console.log("取r8寄存器的最后三个bit位", this.context.r8 & 0x7);
    }
});
//add函数触发以后的输出为
/*
0x7bc3bd66c0
0x7fda079fb4
0x5
6
7
18
0x12
取x0寄存器的最后三个bit位 2
*/