import io
import click

from typing import Optional
from tuubacrypt import TuubaCrypt # type: ignore

def println(text: str) -> None:
    click.echo(text, nl=False)

def get_stream() -> str:
    return "".join(click.get_text_stream('stdin').readlines())

@click.group()
@click.version_option()
@click.pass_context
def main(ctx: click.Context) -> None:
    """The least useful encryption and decryption algorithm."""
    ctx.ensure_object(dict)
    ctx.obj['tcrypt'] = TuubaCrypt()

@main.command()
@click.pass_context
@click.argument('text', type=click.STRING, required=False)
def encrypt(ctx: click.Context, text: str) -> None:
    """Encrypt data from STDIN or <TEXT>"""
    tcrypt = ctx.obj['tcrypt']

    if not text:
        text = get_stream()

    println(tcrypt.encrypt(text))

@main.command()
@click.pass_context
@click.argument('text', type=click.STRING, required=False)
def decrypt(ctx: click.Context, text: str) -> None:
    """Decrypt data from STDIN or <TEXT>"""
    tcrypt = ctx.obj['tcrypt']

    if not text:
        text = get_stream()

    println(tcrypt.decrypt(text))
