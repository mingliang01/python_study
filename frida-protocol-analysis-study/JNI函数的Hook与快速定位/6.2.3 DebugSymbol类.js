var debsym = DebugSymbol.fromName("strcat");
console.log("address: ", debsym.address);
console.log("name: ", debsym.name);
console.log("moduleName: ", debsym.moduleName);
console.log("fileName: ", debsym.fileName);
console.log("lineNumber: ", debsym.lineNumber);
console.log("toString: ", debsym.toString());

console.log("getFunctionByName: ", DebugSymbol.getFunctionByName("strcat"));
console.log("findFunctionsNamed: ", DebugSymbol.findFunctionsNamed("JNI_OnLoad"));
console.log("findFunctionsMatching: ", DebugSymbol.findFunctionsMatching("JNI_OnLoad"));
/*
address:  0x7a4d20222c
name:  strcat
moduleName:  libc.so
fileName:
lineNumber:  0
toString:  0x7a4d20222c libc.so!strcat

getFunctionByName:  0x7a4d20222c
findFunctionsNamed:  0x79c20cf89c,0x79c206d35c,0x79c08b1898,0x79b6419ab8,0x79b6377014,0x79b62e7070,0x79b27cd1f8,0x796f4eef0c,0x7960434d28
findFunctionsMatching:  0x7960434d28,0x796f4eef0c,0x79b27cd1f8,0x79b62e7070,0x79b6377014,0x79b6419ab8,0x79c08b1898,0x79c206d35c,0x79c20cf89c
*/