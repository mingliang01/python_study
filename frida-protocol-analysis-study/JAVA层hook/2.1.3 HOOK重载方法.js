//第一步：先不管重载声明直接HOOK，通过报错再修改HOOK代码
// function test(){
//     Java.perform(function(){
//         var Utils=Java.use("com.xiaojianbang.hook.Utils");
//         Utils.getCalc.implementation=function(){
//             return this.getCalc();
//         }
//     })
// };
// test();

//第二步：根据报错信息，修改HOOK代码为重载声明方式
function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        Utils.getCalc.overload('int','int').implementation=function(a,b){
            console.log("Utils.getCalc params:",a,b);
            return this.getCalc(a,b);
        }
    })
};
test();
//第三步：根据报错信息，继续添加重载声明
/*
    Utils.getCalc.overload('int','int').implementation=function(a,b){
            console.log("Utils.getCalc params:",a,b);
            return this.getCalc(a,b);
        };
        Utils.getCalc.overload('int', 'int', 'int').implementation=function(a,b,c){
            console.log("Utils.getCalc params:",a,b,c);
            return this.getCalc(a,b,c);
        };
        Utils.getCalc.overload('int', 'int', 'int', 'int').implementation=function(a,b,c,d){
            console.log("Utils.getCalc params:",a,b,c,d);
            return this.getCalc(a,b,c,d);
        };
*/