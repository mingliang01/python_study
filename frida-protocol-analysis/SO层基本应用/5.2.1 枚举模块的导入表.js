enumerateImports(): ModuleImportDetails[];

var imports = Process.getModuleByName("libxiaojianbang.so").enumerateImports();
console.log(JSON.stringify(imports[0]));
//{"type":"function","name":"__cxa_atexit","module":"/apex/com.android.runtime/lib/bionic/libc.so","address":"0xedf050b9"}

var improts = Process.findModuleByName("libxiaojianbang.so").enumerateImports();
var sprintf_addr = null;
for(let i = 0; i < improts.length; i++){
    let _import = improts[i];
    if(_import.name.indexOf("sprintf") != -1){
        sprintf_addr = _import.address;
        break;
    }
}
console.log("sprintf_addr: ", sprintf_addr);
//sprintf_addr:  0x7bc0debaa0