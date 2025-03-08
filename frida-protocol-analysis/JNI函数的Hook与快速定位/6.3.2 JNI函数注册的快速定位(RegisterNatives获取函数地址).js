var RegisterNativesAddr = null;
var _symbols = Process.findModuleByName("libart.so").enumerateSymbols();
for (var i = 0; i < _symbols.length; i++) {
    var _symbol = _symbols[i];
    if (_symbol.name.indexOf("CheckJNI") == -1 && _symbol.name.indexOf("RegisterNatives") != -1) {
        RegisterNativesAddr = _symbols[i].address;
    }
}
console.log(RegisterNativesAddr);
// 0x7da0a0a158


var RegisterNativesAddr = null;
var _symbols = Process.findModuleByName("libart.so").enumerateSymbols();
for (var i = 0; i < _symbols.length; i++) {
    var _symbol = _symbols[i];
    if (_symbol.name.indexOf("CheckJNI") == -1 && _symbol.name.indexOf("RegisterNatives") != -1) {
        RegisterNativesAddr = _symbols[i].address;
    }
}

Interceptor.attach(RegisterNativesAddr, {
    onEnter: function (args) {
        var env = Java.vm.tryGetEnv();
        var className = env.getClassName(args[1]);
        var methodCount = args[3].toInt32();

        for (let i = 0; i < methodCount; i++) {
            var methodName = args[2].add(Process.pointerSize * 3 * i)
.readPointer().readCString();
            var signature = args[2].add(Process.pointerSize * 3 * i)
.add(Process.pointerSize).readPointer().readCString();
            var fnPtr = args[2].add(Process.pointerSize * 3 * i)
.add(Process.pointerSize * 2).readPointer();
            var module = Process.findModuleByAddress(fnPtr);
            console.log(className, methodName, signature, fnPtr, module.name, fnPtr.sub(module.base));
        }
    }, onLeave: function (retval) {
    }
});