# SSH-SERVER

  * Get server data from YAML config for SSH.

### How to use 
1. Clone code to your machine.
1. Install code in virtualenv or machine
``` python setup.py install ``` 
1. You can use `ssh-server` command 
``` ssh-server <server-name> ```
1. You can add or edit server file in `~/ssh-server`

### Sample server file
```
- 
  server-name : server-01
  host : 192.168.1.123
  user : ubuntu
  port : 22
- 
  server-name : server-01
  host : 192.168.1.124
  user : ubuntu
  port : 1234
