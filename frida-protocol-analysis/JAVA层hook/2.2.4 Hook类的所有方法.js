function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        var methods=Utils.class.getDeclaredMethods();
        for(let k=0;k<methods.length;k++){
            var methodName=methods[k].getName();
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