// 主动调用静态方法
// function test(){
//     Java.perform(function(){
//         var money=Java.use("com.xiaojianbang.hook.Money");
//         money.setFlag("xiaojianbang1");
//         console.log(money.getFlag());
//     })
// };
// test();

// 自己new然后调用实例
// function test(){
//     Java.perform(function(){
//         var money=Java.use("com.xiaojianbang.hook.Money");
//         var moneyobj=money.$new("美元",1000);
//         console.log(moneyobj.getInfo());
//     })
// };
// test();

// // 获取已有对象
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