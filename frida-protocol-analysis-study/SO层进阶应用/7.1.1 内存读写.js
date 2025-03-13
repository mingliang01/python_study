type PageProtection = string;
declare namespace Memory {
function protect(address: NativePointerValue, size: number | UInt64, protection: PageProtection): boolean;
......
}

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
Memory.protect(soAddr.add(0x3DED), 16, 'rwx');

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
console.log(soAddr.add(0x3DED).readCString());
// com/xiaojianbang/ndk/NativeHelper

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
console.log(hexdump(soAddr.add(0x3DED)));
/*
795b345ded  63 6f 6d 2f 78 69 61 6f 6a 69 61 6e 62 61 6e 67  com/xiaojianbang
795b345dfd  2f 6e 64 6b 2f 4e 61 74 69 76 65 48 65 6c 70 65  /ndk/NativeHelpe
795b345e0d  72 00 65 6e 63 6f 64 65 00 28 29 4c 6a 61 76 61  r.encode.()Ljava
*/

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
console.log(soAddr.add(0x3DED).readByteArray(16));
/*
00000000  63 6f 6d 2f 78 69 61 6f 6a 69 61 6e 62 61 6e 67  com/xiaojianbang
*/

declare class NativePointer {
writeByteArray(value: ArrayBuffer | number[]): NativePointer;
}

// 将字符串转为字节数组
function stringToBytes(str){
    return hexToBytes(stringToHex(str));
}
// 将字符串进行hex编码
function stringToHex(str) {
    return str.split("").map(function(c) {
        return ("0" + c.charCodeAt(0).toString(16)).slice(-2);
    }).join("");
}
// 将hex编码的数据转为字节数组
function hexToBytes(hex) {
    for (var bytes = [], c = 0; c < hex.length; c += 2)
        bytes.push(parseInt(hex.substr(c, 2), 16));
    return bytes;
}
// 将hex编码的数据转为字符串
function hexToString(hexStr) {
    var hex = hexStr.toString();
    var str = '';
    for (var i = 0; i < hex.length; i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var tmpAddr = soAddr.add(0x3DED);
Memory.protect(tmpAddr, 16, 'rwx');
console.log(hexdump( tmpAddr.writeByteArray(stringToBytes("xiaojianbang\0")) ));
/*
795b345ded  78 69 61 6f 6a 69 61 6e 62 61 6e 67 00 64 65 66  xiaojianbang.def
*/

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var tmpAddr = soAddr.add(0x3DED);
Memory.protect(tmpAddr, 16, 'rwx');
console.log(hexdump( tmpAddr.writeByteArray(hexToBytes("0123456789abcdeffedcba9876543210")) ));
/*
795b345ded  01 23 45 67 89 ab cd ef fe dc ba 98 76 54 32 10  .#Eg........vT2.
*/

declare namespace Memory {
function alloc(size: number | UInt64, options?: MemoryAllocOptions): NativePointer;
function allocUtf8String(str: string): NativePointer;
}

var addr = Memory.alloc(8);
addr.writeByteArray(hexToBytes("eeeeeeeeeeeeeeee"));
console.log(addr.readByteArray(8));
/*
00000000  ee ee ee ee ee ee ee ee                          ........
*/

var addr = Memory.allocUtf8String("小肩膀8888");
console.log(addr.readByteArray(16));
/*
00000000  e5 b0 8f e8 82 a9 e8 86 80 38 38 38 38 00 00 00  .........8888...
*/