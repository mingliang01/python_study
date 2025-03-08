var pthread_create_addr = Module.findExportByName("libc.so", "pthread_create");
Interceptor.attach(pthread_create_addr,{
    onEnter:function(args){
        console.log(args[0], args[1], args[2], args[3]);
        var Module = Process.findModuleByAddress(args[2]);
        if(Module != null) console.log(Module.name, args[2].sub(Module.base));
    },onLeave:function(retval){
    }
});
/*
0x7fc2d0bc18 0x7fc2d0bc20 0x7e21962f90 0x7e259783c0
libutils.so 0x12f90
......
0x7da0bfe9a0 0x0 0x7da097b8dc 0x7e259cbe00
libart.so 0x34b8dc
......
0x7fc2d09378 0x0 0x7d91152d8c 0x0
libxiaojianbang.so 0x1d8c
*/