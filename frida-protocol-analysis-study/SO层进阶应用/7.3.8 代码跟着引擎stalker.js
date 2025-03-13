var md5Addr = Module.getExportByName("libxiaojianbang.so", "Java_com_xiaojianbang_ndk_NativeHelper_md5");
Interceptor.attach(md5Addr, {
    onEnter: function () {
        this.tid = Process.getCurrentThreadId();
        Stalker.follow(this.tid, {
            events: {
                call: true,
            },
            onReceive(events) {
                var _events = Stalker.parse(events);
                for (var i = 0; i < _events.length; i++) {
                    console.log(_events[i]);
                }
            },
        });
    }, onLeave: function () {
        Stalker.unfollow(this.tid);
    }
});
/*
call,0x7590e77054,0x7590d63f60,0
call,0x7590e035a8,0x7590e0b24c,0
......
*/


declare namespace Stalker {
function follow(threadId?: ThreadId, options?: StalkerOptions): void;
    function unfollow(threadId?: ThreadId): void;
function parse(events: ArrayBuffer, options?: StalkerParseOptions): StalkerEventFull[] | StalkerEventBare[];
......
}


interface StalkerOptions {
    events?: {
        call?: boolean;
        ret?: boolean;
        exec?: boolean;
        block?: boolean;
        compile?: boolean;
    };
    onReceive?: (events: ArrayBuffer) => void;
    onCallSummary?: (summary: StalkerCallSummary) => void;
......
}


interface StalkerParseOptions {
    annotate?: boolean;
    stringify?: boolean;
}
type StalkerEventFull = StalkerCallEventFull | StalkerRetEventFull | StalkerExecEventFull |
    StalkerBlockEventFull | StalkerCompileEventFull;
type StalkerEventBare = StalkerCallEventBare | StalkerRetEventBare | StalkerExecEventBare |
    StalkerBlockEventBare | StalkerCompileEventBare;

type StalkerCallEventFull = [ "call", NativePointer | string, NativePointer | string, number ];
type StalkerCallEventBare = [         NativePointer | string, NativePointer | string, number ];
......


onReceive(events) {
	var _events = Stalker.parse(events);
	for (var i = 0; i < _events.length; i++) {
		var addr1 = _events[i][1];
		var module1 = Process.findModuleByAddress(addr1);
		if (module1 && module1.name == "libxiaojianbang.so") {
			var addr2 = _events[i][2];
			var module2 = Process.findModuleByAddress(addr2);
			console.log(module1.name, addr1.sub(module1.base), module2.name, addr2.sub(module2.base));
		}
	}
}
/*
libxiaojianbang.so 0x1f64 libxiaojianbang.so 0x1440
libxiaojianbang.so 0x1710 libxiaojianbang.so 0x1630
libxiaojianbang.so 0x187c libart.so 0x34f218
......
*/

interface StalkerCallSummary {
    [target: string]: number;
}

var md5Addr = Module.getExportByName("libxiaojianbang.so", "Java_com_xiaojianbang_ndk_NativeHelper_md5");
Interceptor.attach(md5Addr, {
    onEnter: function () {
        this.tid = Process.getCurrentThreadId();
        Stalker.follow(this.tid, {
            events: {
                call: true,
            },
            onCallSummary(summary) {
                for (const addr in summary) {
                    var module = Process.findModuleByAddress(addr);
                    if (module && module.name == "libxiaojianbang.so") {
                        const num = summary[addr];
                        console.log(module.name, ptr(addr).sub(module.base), num);
                    }
                }
            },
        });
    }, onLeave: function () {
        Stalker.unfollow(this.tid);
    }
});
/*
libxiaojianbang.so 0x14a0 2
libxiaojianbang.so 0x15e0 1
libxiaojianbang.so 0x1610 1
libxiaojianbang.so 0x1460 1
libxiaojianbang.so 0x15d0 16
......
*/