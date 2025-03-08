   var Wallet$InnerSturcture=Java.use("com.xiaojianbang.hook.Wallet$InnerStructure");
        console.log(Wallet$InnerSturcture);

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

        var money=Java.use("com.xiaojianbang.app.MainActivity$1");
        money.getInfo.implementation=function(){
            var result=this.getInfo();
            console.log(result);
            return result;
        }