// 访问匿名内部类的方法

   var Wallet$InnerSturcture=Java.use("com.xiaojianbang.hook.Wallet$InnerStructure");
        console.log(Wallet$InnerSturcture);

// 访问内部类中的bankCardsList字段
        Java.choose("com.xiaojianbang.hook.Wallet$InnerStructure",{
            onMatch:function(obj){
                console.log("Java Wallet$InnerSturcture:",obj.bankCardsList.value);
            },
            onComplete:function(){
            }
        })

logOutPut(new Money("欧元", 		ItemTouchHelper.Callback.DEFAULT_DRAG_ANIMATION_DURATION) {
            @Override // com.xiaojianbang.hook.Money
            public String getInfo() {
                return getCurrency() + " " + getAmount() + " 这是匿名内部类";
            }
        }.getInfo());

        // 这样是hook不到匿名类的
function test(){
    Java.perform(function(){
        var money=Java.use("com.xiaojianbang.hook.Money");
        money.getInfo.implementation=function(){
            var result=this.getInfo();
            console.log(result);
            return result;
        }
    })
};
test();

// 用jed反汇编，可以看到对应代码的smali语法
        var money=Java.use("com.xiaojianbang.app.MainActivity$1");
        money.getInfo.implementation=function(){
            var result=this.getInfo();
            console.log(result);
            return result;
        }