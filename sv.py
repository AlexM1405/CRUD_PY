import click

from Clients import commands as Clients_commands 

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command(Clients_commands.all)