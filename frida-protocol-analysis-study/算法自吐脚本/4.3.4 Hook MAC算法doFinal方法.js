mac.doFinal.overload().implementation = function () {
        console.log("Mac.doFinal() is called!");
        var result = this.doFinal();
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " doFinal result";
        toHex(tag, result);
        toBase64(tag, result);
        console.log("=======================================");
        return result;
    }