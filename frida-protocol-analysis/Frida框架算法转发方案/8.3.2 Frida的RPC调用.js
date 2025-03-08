function test(data){
    	var result="";
    	Java.perform(function (){
        	result=Java.use('com.dodonew.online.util.Utils').md5(data);
    	});
    	return result;
		};
	var result=test('123456');
	console.log("result:",result);


rpc.exports={
    	rpcfunc:test
	};

result=script.exports.rpcfunc("123456")