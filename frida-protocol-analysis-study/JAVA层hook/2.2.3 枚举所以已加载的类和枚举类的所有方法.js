// 枚举所有加载的类
function test(){
    Java.perform(function(){
        console.log(Java.enumerateLoadedClassesSync().join('\n'));
    })
};
test();

// 枚举某个类的所有方法
function test(){
    Java.perform(function(){
        var wallet=Java.use("com.xiaojianbang.hook.Wallet");
        var methods=wallet.class.getDeclaredMethods();
        for(var i=0;i<methods.length;i++){
            console.log(methods[i].getName());
        };
});
};
test();

//枚举某个类的所有构造器
        var constructor=wallet.class.getDeclaredConstructors();
        for(var j=0;j<constructor.length;j++){
            console.log(constructor[j].getName());
        }