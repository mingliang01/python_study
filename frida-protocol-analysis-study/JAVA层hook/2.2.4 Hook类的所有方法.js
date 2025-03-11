function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        var methods=Utils.class.getDeclaredMethods();
        for(let k=0;k<methods.length;k++){
    // 注意这里用let而不是var，不然会报错。因为进了循环以后，var修饰的变量，作用域会变。
            let methodName=methods[k].getName();
            var overloadArr=Utils[methods[k].getName()].overloads;
            console.log("fun:",methodName);
            for(var i=0;i<overloadArr.length;i++){
                overloadArr[i].implementation=function(){
                    var params="";
                    for(var j=0;j<arguments.length;j++){
                        params+=arguments[j]+" ";
                    };
                    console.log("utils."+methodName+" is called! params is:",params);
                    return this[methodName].apply(this,arguments);
                }
            }
        };
});
};
test();