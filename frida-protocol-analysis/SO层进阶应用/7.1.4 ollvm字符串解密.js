var soAddr = Module.findBaseAddress("liblogin_encrypt.so");
console.log(soAddr.add(0xD060).readCString());
// java/security/KeyFactory


var  xiugaiStrAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x1B00);
var  xiugaiStr = new NativeFunction(xiugaiStrAddr,  'int64',  ['pointer']);

var strAddr = Memory.allocUtf8String("dajianbang");
console.log(hexdump(strAddr));
/*7d95814930  64 61 6a 69 61 6e 62 61 6e 67 00 98 7d 00 00 00  dajianbang..}...
*/

var finalAddr = Memory.alloc(8).writePointer(strAddr);
console.log(hexdump(finalAddr));
/*
7d95142920  30 49 81 95 7d 00 00 00 22 6c 6f 67 22 2c 22 6c  0I..}..."log","l
*/

xiugaiStr(finalAddr);
console.log(hexdump(strAddr));
/*
7d9582dfe0  64 61 6a 69 61 6e 62 61 6e 67 20 51 51 32 34 33  dajianbang QQ243
7d9582dff0  35 38 37 35 37 00 00 00 03 04 00 00 00 00 00 00  58757...........
*/