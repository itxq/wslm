WSL Management Tool
===============

### Installation

```shell
pip install wslm
```

### Add Ports

```shell
# add ports
wslm port add -p 3306 3307
# add ports with firewall
wslm port add -p 3306 3307 -w
# add ports with firewall Inbound
wslm port add -p 3306 3307 -w Inbound
# add ports with firewall Outbound
wslm port add -p 3306 3307 -w Outbound
```

### Delete Ports

```shell
# del ports
wslm port del -p 3306 3307
# del ports with firewall
wslm port del -p 3306 3307 -w
# del ports with firewall Inbound
wslm port del -p 3306 3307 -w Inbound
# del ports with firewall Outbound
wslm port del -p 3306 3307 -w Outbound
```