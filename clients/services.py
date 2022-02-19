import csv
from encodings import utf_8
from clients.models import Client


class ClientServices:

    def __init__(self, table_name):
        self.table_name = table_name #recibe el nombre de nuestro archivo .csv

    def create_client(self, client):
        with open(self.table_name, mode='a', encoding='utf_8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())#schema() retorna las llaves del dict
            writer.writerow(client.to_dict())#escribimos una nueva fila
            #el cliente que recibimos como parametro lo convertimos a dict

    def list_clients(self):
        with open(self.table_name, mode='r', encoding='utf_8') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader) #reader es un iterable que contiene los valores del dict
