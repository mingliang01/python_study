        var walletils=Java.use("com.xiaojianbang.hook.Wallet");
        walletils.deposit.implementaton=function(a){
            console.log("money.$init param:",a.getInfo());
            return this.deposit();

        var walletils=Java.use("com.xiaojianbang.hook.Wallet");
        var Money=Java.use("com.xiaojianbang.hook.Money");
        walletils.deposit.implementaton=function(a){
            console.log("money.$init param:",a.getInfo());
            return this.deposit(Money.$new("美元",1000));