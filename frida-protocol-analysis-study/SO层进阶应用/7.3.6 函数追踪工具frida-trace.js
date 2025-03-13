trace_natives插件
-a 'libxiaojianbang.so!0x16bc' -a 'libxiaojianbang.so!0x1854' -a 'libxiaojianbang.so!0x188c' -a 'libxiaojianbang.so!0x18c4' -a 'libxiaojianbang.so!0x190c' -a 'libxiaojianbang.so!0x1a0c' -a 'libxiaojianbang.so!0x1a44' -a 'libxiaojianbang.so!0x1a84' -a 'libxiaojianbang.so!0x1acc' 
......

frida-trace -UF -O C:\Users\Administrator\Desktop\libxiaojianbang_1634124936.txt

Instrumenting...
sub_16bc: Auto-generated handler at "D:\\Project\\JSProject\\HookProject\\src\\__handlers__\\libxiaojianbang.so\\sub_16bc.js"
......
Started tracing 25 functions. Press Ctrl+C to stop.
           /* TID 0x27ac */
 59084 ms  sub_1f2c()
 59084 ms     | sub_16bc()
 59084 ms     |    | sub_1854()
 ......
 59085 ms     | sub_2230()
 59085 ms     | sub_22a0()
 59085 ms     | sub_3a78()
 59085 ms     |    | sub_3b74()
 59085 ms     |    | sub_22a0()
 59085 ms     |    | sub_22a0()
 59086 ms     |    |    | sub_2518()
 59086 ms     |    |    |    | sub_3cb0()
 59086 ms     |    | sub_3b74()
 59086 ms     | sub_20f4()
 ......
 59086 ms     | sub_21f0()
 59087 ms     | sub_188c()


{
  onEnter(log, args, state) {
    log('sub_22a0()');
  },
  onLeave(log, retval, state) {
  }
}

{
  onEnter(log, args, state) {
    log('sub_22a0()', DebugSymbol.fromAddress(this.context.pc).name, hexdump(args[1], {length: 16, header: false}), args[2]);
  },
  onLeave(log, retval, state) {
  }
}

Instrumenting...
sub_16bc: Loaded handler at "D:\\Project\\JSProject\\HookProject\\src\\__handlers__\\libxiaojianbang.so\\sub_16bc.js"
......
Started tracing 25 functions. Press Ctrl+C to stop.
           /* TID 0x27ac */
  2755 ms  sub_1f2c()
  2755 ms     | sub_16bc()
  2755 ms     |    | sub_1854()
  ......
  2756 ms     | sub_2230()
  2756 ms     | sub_22a0()  _Z9MD5UpdateP7MD5_CTXPhj
75a2798bb0  78 69 61 6f 6a 69 61 6e 62 61 6e 67 00 00 c0 41  xiaojianbang...A
0xc
  2758 ms     | sub_3a78()
  2758 ms     |    | sub_3b74()
  2758 ms     |    | sub_22a0()  _Z9MD5UpdateP7MD5_CTXPhj
75f02d7000  80 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................ 
0x2c
  2759 ms     |    | sub_22a0()  _Z9MD5UpdateP7MD5_CTXPhj
7fc209c7c0  60 00 00 00 00 00 00 00 c0 98 f2 f3 97 9d a5 df  `............... 
0x8
  2759 ms     |    |    | sub_2518()
  2759 ms     |    |    |    | sub_3cb0()
  2759 ms     |    | sub_3b74()
  2760 ms     | sub_20f4()
  ......
  2761 ms     | sub_21f0()
  2761 ms     | sub_188c()


frida-trace -UF -j '*!*certificate*/isu'
frida-trace -UF -i "Java_*"