var str = Java.use("java.lang.String");
str.getBytes.overload().implementation = function () {
    showStacks();
    var result = this.getBytes();
    var newStr = str.$new(result);
    console.log("str.getBytes: ", newStr);
    return result;
}
str.getBytes.overload('java.lang.String').implementation = function (a) {
    showStacks();
    var result = this.getBytes(a);
    var newStr = str.$new(result, a);
    console.log("str.getBytes: ", newStr);
    return result;
}