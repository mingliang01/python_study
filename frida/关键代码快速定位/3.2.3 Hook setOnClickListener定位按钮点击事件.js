Java.perform(function () {
    var btn_login_id = Java.use("com.dodonew.online.R$id").btn_login.value;
    console.log("btn_login_id", btn_login_id);
    var view = Java.use("android.view.View");
    view.setOnClickListener.implementation = function (a) {
        if(this.getId() == btn_login_id){
            showStacks();
            console.log("view.id: " + this.getId());
            console.log("view.setOnClickListener is called");
        }
        return this.setOnClickListener(a);
    }
});