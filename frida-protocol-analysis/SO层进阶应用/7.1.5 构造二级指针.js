var strAddr = Memory.alloctoUtf8String("dajianbang");
console.log(hexdump(strAddr));
var finalAddr = Memory.alloc(8).writePointer(strAddr);
console.log(hexdump(finalAddr));
xiugaiStr(finalAddr);
console.log(hexdump(strAddr));