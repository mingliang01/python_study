function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        console.log(Utils.getCalc.overloads);
        console.log(Utils.getCalc.overloads.length);
    })
};
test();

function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        var overloadArr=Utils.getCalc.overloads;
        for(var i=0;i<overloadArr.length;i++){
            overloadArr[i].implementation=function(){
                var params="";
                for(var j=0;j<arguments.length;j++){
                    params+=arguments[j]+" ";
                };
                console.log("utils.getCalc is called! params is:",params);
                if (arguments.length==2){
                    return this.getCalc(arguments[0],arguments[1]);
                }else if (arguments.length==3){
                    return this.getCalc(arguments[0],arguments[1],arguments[2]);
                }else if(arguments.length==4){
                    return this.getCalc(arguments[0],arguments[1],arguments[2],arguments[3]);
                };
            }
        }
    })
};
test();

function test(){
    Java.perform(function(){
        var Utils=Java.use("com.xiaojianbang.hook.Utils");
        var overloadArr=Utils.getCalc.overloads;
        for(var i=0;i<overloadArr.length;i++){
            overloadArr[i].implementation=function(){
                var params="";
                for(var j=0;j<arguments.length;j++){
                    params+=arguments[j]+" ";
                };
                console.log("utils.getCalc is called! params is:",params);
                return this.getCalc.apply(this,arguments);
            }
        }
    })
};
test();

        Utils.getCalc.overload('int','int').implementation=function(a,b){
            console.log("Utils.getCalc params:",a,b);
            return this.getCalc(a,b);
        };

     Utils.getCalc.overload('int','int').implementation=function(a,b){
            console.log("Utils.getCalc params:",a,b);
            return Utils.getCalc(a,b);
        };