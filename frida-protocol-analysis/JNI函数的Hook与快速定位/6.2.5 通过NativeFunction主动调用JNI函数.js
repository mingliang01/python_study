var symbols = Process.getModuleByName("libart.so").enumerateSymbols();
var NewStringUTFAddr = null;
var GetStringUTFCharsAddr = null;
for (var i = 0; i < symbols.length; i++) {
    var symbol = symbols[i];
    if(symbol.name.indexOf("CheckJNI") == -1 && symbol.name.indexOf("NewStringUTF") != -1){
        NewStringUTFAddr = symbol.address;
    }else if (symbol.name.indexOf("CheckJNI") == -1 && symbol.name.indexOf("GetStringUTFChars") != -1){
        GetStringUTFCharsAddr = symbol.address;
    }
}
var NewStringUTF = new NativeFunction(NewStringUTFAddr, 'pointer', ['pointer', 'pointer']);
var GetStringUTFChars = new NativeFunction(GetStringUTFCharsAddr, 'pointer', ['pointer', 'pointer', 'pointer']);

var jstring = NewStringUTF(Java.vm.tryGetEnv().handle, Memory.allocUtf8String("xiaojianbang"));
console.log(jstring);

var cstr = GetStringUTFChars(Java.vm.tryGetEnv(),  jstring,  ptr(0));
console.log(cstr.readCString());
/*
0x1
xiaojianbang
*/


var cstr = GetStringUTFChars(Java.vm.tryGetEnv(),  jstring,  Memory.alloc(1).writeS8(1));
console.log(cstr.readCString());
//xiaojianbang


//......
var GetStringUTFChars = new NativeFunction(GetStringUTFCharsAddr, 'pointer', ['pointer', 'pointer']);
var cstr = GetStringUTFChars(Java.vm.tryGetEnv(),  jstring);
console.log(cstr.readCString());
//xiaojianbang