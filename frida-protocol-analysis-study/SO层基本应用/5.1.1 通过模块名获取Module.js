var module = Process.findModuleByName("libxiaojianbang.so");
console.log(JSON.stringify(module));
//Process.getModuleByName("libxiaojianbang.so");
//{"name":"libxiaojianbang.so","base":"0x7ad1ce6000","size":28672,"path":"/data/app/com.xiaojianbang.app-r_cD2g_EAJo-3V4FJEttXQ==/lib/arm64/libxiaojianbang.so"}

function findModuleByName(name: string): Module | null;
function getModuleByName(name: string): Module;

var module = Process.findModuleByName("libxiaojianbang.so");
if(module != null){
	//do someting ... 
}