// function test(){
//         Java.perform(function(){
//                 var walletils=Java.use("com.xiaojianbang.hook.Wallet");
// //         console.log(Utils.getCalc.overloads.length);
//                 walletils.deposit.implementation=function(a){
//                     console.log("money.$init param:", a.getInfo());
//         // 没加参数会报错
//                     return this.deposit();
//                 };
//                 // money.setFlag.implementation=function(a){
//                 //                 console.log("money.setFlag param:",a);
//                 //                 return this.setFlag(a);
//                 //             };
//         })
//     };
//     test();


function test(){
    Java.perform(function(){
        var walletils=Java.use("com.xiaojianbang.hook.Wallet");
                var Money=Java.use("com.xiaojianbang.hook.Money");
                walletils.deposit.implementation=function(a){
                console.log("money.$init param:",a.getInfo());
                return this.deposit(Money.$new("美元",1000));
            };
    })
};
test();

       