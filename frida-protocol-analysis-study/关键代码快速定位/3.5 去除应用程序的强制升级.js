Java.perform(function () {
    var toast = Java.use("android.widget.Toast");
    toast.show.implementation = function () {
        showStacks();
        console.log("Toast.show");
        return this.show();
    }
});

objection -g com.xxxx explore --startup-command "android hooking watch class 'com.xxxx.util.UpgraderUtil'"

var upgraderUtil = Java.use("com.xxxx.util.UpgraderUtil");
upgraderUtil.a.overload('android.content.Context').implementation = function (context) {
    showStacks();
    var result = this.a(context);
    console.log("versionCode: ", result);
    return 605;
}