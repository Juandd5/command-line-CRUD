import csv
import os
from clients.models import Client


class ClientServices:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        """Creates a new client
        Args:
            client (Client): Object from Client class
        """
        with open(self.table_name, mode='a', encoding='utf_8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        """Generates the client list
        Returns:
            list: a list of dicts with the clients in it
        """
        with open(self.table_name, mode='r', encoding='utf_8') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)

    def update_client(self, updated_client):
        """Updates a client from the list
        Args:
            updated_client (Client): It is an object from Client class
        """
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['id'] == updated_client.id:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)
        
        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients):
        """Saves the clients list to the teable_name file
        Args:
            clients (list): It is a list of dicts with the clients in it
        """
        temporary_table_name = self.table_name + '.tmp'
        with open(temporary_table_name, mode='w', encoding='utf_8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(temporary_table_name, self.table_name)
