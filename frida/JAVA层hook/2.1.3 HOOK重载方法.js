function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        Utils.getCalc.implementation=function(){
            return this.getCalc();
        }
    })
};
test();

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