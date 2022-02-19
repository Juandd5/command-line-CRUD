import click

@click.group() #convierte a la función en un decorador
def clients():
    """Manages the clients lifecycle"""
    pass


@clients.command()#decimos que create es un comando
@click.pass_context #Nos da el objeto contexto
def create(ctx, name, company, email, position):
    """Creates a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """Lists all clients"""
    pass


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
