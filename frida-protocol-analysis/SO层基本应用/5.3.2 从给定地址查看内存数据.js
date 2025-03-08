declare function hexdump(target: ArrayBuffer | NativePointerValue, options?: HexdumpOptions): string;
interface HexdumpOptions {
    offset?: number;	//从给定的target偏移一定字节数开始dump，默认为0
    length?: number;	//指定dump的字节数，注意需要十进制的数值，默认16*16
    header?: boolean;	//返回的string中是否包含标题，默认为true
    ansi?: boolean;	//返回的string是否带颜色，默认为false
}

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var data = hexdump(soAddr, {length: 16, header: false});
console.log(data);
//  74c6c39000  7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00  .ELF............

var soAddr = Module.findBaseAddress("libxiaojianbang.so");
var data = hexdump(soAddr, {offset: 4, length: 16, header: false});
console.log(data);
//  74c6c39004  02 01 01 00 00 00 00 00 00 00 00 00     