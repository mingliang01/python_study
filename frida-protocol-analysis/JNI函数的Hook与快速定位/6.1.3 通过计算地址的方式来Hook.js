var envAddr = Java.vm.tryGetEnv().handle.readPointer();
var NewStringUTF = envAddr.add(167 * Process.pointerSize);
var NewStringUTFAddr = envAddr.add(167 * Process.pointerSize).readPointer();
console.log(hexdump(NewStringUTF));
console.log(hexdump(NewStringUTFAddr));
console.log(Instruction.parse(NewStringUTFAddr).toString());
/*
6fa4fde428  ec 30 d7 a4 6f 00 00 00 a0 38 d7 a4 6f 00 00 00  .0..o....8..o...
6fa4fde438  50 40 d7 a4 6f 00 00 00 70 40 d7 a4 6f 00 00 00  P@..o...p@..o...

6fa4d730ec  ff 43 03 d1 fc 6f 07 a9 fa 67 08 a9 f8 5f 09 a9  .C...o...g..._..
6fa4d730fc  f6 57 0a a9 f4 4f 0b a9 fd 7b 0c a9 fd 03 03 91  .W...O...{......

sub sp, sp, #0xd0
*/

function hook_jni2() {
    var envAddr = Java.vm.tryGetEnv().handle.readPointer();
    var NewStringUTFAddr = envAddr.add(167 * Process.pointerSize).readPointer();
    Interceptor.attach(NewStringUTFAddr, {
        onEnter: function (args) {
            console.log("FindClass args: ", args[1].readCString());
        }, onLeave: function (retval) {
            console.log("FindClass retval: ", retval);
        }
    });
}
hook_jni2();
/*
newStringUtf args:  GB2312
newStringUtf retval:  0x81
newStringUtf args:  41bef1ce7fdc3e42c0e5d940ad74ac00
newStringUtf retval:  0xa9
*/