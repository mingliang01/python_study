var base64 = Java.use("android.util.Base64");
base64.encodeToString.overload('[B', 'int').implementation = function (a, b) {
    showStacks();
    var result = this.encodeToString(a, b);
    console.log("Base64.encodeToString: ", JSON.stringify(a), result)
    return result;
}