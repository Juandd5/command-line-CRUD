import click
from clients import commands as clients_commands #importamos los comandos del módulo commands.py

CLIENTS_TABLE = '.clients.csv'


@click.group() #Le decimos a python que este es nuestro punto de entrada
@click.pass_context #Nos da un objeto contexto
def cli(ctx): #Este es nuestro punto de entrada. El argumento es nuestro objeto contexto
    ctx.obj = {} #Inicializamos el contexto como un diccionario vacío
    ctx.obj['clients_table'] = CLIENTS_TABLE #Añadimos la tabla al contexto


cli.add_command(clients_commands.all) #all es una alias de la función clients en el módulo commands.py
