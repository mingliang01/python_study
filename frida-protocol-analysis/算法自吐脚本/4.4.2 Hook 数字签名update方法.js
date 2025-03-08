   var signature = Java.use("java.security.Signature");
    signature.update.overload('byte').implementation = function (data) {
        console.log("Signature.update('byte') is called!");
        return this.update(data);
    }
    signature.update.overload('java.nio.ByteBuffer').implementation = function (data) {
        console.log("Signature.update('java.nio.ByteBuffer') is called!");
        return this.update(data);
    }
    signature.update.overload('[B', 'int', 'int').implementation = function (data, start, length) 
{
        console.log("Signature.update('[B', 'int', 'int') is called!");
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " update data";
        toUtf8(tag, data);
        toHex(tag, data);
        toBase64(tag, data);
        console.log("=================================", start, length);
        return this.update(data, start, length);
    }