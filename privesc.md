# Privesc
## Enum tools
- [Lin Peas](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)
- [pspy](https://github.com/DominicBreuker/pspy)
- [Lin Enum](https://github.com/rebootuser/LinEnum)
- [RustScan](https://github.com/RustScan/RustScan)

## Resources
- [gtfobins](https://gtfobins.github.io/gtfobins/ssh/)
- [hacktricks (linux)](https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses)
- [hacktricks (windows)](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

## Operations
```
sudo -l
```
```
bash -p
```

### ssh private key

```
# victim
ssh-keygen -t rsa -b 4096
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Host
## copy key to host
chmod 600 /path/to/id_rsa_custom
ssh -i /path/to/id_rsa_custom user@target_machine_ip
```
