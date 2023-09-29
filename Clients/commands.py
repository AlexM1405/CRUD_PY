import click

from Clients.services import Client_Services
from Clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()
@click.option( '-n','--name',
               type =str,
               prompt='Client name',
               help="The client's name")
@click.option( '-c','--company',
               type =str,
               prompt='Client company',
               help="The client's company")
@click.option( '-e','--email',
               type =str,
               prompt='Client email',
               help="The client's email")

@click.option( '-p','--position',
               type =str,
               prompt='Client position',
               help="The client's position")

@click.option( '-n','--name',
               type =str,
               prompt='Client name',
               help="The client's name")
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client."""
    client = Client(name, company, email, position)
    client_services = Client_Services(ctx.obj ["clients_table"])

    client_services.create_client(Client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all client"""
    client_services = Client_Services(ctx.obj ["clients_table"])

    clients_list = client_services.list_clients()

    click.echo( ' ID  | NAME  | COMPANY | EMAIL | POSITION  ')
    click.echo ('*' * 100)

    for client in clients:
        print(' {uid} | {name} |{company}| {email}  | {position}'.format(
            uid=client['id'],
            name=client["name"],
            company=client["company"],
            email=client["email"],
            position=client["position"]

        ))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    client_service = Client_Services(ctx.obj ["client_table"])

    client_list = client_service.list_clients()

    client = [ client for client in client_list if client["uid"] == client_uid]

    if client:
        client = _update_client_flow(Client(client[0]))
        client_service.update_client(client)
    else:
        click.echo("Client not found")

def _update_client_flow(client):
    click.echo("Leave empty if you want to modify the value")

    client.name = click.prompt("New name", type=str, default=client.name)
    client.company= click.prompt("New company", type=str, default=client.company)
    client.email = click.prompt("New email", type=str, default=client.email)
    client.position = click.prompt("New position", type=str, default=client.position)

    return client



@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass

all = clients
