// 直接输出flag，是获取不到flag的值的
function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        console.log(money.flag);
    })
};
test();

//使用value访问静态字段flag的值，并可以修改flag的值
  var money=Java.use("com.xiaojianbang.hook.Money");
        console.log(money.flag.value);
        money.flag.value="修改后的结果";
        console.log(money.flag.value);

//自己new一个实例，再获取和修改成员变量
        var money=Java.use("com.xiaojianbang.hook.Money");
        var moneyobj=money.$new("美元",1000);
        console.log(moneyobj.currency.value);
        moneyobj.currency.value="修改后的currency";
        console.log(moneyobj.currency.value);

//遍历所有实例，获取和修改成员变量

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
// 如果有函数和变量重名，需要使用obj._accountName.value来访问