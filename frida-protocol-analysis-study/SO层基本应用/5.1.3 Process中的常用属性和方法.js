declare namespace Process {
    const id: number;
    const arch: Architecture;
    const platform: Platform;
    const pageSize: number;
    const pointerSize: number;
    ......
    function getCurrentThreadId(): ThreadId;
    function findModuleByAddress(address: NativePointerValue): Module | null;
    function getModuleByAddress(address: NativePointerValue): Module;
    function findModuleByName(name: string): Module | null;
    function getModuleByName(name: string): Module;
    function enumerateModules(): Module[];
    function findRangeByAddress(address: NativePointerValue): RangeDetails | null;
    function getRangeByAddress(address: NativePointerValue): RangeDetails;
    function setExceptionHandler(callback: ExceptionHandlerCallback): void;
}

console.log("pid: ", Process.id);
console.log("arch: ", Process.arch);
console.log("platform: ", Process.platform);
console.log("pageSize: ", Process.pageSize);
console.log("pointerSize: ", Process.pointerSize);
console.log("CurrentThreadId: ", Process. getCurrentThreadId());
var soAddr = Process.findModuleByName("libxiaojianbang.so").base;
console.log("soAddr: ", soAddr);
var range = Process.findRangeByAddress(Process.findModuleByName("libxiaojianbang.so").base);
console.log("Range: ", JSON.stringify(range));
/*
pid:  13170
arch:  arm64
platform:  linux
pageSize:  4096
pointerSize:  8
CurrentThreadId:  13231
soAddr:  0x743a8e2000
Range:  {"base":"0x743a8e2000","size":20480,"protection":"r-x","file":{"path":"/data/app/com.xiaojianbang.app-Qj8kZpS2qmejJj88S35LnQ==/lib/arm64/libxiaojianbang.so","offset":0,"size":0}}
*/