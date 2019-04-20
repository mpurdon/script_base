import click

import sys


@click.command
def main():
    click.echo('Hello world')

    return 1


if __name__ == '__main__':

    sys.exit(main())
