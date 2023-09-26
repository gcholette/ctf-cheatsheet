# Web stuff

## Enum

## Resources
- [:alien: Revshells](https://www.revshells.com/)
- [hacktricks](https://book.hacktricks.xyz/pentesting-web/web-vulnerabilities-methodology)
- [prototype pollution](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)

  
### nmap
```shell
nmap -sC -A -T4 <ip>
```

### ffuf
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

## Foothold
- Look for
    - SSTI
    - SQL injections
    - SSRF


