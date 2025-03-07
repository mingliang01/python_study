function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        money.$init.implementation=function(a,b){
            console.log("money.$init param:",a,b);
            return this.$init("美元",200);
        }
    })
};
test();