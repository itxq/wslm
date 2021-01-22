WSL Management Tool
===============

### Repository

【Coding】[https://e.coding.net/xqitw/wslm/wslm.git](https://xqitw.coding.net/public/wslm/wslm/git/files)

【Gitee】[https://gitee.com/itxq/wslm.git](https://gitee.com/itxq/wslm.git)

【GitHub】[https://github.com/itxq/wslm.git](https://github.com/itxq/wslm.git)

### Installation

```shell
pip install wslm
```

### Help

```shell
# eg:
wslm -h
wslm port -h
wslm port add -h
```

### Base

```shell
# set encoding , PowerShell.exe PATH
wslm -e utf-8 -s PowerShell.exe
# eg:
wslm -e utf-8 -s PowerShell.exe port add -p 3306 3307 -w
wslm -e gbk -s PowerShell.exe port add -p 3306 3307 -w
```

### Ports info

```shell
# view ports info
wslm port info

# show
Ports Info:
+---------------+------------+----------------+-------------+
| ListenAddress | ListenPort | ConnectAddress | ConnectPort |
+---------------+------------+----------------+-------------+
|    0.0.0.0    |    3306    |  172.23.60.88  |     3306    |
|    0.0.0.0    |    6379    |  172.23.60.88  |     6379    |
+---------------+------------+----------------+-------------+

NetFireWallRules Info:
+-------------------------------------+-----------+--------+---------+
|             DisplayName             | Direction | Action | Enabled |
+-------------------------------------+-----------+--------+---------+
| WSL 2 Firewall Unlock Outbound 3306 |  Outbound | Allow  |   True  |
|  WSL 2 Firewall Unlock Inbound 3306 |  Inbound  | Allow  |   True  |
| WSL 2 Firewall Unlock Outbound 6379 |  Outbound | Allow  |   True  |
|  WSL 2 Firewall Unlock Inbound 6379 |  Inbound  | Allow  |   True  |
+-------------------------------------+-----------+--------+---------+

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

### Reset Ports

```shell
# reset ports
wslm port reset
# reset ports with firewall
wslm port reset -w
```