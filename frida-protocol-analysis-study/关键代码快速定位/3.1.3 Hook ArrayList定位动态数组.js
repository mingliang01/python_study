var arrayList = Java.use("java.util.ArrayList");
arrayList.add.overload('java.lang.Object').implementation = function (a) {
    // 不判断类型会挂掉
    if(a.$className == "java.lang.String"){
    console.log("ArrayList.add: ", a);
}
    return this.add(a);
}
arrayList.add.overload('int', 'java.lang.Object').implementation = function (a, b) {

    console.log("ArrayList.add: ", a, b);

    return this.add(a, b);
}

var arrayList = Java.use("java.util.ArrayList");
arrayList.add.overload('java.lang.Object').implementation = function (a) {
    if(a.$className == "java.lang.String" && && a.equals("username=13866668888")){
        showStacks();
        console.log("ArrayList.add: ", a);
    }
    return this.add(a);
}