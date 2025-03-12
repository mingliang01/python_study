var soAddr = Module.findBaseAddress("libtre.so");
var input = soAddr.add(0x15BE + 1);
var result = soAddr.add(0x14C8 + 1);
Interceptor.attach(input, {
    onEnter: function (args) {
        console.log("input onEnter args[1]: ", args[1].readCString())
        console.log("input onEnter args[2]: ", args[2].toInt32());
    }, onLeave: function (retval) {
    }
});
Interceptor.attach(result, {
    onEnter: function (args) {
        this.args1 = args[1];
    }, onLeave: function (retval) {
        console.log("result onLeave this.args1: ", hexdump(this.args1));
    }
});
/*
input onEnter args[1]:  YXBwX3Zlcj0xMDAmbm9uY2 ...... lhK2B3OWc=
input onEnter args[2]:  828
result onLeave this.args1:
c50f2574  67 67 6a 07 7d 37 f4 39 eb d5 62 49 9c 7c 2f 30  ggj.}7.9..bI.|/0
c50f2584  c3 54 7d cd 07 6a 67 67 39 f4 37 7d 49 62 d5 eb  .T}..jgg9.7}Ib..
*/


var soAddr = Module.findBaseAddress("libtre.so");
var base64 = soAddr.add(0x13B4 + 1);
Interceptor.attach(base64, {
    onEnter: function (args) {
        console.log("base64 onEnter args[0]: ", args[0].readCString())
        this.args1 = args[1];
        console.log("base64 onEnter args[2]: ", args[2].toInt32());
    }, onLeave: function (retval) {
        console.log("base64 onLeave this.args1: ", this.args1.readCString());
    }
});
/*
base64 onEnter args[0]:  app_ver=100&nonce=7tznu51634898812677&timestamp=1634898812&tzrd=BwzXzSGFyiPstMIVuzTZb7LzTZzbXRJOFzpb......ZFB26p7dBE4=b2qKgtaW4,9z9D`Fmst?K5JZbLYOY]NP6ssGf2U~;zk9oCNgoytV!}wW7ia+`w9g
base64 onEnter args[2]:  620
base64 onLeave this.args1:  YXBwX3Zlcj0xMDAmbm9uY2 ...... lhK2B3OWc=
*/