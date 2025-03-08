function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        console.log(money.flag);
    })
};
test();


  var money=Java.use("com.xiaojianbang.hook.Money");
        console.log(money.flag.value);
        money.flag.value="修改后的结果";
        console.log(money.flag.value);


        var money=Java.use("com.xiaojianbang.hook.Money");
        var moneyobj=money.$new("美元",1000);
        console.log(moneyobj.currency.value);
        moneyobj.currency.value="修改后的currency";
        console.log(moneyobj.currency.value);


        var money=Java.use("com.xiaojianbang.hook.Money");
        Java.choose("com.xiaojianbang.hook.Money",{
            onMatch:function(obj){
                console.log("Java onMatch:",obj.currency.value);
            },
            onComplete:function(){
            }
        })

        Java.choose("com.xiaojianbang.hook.BankCard",{
            onMatch:function(obj){
                console.log("Java onMatch:",obj.accountName.value);
            },
            onComplete:function(){
            }
        })