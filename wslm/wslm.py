import argparse

from .windows_command import WindowsCommandBase, WindowsCommandPort, WindowsCommandFireWall


class WindowsCommandArgParse:
    """
    命令解析类
    """

    def __init__(self):
        """
        初始化命令解析
        """

        self._parser = argparse.ArgumentParser(prog='wslm')
        self._subparsers = self._parser.add_subparsers(help='可选命令')
        self._parser.add_argument(
            '-s',
            '--power_shell',
            default=WindowsCommandBase.POWER_SHELL,
            help='PowerShell.exe 可执行文件路径'
        )
        self._parser.set_defaults(func=lambda *args, **kwargs: self._parser.print_help())

    def _parser_cmd_port(self):
        # windows10 端口转发管理
        port = self._subparsers.add_parser(
            name='port',
            help='windows10 端口转发管理'
        )
        port_subparsers = port.add_subparsers(
            help='windows10 端口转发管理'
        )

        port.set_defaults(func=lambda *args, **kwargs: port.print_help())

        # # 添加端口转发
        port_add = port_subparsers.add_parser('add', help='添加端口转发')
        port_add.add_argument(
            '-p',
            '--port',
            type=int,
            nargs='*',
            help='端口号',
            required=True
        )
        port_add.add_argument(
            '-w',
            '--wall',
            type=str,
            nargs='*',
            choices=WindowsCommandFireWall.WALL_TYPES,
            help='防火墙'
        )
        port_add.set_defaults(func=self.port_add_callback)

        # # 删除端口转发
        port_del = port_subparsers.add_parser('del', help='删除端口转发')
        port_del.add_argument(
            '-p',
            '--port',
            type=int,
            nargs='*',
            help='端口号',
            required=True
        )
        port_del.add_argument(
            '-w',
            '--wall',
            type=str,
            nargs='*',
            choices=WindowsCommandFireWall.WALL_TYPES,
            help='防火墙'
        )
        port_del.set_defaults(func=self.port_del_callback)

    @staticmethod
    def port_add_callback(namespace, parser, *args, **kwargs):
        windows_command_port = WindowsCommandPort()
        windows_command_fire_wall = WindowsCommandFireWall()
        for port in namespace.port:
            windows_command_port.add(port=port, power_shell=namespace.power_shell)
            if namespace.wall is None:
                continue
            for wall in namespace.wall:
                if wall == windows_command_fire_wall.FIRE_WALL_RULE_OUT:
                    windows_command_fire_wall.add_out(port=port, power_shell=namespace.power_shell)
                elif wall == windows_command_fire_wall.FIRE_WALL_RULE_IN:
                    windows_command_fire_wall.add_in(port=port, power_shell=namespace.power_shell)
            else:
                windows_command_fire_wall.add_out(port=port, power_shell=namespace.power_shell)
                windows_command_fire_wall.add_in(port=port, power_shell=namespace.power_shell)

    @staticmethod
    def port_del_callback(namespace, parser, *args, **kwargs):
        windows_command_port = WindowsCommandPort()
        windows_command_fire_wall = WindowsCommandFireWall()
        for port in namespace.port:
            windows_command_port.delete(port=port, power_shell=namespace.power_shell)
            if namespace.wall is None:
                continue
            for wall in namespace.wall:
                if wall == windows_command_fire_wall.FIRE_WALL_RULE_OUT:
                    windows_command_fire_wall.delete_out(port=port, power_shell=namespace.power_shell)
                elif wall == windows_command_fire_wall.FIRE_WALL_RULE_IN:
                    windows_command_fire_wall.delete_in(port=port, power_shell=namespace.power_shell)
            else:
                windows_command_fire_wall.delete_out(port=port, power_shell=namespace.power_shell)
                windows_command_fire_wall.delete_in(port=port, power_shell=namespace.power_shell)

    def run(self):
        # 解析参数，并执行回调方法
        _args = self._parser.parse_args()
        _func = getattr(_args, 'func', None)
        if _func:
            _func(namespace=_args, parser=self._parser)
        else:
            self._parser.print_help()


def main():
    """
    主方法
    :return:
    """

    windows_command_arg_parse = WindowsCommandArgParse()
    windows_command_arg_parse.run()


if __name__ == '__main__':
    main()
