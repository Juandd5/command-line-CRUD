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
@click.pass_context
def update(ctx, client_id):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_id):
    """Deletes a client"""
    pass

#genero un alias de clients
all = clients
