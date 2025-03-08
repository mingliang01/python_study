    var messageDigest = Java.use("java.security.MessageDigest");
    messageDigest.update.implementation = function (data) {}

 var messageDigest = Java.use("java.security.MessageDigest");
    messageDigest.update.overload('byte').implementation = function (data) {
        console.log("MessageDigest.update('byte') is called!");
        return this.update(data);
    }
    messageDigest.update.overload('java.nio.ByteBuffer').implementation = function (data) {
        console.log("MessageDigest.update('java.nio.ByteBuffer') is called!");
        return this.update(data);
    }
    messageDigest.update.overload('[B').implementation = function (data) {
        console.log("MessageDigest.update('[B') is called!");
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " update data";
        toUtf8(tag, data);
        toHex(tag, data);
        toBase64(tag, data);
        console.log("=================================================");
        return this.update(data);
    }
    messageDigest.update.overload('[B', 'int', 'int').implementation = 
function (data, start, length) {
        console.log("MessageDigest.update('[B', 'int', 'int') is called!");
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " update data";
        toUtf8(tag, data);
        toHex(tag, data);
        toBase64(tag, data);
        console.log("=========================================", start, length);
        return this.update(data, start, length);
    }