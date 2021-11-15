#!/usr/bin/env python3

import sys
import os

usage = 'Usage: run {--remove-prev, --help}'

options = ['--remove-prev']
remove_commands = [
    'docker stop c_sample',
    'docker rm c_sample',
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

if option == '--remove-prev':
    for command in remove_commands:
        os.system(command)

# Run docker compose
os.system(
    'docker-compose -f sample.yml up --build --force-recreate'
)
