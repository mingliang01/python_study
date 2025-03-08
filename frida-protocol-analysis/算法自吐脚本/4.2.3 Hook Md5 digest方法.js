 messageDigest.digest.implementation = function () {}

  messageDigest.digest.overload().implementation = function () {
        console.log("MessageDigest.digest() is called!");
        var result = this.digest();
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " digest result";
        toHex(tag, result);
        toBase64(tag, result);
       console.log("================================");
        return result;
    }

 messageDigest.digest.overload('[B').implementation = function (data) {
        console.log("MessageDigest.digest('[B') is called!");
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " digest data";
        toUtf8(tag, data);
        toHex(tag, data);
        toBase64(tag, data);
        var result = this.digest(data);
        var tags = algorithm + " digest result";
        toHex(tags, result);
        toBase64(tags, result);
        console.log(("================================");
        return result;
    }

  messageDigest.digest.overload('[B', 'int', 'int').implementation = 
function (data, start, length) {
        console.log("MessageDigest.digest('[B', 'int', 'int') is called!");
        var algorithm = this.getAlgorithm();
        var tag = algorithm + " digest data";
        toUtf8(tag, data);
        toHex(tag, data);
        toBase64(tag, data);
        var result = this.digest(data, start, length);
        var tags = algorithm + " digest result";
        toHex(tags, result);
        toBase64(tags, result);
        console.log("============================", start, length);
        return result;
    }