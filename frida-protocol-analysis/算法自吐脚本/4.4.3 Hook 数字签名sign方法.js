 signature.sign.overload('[B', 'int', 'int').implementation = function () {
        console.log("Signature.sign('[B', 'int', 'int') is called!");
        return this.sign.apply(this, arguments);
    }
 signature.sign.overload().implementation = function () {
        console.log("Signature.sign() is called!");
        var result = this.sign();
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " sign result";
        toHex(tag, result);
        toBase64(tag, result);
        console.log("===================================");
        return result;
    }