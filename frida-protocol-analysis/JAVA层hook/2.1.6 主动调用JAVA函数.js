function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        money.setFlag("xiaojianbang");
    })
};
test();

function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        var moneyobj=money.$new("美元",1000);
        console.log(moneyobj.getInfo());
    })
};
test();

function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        Java.choose("com.xiaojianbang.hook.Money",{
            onMatch:function(obj){
                console.log(obj.getInfo());
            },
            onComplete:function(){
                console.log("内存中的Money对象搜索完毕！")
            }
        })
    })};
test();