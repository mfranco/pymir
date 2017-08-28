from pymir import settings

from pymir.commands import *  # noqa

import argparse
import importlib
import pymir.commands


def execute_command(cmd, **kwargs):
    """
    Loads all commands from commands directory
    """
    cmd_dict = {
        c: 'pymir.commands.' + c for c
            in dir(pymir.commands) if not c.startswith('_') and c != 'os'
    }

    if cmd not in cmd_dict:
        print('command {} does not exists\n'.format(cmd))
        print('valid commands are:\n')
        for k, v in cmd_dict.items():
            print('{}\n'.format(k))
        exit(1)

    cmd_module = importlib.import_module(cmd_dict[cmd])
    cmd_module.run()


def load_settings(settings_module):
    # loading settings module and adding values to global configuration
    s = importlib.import_module(settings_module)

    for v in dir(s):
        if not v.startswith('_'):
            setattr(settings, v, getattr(s, v))

def main():
    description = 'pymir runner'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('command', help='command to execute')
    parser.add_argument(
        '--settings', help='config file path', default='config.development')

    args, extra_params = parser.parse_known_args()
    load_settings(args.settings)
    execute_command(args.command)


if __name__ == '__main__':
    main()
