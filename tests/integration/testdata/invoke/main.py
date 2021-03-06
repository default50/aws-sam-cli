import time
import os
import sys
print('Loading function')


def handler(event, context):
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])

    sys.stdout.write("Docker Lambda is writing to stderr")

    return "Hello world"


def sleep_handler(event, context):
    time.sleep(10)
    return "Slept for 10s"


def env_var_echo_hanler(event, context):
    return os.environ.get("CustomEnvVar")


def write_to_stderr(event, context):
    sys.stderr.write("Docker Lambda is writing to stderr")

    return "wrote to stderr"


def write_to_stdout(event, context):
    sys.stdout.write("Docker Lambda is writing to stdout")

    return "wrote to stdout"
