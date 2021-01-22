from functools import wraps

from .util import Color
from .windows_command import WindowsCommandPort, WindowsCommandFireWall


def __print_port_info(namespace, parser, *args, **kwargs):
    """
    输出端口转发信息到控制台
    :param args:
    :param kwargs:
    :return:
    """

    port_info_table = WindowsCommandPort(
        encoding=namespace.encoding,
        power_shell=namespace.power_shell
    ).info_table()
    print(Color.cyan('Ports Info:'))
    print(Color.green(port_info_table))


def __print_wall_info(namespace, parser, *args, **kwargs):
    """
    输出防火墙信息到控制台
    :param args:
    :param kwargs:
    :return:
    """

    wall_info_table = WindowsCommandFireWall(
        encoding=namespace.encoding,
        power_shell=namespace.power_shell
    ).info_table()
    print(Color.cyan('NetFireWallRules Info:'))
    print(Color.green(wall_info_table))


def print_port_info(func):
    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __print_port_info(**kwargs)
        return _result

    return __wraps


def print_wall_info(func):
    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __print_wall_info(**kwargs)
        return _result

    return __wraps


def print_port_wall_info(func):
    @wraps(func)
    def __wraps(*args, **kwargs):
        _result = func(*args, **kwargs)
        __print_port_info(**kwargs)
        __print_wall_info(**kwargs)
        return _result

    return __wraps
