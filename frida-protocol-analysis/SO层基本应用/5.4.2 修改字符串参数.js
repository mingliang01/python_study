var MD5Update = Module.findExportByName("libxiaojianbang.so", "_Z9MD5UpdateP7MD5_CTXPhj");
Interceptor.attach(MD5Update, {
    onEnter: function (args) {
        console.log(hexdump(args[1]));  //hexdump用于从给定的地址开始，dump一段内存
        console.log(args[2].toInt32());
    }, onLeave: function (retval) {
    }
});
/*
7ad0ca9f40  78 69 61 6f 6a 69 61 6e 62 61 6e 67 00 00 c0 41  xiaojianbang...A
12

7ad042e000  80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
44

7fda079e50  60 00 00 00 00 00 00 00 ed 17 ae 39 cf 5d 07 be  `..........9.]..
8
//logcat中的输出结果
//CMD5 md5Result: 41bef1ce7fdc3e42c0e5d940ad74ac00
*/

function stringToBytes(str){
    return hexToBytes(stringToHex(str));
}
function stringToHex(str) {
    return str.split("").map(function(c) {
        return ("0" + c.charCodeAt(0).toString(16)).slice(-2);
    }).join("");
}
function hexToBytes(hex) {
    for (var bytes = [], c = 0; c < hex.length; c += 2)
        bytes.push(parseInt(hex.substr(c, 2), 16));
    return bytes;
}
var MD5Update = Module.findExportByName("libxiaojianbang.so", "_Z9MD5UpdateP7MD5_CTXPhj");
Interceptor.attach(MD5Update, {
    onEnter: function (args) {
        if(args[1].readCString() == "xiaojianbang"){
             let newStr = "xiaojian\0";
             args[1].writeByteArray(stringToBytes(newStr));
             console.log(hexdump(args[1]));
             args[2] = ptr(newStr.length - 1);
             console.log(args[2].toInt32());
        }
    }, onLeave: function (retval) {
    }
});
/*
7b2e35bf50  78 69 61 6f 6a 69 61 6e 00 61 6e 67 00 00 c0 41  xiaojian.ang...A
8
//logcat中的输出结果
//CMD5 md5Result: 66b0451b7a00d82790d4910a7a3a4162
*/


var MD5Update = Module.findExportByName("libxiaojianbang.so", "_Z9MD5UpdateP7MD5_CTXPhj");
var strAddr = Module.findBaseAddress("libxiaojianbang.so").add(0x3CFD);
Interceptor.attach(MD5Update, {
    onEnter: function (args) {
        if(args[1].readCString() == "xiaojianbang"){
            args[1] = strAddr;
            console.log(hexdump(args[1]));
            args[2] = ptr(strAddr.readCString().length);
            console.log(args[2].toInt32());
        }
    }, onLeave: function (retval) {
    }
});
/*
7ae6787cfd  63 6f 6d 2f 78 69 61 6f 6a 69 61 6e 62 61 6e 67  com/xiaojianbang
7ae6787d0d  2f 6e 64 6b 2f 4e 61 74 69 76 65 48 65 6c 70 65  /ndk/NativeHelpe
7ae6787d1d  72 00 65 6e 63 6f 64 65 00 28 29 4c 6a 61 76 61  r.encode.()Ljava
33
//logcat中的输出结果
//CMD5 md5Result: f6190c61b22ec8efe63fade2c47d8a49
*/


//stringToBytes函数的定义，参考上一小节
var MD5Update = Module.findExportByName("libxiaojianbang.so", "_Z9MD5UpdateP7MD5_CTXPhj");
Interceptor.attach(MD5Update, {
    onEnter: function (args) {
        this.args0 = args[0];
        this.args1 = args[1];
    }, onLeave: function (retval) {
        if(this.args1.readCString() == "xiaojianbang"){
            let newStr = "jianbang";
            this.args0.add(24).writeByteArray(stringToBytes(newStr));
            console.log(hexdump(this.args0.writeInt(newStr.length * 8)));
        }
    }
});
/*
7fda079f08  40 00 00 00 00 00 00 00 01 23 45 67 89 ab cd ef  @........#Eg....
7fda079f18  fe dc ba 98 76 54 32 10 6a 69 61 6e 62 61 6e 67  ....vT2.jianbang
7fda079f28  62 61 6e 67 00 00 00 00 d0 a0 07 da 7f 00 00 00  bang............
7fda079f38  78 b2 2f 3e 7b 00 00 00 4c b2 2f 3e 7b 00 00 00  x./>{...L./>{...
7fda079f48  00 00 00 00 00 00 00 00 06 00 00 00 00 00 00 00  ................
7fda079f58  63 01 63 01 00 00 00 00 10 00 00 00 10 00 00 00  c.c.............
//logcat中的输出结果
//CMD5 md5Result: ea54ded1bd8a592dd826fb919687f13f
*/


var MD5Update = Module.findExportByName("libxiaojianbang.so", "_Z9MD5UpdateP7MD5_CTXPhj");
var newStr = "xiaojianbang&liruyi";
var newStrAddr = Memory.allocUtf8String(newStr);
Interceptor.attach(MD5Update, {
    onEnter: function (args) {
        if(args[1].readCString() == "xiaojianbang"){
            args[1] = newStrAddr;
            console.log(hexdump(args[1]));
            args[2] = ptr(newStr.length);
            console.log(args[2].toInt32());
        }
    }, onLeave: function (retval) {
    }
});
/*
7b34a80060  78 69 61 6f 6a 69 61 6e 62 61 6e 67 26 6c 69 72  xiaojianbang&lir
7b34a80070  75 79 69 00 00 00 00 00 23 00 00 00 00 00 00 00  uyi.....#.......
19
//logcat中的输出结果
//CMD5 md5Result: 8f1968f06a1e62bb3d83119352cc26cc
*/