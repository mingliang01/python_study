function hook_dlopen(addr, soName, callback) {
    Interceptor.attach(addr, {
        onEnter: function (args) {
            var soPath = args[0].readCString();
            if(soPath.indexOf(soName) != -1) this.hook = true;
        }, onLeave: function (retval) {
            if (this.hook) {callback()}
        }
    });
}
var dlopen = Module.findExportByName("libdl.so", "dlopen");
var android_dlopen_ext = Module.findExportByName("libdl.so", "android_dlopen_ext");
hook_dlopen(dlopen, "libxiaojianbang.so", set_read_write_break);
hook_dlopen(android_dlopen_ext, "libxiaojianbang.so", set_read_write_break);

function set_read_write_break(){
    Process.setExceptionHandler(function(details) {
console.log(JSON.stringify(details, null, 2));
        Memory.protect(details.memory.address, Process.pointerSize, 'rwx');
        return true;
    });
    var addr = Module.findBaseAddress("libxiaojianbang.so").add(0x3DED);
    Memory.protect(addr, 8, '---');
}
/*
{
  "message": "access violation accessing 0x75ecd31e6b",
  "type": "access-violation",
  "address": "0x767e9e75c4",
  "memory": {
    "operation": "read",
    "address": "0x75ecd31e6b"
  },
  "context": {
    "pc": "0x767e9e75c4",
    "sp": "0x7fc2481e50",
    "x0": "0x7681a52188",
    "x1": "0x75ecd31e6b",
......
    "lr": "0x767e9e73f8"
  },
  "nativeContext": "0x7fc2480c70"
}
*/


......
function set_read_write_break(){
    Process.setExceptionHandler(function(details) {
        console.log(JSON.stringify(details, null, 2));
        console.log("lr", DebugSymbol.fromAddress(details.context.lr));
        console.log("pc", DebugSymbol.fromAddress(details.context.pc));
        Memory.protect(details.memory.address, Process.pointerSize, 'rwx');
        console.log(Thread.backtrace(details.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n') + '\n');
        return true;
    });
    var addr = Module.findBaseAddress("libxiaojianbang.so").add(0x3DED);
    Memory.protect(addr, 8, '---');
}
/*
{
  "message": "access violation accessing 0x75eaff1e6b",
  ......
  "nativeContext": "0x7fc2480c70"
}
lr 0x767e9e73f8 libc.so!__vfprintf+0x3c
pc 0x767e9e75c4 libc.so!__vfprintf+0x208
0x767e9e73f8 libc.so!__vfprintf+0x3c
......
0x75eafefe08 libxiaojianbang.so!_Z6myInitv+0x20
0x75eafefe34 libxiaojianbang.so!JNI_OnLoad+0x24
......
*/