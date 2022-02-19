import csv
from clients.models import Client


class ClientServices:

    def __init__(self, table_name):
        self.table_name = table_name #recibe nuestro el nombre de nuestro archivo .csv

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())#schema() retorna las llaves del dict
            writer.writerow(client.to_dict())#escribimos una nueva fila
            #el cliente que recibimos como parametro lo convertimos a dict
