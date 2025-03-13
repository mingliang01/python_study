var soAddr = Module.findBaseAddress("libxiaojianbang.so");
hookAddr(soAddr.add(0x1ACC), 5); 	// Java_com_xiaojianbang_ndk_NativeHelper_add
hookAddr(soAddr.add(0x22A0), 3); 	// MD5Update

function hookAddr(funcAddr, paramsNum){
    var module = Process.findModuleByAddress(funcAddr);
    Interceptor.attach(funcAddr, {
        onEnter: function(args){
            this.logs = [];
            this.params = [];
            this.logs.push("call " + module.name + "!" + ptr(funcAddr).sub(module.base) + "\n");
            for(let i = 0; i < paramsNum; i++){
                this.params.push(args[i]);
                this.logs.push("this.args" + i + " onEnter: " + printAddr(args[i]));
            }
        }, onLeave: function(retval){
            for(let i = 0; i < paramsNum; i++){
                this.logs.push("this.args" + i + " onLeave: " + printAddr(this.params[i]));
            }
            this.logs.push("retval onLeave: " + printAddr(retval) + "\n");
            console.log(this.logs);
        }
    });
}


function printAddr(addr){
    var module = Process.findRangeByAddress(addr);
    if(module != null) return hexdump(addr) + "\n";
    return ptr(addr) + "\n";
}

call libxiaojianbang.so!0x1acc
......
,this.args2 onEnter: 0x5
,this.args3 onEnter: 0x6
,this.args4 onEnter: 0x7
......
,this.args2 onLeave: 0x5
,this.args3 onLeave: 0x6
,this.args4 onLeave: 0x7
,retval onLeave: 0x12

call libxiaojianbang.so!0x22a0
......
,this.args1 onEnter: 
7590c56390  78 69 61 6f 6a 69 61 6e 62 61 6e 67 00 00 c0 41  xiaojianbang...A
,this.args2 onEnter: 0xc
......
,this.args1 onLeave: 
7590c56390  78 69 61 6f 6a 69 61 6e 62 61 6e 67 00 00 c0 41  xiaojianbang...A
,this.args2 onLeave: 0xc
,retval onLeave: 
7fc209c890  78 69 61 6f 6a 69 61 6e 62 61 6e 67 76 00 00 00  xiaojianbangv...