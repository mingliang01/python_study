var toast = Java.use("android.widget.Toast");
toast.show.implementation = function () {
    showStacks();
    console.log("Toast.show");
    return this.show();
}