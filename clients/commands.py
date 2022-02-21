from itertools import count
import click
from clients.models import Client
from clients.services import ClientServices
from tabulate import tabulate


@click.group() #convierte a la función en un decorador
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()#decimos que create es un comando
@click.option('-n', '--name',#tenemos un nombre abreviado y el nombre completo
                type = str, #El tipo es string
                prompt = True, #Si no lo dan con el patrón abreviado, se lo pedimos al usuario
                help = 'The client name') #creamos una línea de ayuda
@click.option('-c', '--company',
                type = str,
                prompt = True,
                help = 'The client company')
@click.option('-e', '--email',
                type = str,
                prompt = True,
                help = 'The client email')
@click.option('-p', '--position',
                type = str,
                prompt = True,
                help = 'The client position')
@click.pass_context #Nos da el objeto contexto
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position) #creamos un cliente
    client_service = ClientServices(ctx.obj['clients_table'])
    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """Lists all clients"""
    #creamos un objeto de ClientServices y le pasamos el nombre del archivo de clientes
    client_services = ClientServices(ctx.obj['clients_table'])

    client_list = client_services.list_clients() #traemos la lista de clientes (lista de diccionarios)
    headers = [field.upper() for field in Client.schema()] #llaves del dict para titulo de la tabla
    table = []#será una lista que contiene en cada índice una lista con los datos del cliente
  
    for client in client_list:
        table.append([client["name"], client["company"], client["email"], client["position"], client["id"]])

    click.echo(tabulate(table, headers))#cumple la función de print, pero echo es para cualquier SO


@clients.command()
@click.argument('client_id', type=str) #pido el id como argumento
@click.pass_context
def update(ctx, client_id):
    """Updates a client"""
    client_service = ClientServices(ctx.obj['clients_table'])

    client_list = client_service.list_clients() #nos traemos la lista de clientes

    client = [client for client in client_list if client['id'] == client_id]
    #en client solo se almacena un diccionario si coincide con el id del cliente
    if client:
        client = _update_client_flow(Client(**client[0]))#pasamos un objeto tipo Client y le damos los valores
        #que tiene tiene el único diccionario de la lista client
        client_service.update_client(client)

        click.echo('Client is updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    """Updates client data as desired by the user
    Args:
        client (Client): it is an object from Client class
    returns:
        Client: an update object from Client class
    """
    click.echo('Leave the field empty if you do not want to modify it/n')
    #pediremos las datos del nuevo cliente, el usuario puede cambiarlos todos o los que desee
    #en caso de que solo quiera cambiar un campo, los demás quedan como estaban
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client


@clients.command()
@click.argument('client_id', type=str)
@click.pass_context
def delete(ctx, client_id):
    """Deletes a client"""
    client_service = ClientServices(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    client_in_list = False

    for idx, client in enumerate(clients_list):
        if client['id'] == client_id:
            del clients_list[idx]
            client_in_list = True
            break
    
    click.echo(f'Client {"deleted" if client_in_list else "not found"}')
    
    client_service._save_to_disk(clients_list)


#genero un alias de clients
all = clients
