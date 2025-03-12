enumerateExports(): ModuleExportDetails[];

var exports = Process.getModuleByName("libxiaojianbang.so").enumerateExports();
console.log(JSON.stringify(exports[0]));
//{"type":"function","name":"JNI_OnLoad","address":"0xc68995f1"}

var exports = Process.findModuleByName("libxiaojianbang.so").enumerateExports();
var MD5Final_addr = null;
for(let i = 0; i < exports.length; i++){
    let _export = exports[i];
    if(_export.name.indexOf("_Z8MD5FinalP7MD5_CTXPh") != -1){
        MD5Final_addr = _export.address;
        break;
    }
}
console.log("MD5Final_addr: ", MD5Final_addr);
//MD5Final_addr:  0x7ad0beb988d