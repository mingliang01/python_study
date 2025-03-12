declare class Module {
......
    static findBaseAddress(name: string): NativePointer | null;
static getBaseAddress(name: string): NativePointer;
}

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
console.log(soAddr);
//Module.getBaseAddress("libxiaojianbang.so")
//soAddr:  0x7b2e6c0000

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var funcAddr = soAddr.add(0x1ACC); 

declare class NativePointer {
    constructor(v: string | number | UInt64 | Int64 | NativePointerValue);
add(v: NativePointerValue | UInt64 | Int64 | number | string): NativePointer;
......
}

 var soAddr = 0x77ab999000;
 console.log( ptr(soAddr).add(0x1A0C) );  // ptr <=> new NativePointer

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var sub_1ACC = soAddr.add(0x1ACC);
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
//sub_1ACC onEnter args[0]:  0x7bc3bd66c0
//sub_1ACC onEnter args[1]:  0x7fda079fb4
//sub_1ACC onEnter args[2]:  0x5
//sub_1ACC onEnter args[3]:  0x6
//sub_1ACC onEnter args[4]:  0x7
//sub_1ACC onLeave retval:  0x12