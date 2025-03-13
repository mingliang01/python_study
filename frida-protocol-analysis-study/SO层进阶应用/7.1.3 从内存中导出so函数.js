function dump_so(so_name) {
    Java.perform(function () {
        var module = Process.getModuleByName(so_name);
        console.log("[name]:", module.name);
        console.log("[base]:", module.base);
        console.log("[size]:", module.size);
        console.log("[path]:", module.path);
        var currentApplication = Java.use("android.app.ActivityThread").currentApplication();
        var dir = currentApplication.getApplicationContext().getFilesDir().getPath();
        var path = dir + "/" + module.name + "_" + module.base + "_" + module.size + ".so";
        var file = new File(path, "wb");
        if (file) {
            Memory.protect(module.base, module.size, 'rwx');
            var buffer = module.base.readByteArray(module.size);
            file.write(buffer);
            file.flush();
            file.close();
            console.log("[dump]:", path);
        }
    });
}
dump_so("libxiaojianbang.so");
/*
[name]: libxiaojianbang.so
[base]: 0x74c6c39000
[size]: 28672
[path]: /data/app/com.xiaojianbang.app-Kykbukopl-edrrBKaPhfyg==/lib/arm64/libxiaojianbang.so
[dump]: /data/user/0/com.xiaojianbang.app/files/libxiaojianbang.so_0x74c6c39000_28672.so
*/