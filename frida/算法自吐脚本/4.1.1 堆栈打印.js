Java.perform(function(){
    function showStack(){
        var stack=Java.use("android.util.Log").getStackTraceString(
            Java.use("java.lang.Throwable").$new());
            console.log(stack);
    };
})