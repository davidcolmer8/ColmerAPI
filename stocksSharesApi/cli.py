import click
from flask.cli import FlaskGroup

from .app import create_app


def create_stocksSharesApi(info):
    return create_app(cli=True)

@click.group(cls=FlaskGroup, create_app=create_stocksSharesApi)
def cli():
    """Omnia Analytics data access and systems
    """

@cli.command("init")
def init():
    """Init application, create database tables
    and create a new user named admin with password admin
    """

    click.echo("...init complete")

cli.add_command(init)
