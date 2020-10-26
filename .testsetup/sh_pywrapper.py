from __future__ import print_function

import subprocess
import pexpect
from pexpect import replwrap
from io import StringIO
import sys

def create_process(interpreter='/bin/bash'):
    '''Create shell process'''
    process = pexpect.replwrap.bash()
    return process


def kill_process(process):
    '''Kill shell process'''
    pass


def parse(sh_filename):
    '''parse a shell script file into individual commands'''
    sh_file = open(sh_filename)

    commands_list = [[]]
    current_commands = []
    for line in sh_file:
        line = line.rstrip()

        # Split on new lines - register only if command is not empty
        if line == "" and len(commands_list[-1]) > 0:
            commands_list.append([])
        elif line != "":
            commands_list[-1].append(line)

    print (commands_list)
    return commands_list


def run(process, command_list):
    '''Run list of commands - one at a time - and collect output'''
    outputs = []
    for command in command_list:
        print("Running: ", command)
        output = process.run_command(command, timeout=120)
        outputs.append(output)
        print(output)
    return outputs


def exec_python(python_line_list):
    '''eval python code lines - one at a time - and collect output'''
    print("Evaluating: ", python_line_list)
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    output = exec("\n".join(python_line_list), globals())
    sys.stdout = old_stdout
    return (output, mystdout.getvalue())


def get_cwd(process):
    '''Get current working directory in child process'''
    output = process.run_command('pwd')
    return output

