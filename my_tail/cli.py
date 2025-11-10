# my_tail/cli.py
import click
import sys
import time
from collections import deque
from typing import TextIO


def tail_file(f: TextIO, n: int):
    """
    Повертає останні n рядків з файлу-об'єкта f.
    Реалізовано через deque для пам'яті O(n).
    """
    dq = deque(maxlen=n)
    for line in f:
        dq.append(line.rstrip('\n'))
    for line in dq:
        click.echo(line)


def follow_file(fpath: str, n: int, sleep_interval: float = 0.5):
    """
    Реалізація tail -f: читаємо останні n рядків, потім слідкуємо за додаваннями.
    """
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            # прочитати всі та вивести останні n
            tail_file(f, n)
            # перейти в кінець і слідкувати
            f.seek(0, 2)
            while True:
                where = f.tell()
                line = f.readline()
                if not line:
                    time.sleep(sleep_interval)
                    f.seek(where)
                else:
                    click.echo(line.rstrip('\n'))
    except FileNotFoundError:
        click.echo(f"my-tail: cannot open '{fpath}': No such file or directory", err=True)
        sys.exit(1)
    except KeyboardInterrupt:
        # Graceful exit on Ctrl+C when following
        sys.exit(0)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-n', '--lines', default=10, show_default=True, help='Кількість рядків з кінця.')
@click.option('-f', '--follow', is_flag=True, help='Слідкувати за файлом (like tail -f).')
@click.argument('file', required=False, type=click.Path(exists=False))
def cli(lines: int, follow: bool, file):
    """
    my-tail — проста реалізація tail з опціями -n та -f.

    Якщо файл не вказано, читає зі stdin.
    """
    if follow:
        if not file:
            click.echo("my-tail: -f requires a file argument", err=True)
            sys.exit(2)
        follow_file(file, lines)
    else:
        if file:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    tail_file(f, lines)
            except FileNotFoundError:
                click.echo(f"my-tail: cannot open '{file}': No such file or directory", err=True)
                sys.exit(1)
        else:
            # stdin
            tail_file(sys.stdin, lines)


if __name__ == '__main__':
    cli()
