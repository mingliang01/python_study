var textUtils = Java.use("android.text.TextUtils");
textUtils.isEmpty.implementation = function (a) {
    console.log("TextUtils.isEmpty: ", a);
    return this.isEmpty(a);
}

var textUtils = Java.use("android.text.TextUtils");
textUtils.isEmpty.implementation = function (a) {
    showStacks();
    console.log("TextUtils.isEmpty: ", a);
    return this.isEmpty(a);
}