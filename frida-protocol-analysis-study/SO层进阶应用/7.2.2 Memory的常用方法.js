declare namespace Memory {
// 异步，在内存中搜索指定数据
// 可以搜索指定指令，然后patch。可以搜索指定文件头，然后dump等等
    function scan(address: NativePointerValue, size: number | UInt64, pattern: string, callbacks: MemoryScanCallbacks): void;
// scan的同步版本
    function scanSync(address: NativePointerValue, size: number | UInt64, pattern: string): MemoryScanMatch[];
// 在frida私有堆上分配指定大小的内存，返回首地址
    function alloc(size: number | UInt64, options?: MemoryAllocOptions): NativePointer;
// 在frida私有堆上，将str作为UTF-8字符串进行分配、编码和写出
//（可以是中文）
    function allocUtf8String(str: string): NativePointer;
    function allocUtf16String(str: string): NativePointer;
// 仅限Windows平台使用
    function allocAnsiString(str: string): NativePointer;
// 内存拷贝，参数为目标地址、源地址、要复制的字节数
    function copy(dst: NativePointerValue, src: NativePointerValue, n: number | UInt64): void;
// 先分配内存，然后进行拷贝
    function dup(address: NativePointerValue, size: number | UInt64): NativePointer;
// 修改内存页权限，之前小节中有介绍，这里不再赘述
    function protect(address: NativePointerValue, size: number | UInt64, protection: PageProtection): boolean;
// 可以用来patch指令，本书后续内容中单独介绍
    function patchCode(address: NativePointerValue, size: number | UInt64, apply: MemoryPatchApplyCallback): void;
}