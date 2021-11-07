#!/usr/bin/env python3

import sys
import os

usage = 'Usage: run {--remove-prev, --help}'

options = ['--remove-prev']
extra_args = []
remove_commands = [
    'docker stop c_echo',
    'docker rm c_echo',
]

option = None

num_arguments = len(sys.argv) - 1

# Argument validation
if num_arguments == 0:
    pass
elif num_arguments == 1:
    option = sys.argv[1]
    if option == '--help':
        print(usage)
        exit(0)
    else:
        if option not in options:
            raise ValueError('Unknown option: {}'.format(option))
else:
    raise ValueError('Bad arguments')

extra_args = ' '.join([v for v in extra_args])

if option == '--remove-prev':
    for command in remove_commands:
        os.system(command)

# Run docker compose
os.system(
    'docker-compose -f echo.yml up --build --force-recreate {}'
    .format(extra_args)
)
