
        Java.perform(function(){
            var josnRequest=Java.use("com.dodonew.online.http.JsonRequest");
            josnRequest.addRequestMap.overload('java.util.Map', 'int').implementation=function(a,b){
                    console.log("jsonRequest.addRequestMap is called!");
                    return this.addRequestMap(a,b);
            }
            
        var encodeDesMap=Java.use("com.dodonew.online.http.RequestUtil");
            encodeDesMap.encodeDesMap.overload
        ('java.lang.String', 'java.lang.String', 'java.lang.String').implementation=function(a,b,c){
                console.log("encodeDesMap.encodeDesMap is called!");
                console.log("data:",a);
                console.log("deskey:",b);
                console.log("desiv:",c);
        console.log("resul:",this.encodeDesMap(a,b,c))
                return this.encodeDesMap(a,b,c);
            };
    })
