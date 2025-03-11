function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        money.setFlag.implementation=function(a){
            console.log("money.setFlag param:",a);
            return this.setFlag(a);
        };
        money.getInfo.implementation=function(){
            var result=this.getInfo();
            console.log("money.getInfo:",result);
            return result;
        };
    })
};
test();