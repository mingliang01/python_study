declare class NativePointer {
    // NativePointer构造函数，通过new NativePointer(...) 或者ptr(...) 来使用
constructor(v: string | number | UInt64 | Int64 | NativePointerValue);
// 判断是否空指针
isNull(): boolean;
// 创建新指针，值等于this + v
add(v: NativePointerValue | UInt64 | Int64 | number | string): NativePointer;
// 创建新指针，值等于this - v
    sub(v: NativePointerValue | UInt64 | Int64 | number | string): NativePointer;
// 更多用于指针计算的方法，请自行查阅相关文档和源码
......	
// 比较两者是否相等
equals(v: NativePointerValue | UInt64 | Int64 | number | string): boolean;
// 比较两者大小，返回1、-1、0
compare(v: NativePointerValue | UInt64 | Int64 | number | string): number;
// 指针转32位有符号数
toInt32(): number;
// 指针转32位无符号数
toUInt32(): number;
// NativePointer类型转string类型，参数可以指定进制，默认16进制
toString(radix?: number): string;
    toJSON(): string;

// 读取4/8字节数据，转指针
readPointer(): NativePointer;
// 读8bit数据，也就是1字节数据，转有符号数
readS8(): number;
// 读8bit数据，也就是1字节数据，转无符号数
readU8(): number;
// 更多读取数据转数值的方法依此类推
......	
// 读指定字节数内存数据，返回ArrayBuffer 
readByteArray(length: number): ArrayBuffer | null;
// 读指定长度的C语言char*字符串，或者读取到遇字节0为止
readCString(size?: number): string | null;
// 读指定长度的Utf8字符串（可以是中文），或者读取到遇字节0为止
readUtf8String(size?: number): string | null;
readUtf16String(length?: number): string | null;
// 仅限Windows平台使用
    readAnsiString(size?: number): string | null;

// 将4/8字节指针写入内存，后续基本都是与读取类似的操作，不再赘述
writePointer(value: NativePointerValue): NativePointer;
    writeS8(value: number | Int64): NativePointer;
    writeU8(value: number | UInt64): NativePointer;
......
    writeByteArray(value: ArrayBuffer | number[]): NativePointer;
    writeUtf8String(value: string): NativePointer;
writeUtf16String(value: string): NativePointer;
    writeAnsiString(value: string): NativePointer;
}