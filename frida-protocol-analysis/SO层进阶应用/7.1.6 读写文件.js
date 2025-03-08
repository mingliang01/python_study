var fopenAddr = Module.findExportByName("libc.so", "fopen");
var fputsAddr = Module.findExportByName("libc.so", "fputs");
var fcloseAddr = Module.findExportByName("libc.so", "fclose");

// FILE *fopen(const char *filename, const char *mode)
// int fputs(const char *str, FILE *stream)
// int fclose(FILE *stream)
var fopen = new NativeFunction(fopenAddr, "pointer", ["pointer", "pointer"]);
var fputs = new NativeFunction(fputsAddr, "int", ["pointer", "pointer"]);
var fclose = new NativeFunction(fcloseAddr, "int", ["pointer"]);

var fileName = Memory.allocUtf8String("/data/data/com.xiaojianbang.app/xiaojianbang.txt");
var openMode = Memory.allocUtf8String("w");
var buffer = Memory.allocUtf8String("QQ24358757");

var file = fopen(filename, open_mode);
fputs(buffer, file);
fclose(file);

var fopenAddr = Module.findExportByName("libc.so", "fopen");
var fgetsAddr = Module.findExportByName("libc.so", "fgets");
var fcloseAddr = Module.findExportByName("libc.so", "fclose");

// char *fgets(char *str, int n, FILE *stream)
var fopen = new NativeFunction(fopenAddr, "pointer", ["pointer", "pointer"]);
var fgets = new NativeFunction(fgetsAddr, "pointer", ["pointer", "int", "pointer"]);
var fclose = new NativeFunction(fcloseAddr, "int", ["pointer"]);

var fileName = Memory.allocUtf8String("/data/data/com.xiaojianbang.app/xiaojianbang.txt");
var openMode = Memory.allocUtf8String("r");
var buffer = Memory.alloc(60);

var file = fopen(fileName, openMode);
var data = fgets(buffer, 60, file);
console.log(data.readCString());
fclose(file);
// QQ24358757