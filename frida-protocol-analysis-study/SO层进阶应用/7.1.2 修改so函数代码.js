var funcAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x1ACC);
var opcodes = funcAddr.readByteArray(16);
console.log(opcodes);
/*
00000000  ff 83 00 d1 e0 0f 00 f9 e1 0b 00 f9 e2 0f 00 b9  ................
*/

var funcAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x1ACC);
var asm = Instruction.parse(funcAddr);
console.log(asm);
for (var i = 0; i < 3; i++) {
    asm = Instruction.parse(asm.next);
    console.log(asm);
}
/*
sub sp, sp, #0x20
str x0, [sp, #0x18]
str x1, [sp, #0x10]
str w2, [sp, #0xc]
*/

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
soAddr.add(0x1AF4).writeByteArray(hexToBytes("0001094B"));
console.log(Instruction.parse(soAddr.add(0x1AF4)));
// sub w0, w8, w9

// 通常是进入函数的第一步，提升函数栈空间，需要16字节对齐
SUB  SP, SP, #0x20
// 也是arm汇编进入函数的基本操作，保存寄存器中的参数到栈中
// 内存中的数据CPU无法直接运算，会使用str/ldr来操作数据
// str用于将寄存器中的值保存到内存中，ldr用于将内存中的值加载到寄存器中
// x0、x1对应实参JNIEnv*、jclass，因为是指针，所以用64位寄存器
// w2、w3、w4分别对应实战5、6、7，源码中定义的类型是int，所以用32位寄存器
STR  X0, [SP,#0x20+var_8]
STR  X1, [SP,#0x20+var_10]
STR  W2, [SP,#0x20+var_14]
STR  W3, [SP,#0x20+var_18]
STR  W4, [SP,#0x20+var_1C]
// var_14中的值加载到w8中，var_14之前保存了w2的值5，这一句相当于w8 = 5
LDR  W8, [SP,#0x20+var_14]
// var_18中的值加载到w9中，var_18之前保存了w3的值6，这一句相当于w9 = 6
LDR  W9, [SP,#0x20+var_18]
// w8 = w8 + w9  =>  w8 = 11
ADD  W8, W8, W9
// var_1C中的值加载到w9中，var_1C之前保存了w4的值7，这一句相当于w9 = 7
LDR  W9, [SP,#0x20+var_1C]
// w0 = w8 + w9  =>  w0 = 11 + 7  =>  w0 = 18
// arm64中，函数返回值存放于w0/x0
ADD  W0, W8, W9
// 释放栈空间
ADD  SP, SP, #0x20
// 相当于bl  lr，返回
RET


var soAddr = Module.findBaseAddress("libxiaojianbang.so");
new Arm64Writer(soAddr.add(0x1AEC)).putNop();
console.log(Instruction.parse(soAddr.add(0x1AEC)).toString());
// nop


......
STR  W2, [SP,#0x20+var_14]
STR  W3, [SP,#0x20+var_18]
STR  W4, [SP,#0x20+var_1C]
// var_14中的值加载到w8中，var_14之前保存了w2的值5，这一句相当于w8 = 5
LDR  W8, [SP,#0x20+var_14]
LDR  W9, [SP,#0x20+var_18]
NOP
// var_1C中的值加载到w9中，var_1C之前保存了w4的值7，这一句相当于w9 = 7
LDR  W9, [SP,#0x20+var_1C]
// 之前修改的，在app重启之前都生效。w0 = w8 - w9  =>  w0 = 5 - 7  =>  w0 = -2
SUB  W0, W8, W9
......

var codeAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x1AF4);
Memory.patchCode(codeAddr, 4, function (code) {
    var writer = new Arm64Writer(code, { pc: codeAddr });
    writer.putBytes(hexToBytes("0001094B"));   //sub w0, w8, w9
    writer.flush();
});

function hook_func() {
    var soAddr = Module.findBaseAddress("libxiaojianbang.so");
    var MD5Final = soAddr.add(0x3A78);
    console.log(hexdump(MD5Final.readByteArray(20)));
    Interceptor.attach(MD5Final, {
        onEnter: function (args) {
            console.log(hexdump(MD5Final.readByteArray(20)));
        }, onLeave: function (retval) {
        }
    });
}
hook_func();
/*
00000000  ff 43 01 d1 fd 7b 04 a9 fd 03 01 91 48 d0 3b d5  .C...{......H.;.
00000010  08 15 40 f9                                      ..@.

00000000  50 00 00 58 00 02 1f d6 00 96 33 3e 74 00 00 00  P..X......3>t...
00000010  08 15 40 f9                                      ..@.
*/

