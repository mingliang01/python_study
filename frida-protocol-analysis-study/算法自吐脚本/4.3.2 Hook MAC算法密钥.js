    var mac = Java.use("javax.crypto.Mac");mac.init.implementation = function () {}

 var mac = Java.use("javax.crypto.Mac");
    mac.init.overload('java.security.Key', 
'java.security.spec.AlgorithmParameterSpec').implementation = function (key, 
AlgorithmParameterSpec) {
        console.log("Mac.init('java.security.Key', 'java.security.spec.AlgorithmParameterSpec') is called!");
        return this.init(key, AlgorithmParameterSpec);
    }
    mac.init.overload('java.security.Key').implementation = function (key) {
        console.log("Mac.init('java.security.Key') is called!");
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " init Key";
        var keyBytes = key.getEncoded();
        toUtf8(tag, keyBytes);
        toHex(tag, keyBytes);
        toBase64(tag, keyBytes);
        console.log("=======================================");
        return this.init(key);
    }