declare class Module {
    name: string;			//模块名
    base: NativePointer;	//模块基址
    size: number;			//模块大小
    path: string;			//模块所在路径
    enumerateImports(): ModuleImportDetails[];	//枚举导入表
    enumerateExports(): ModuleExportDetails[];	//枚举导出表
    enumerateSymbols(): ModuleSymbolDetails[];	//枚举符号表
    findExportByName(exportName: string): NativePointer | null;	//获取导出函数地址
    getExportByName(exportName: string): NativePointer;		//获取导出函数地址
    static load(name: string): Module;							//加载指定模块
    static findBaseAddress(name: string): NativePointer | null;		//获取模块基址
    static getBaseAddress(name: string): NativePointer;			//获取模块基址
    //获取导出函数地址
static findExportByName(moduleName: string | null, exportName: string): NativePointer | null;	
//获取导出函数地址
    static getExportByName(moduleName: string | null, exportName: string): NativePointer;
}