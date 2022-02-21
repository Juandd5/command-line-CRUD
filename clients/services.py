import csv
import os
from clients.models import Client


class ClientServices:

    def __init__(self, table_name):
        self.table_name = table_name #recibe el nombre de nuestro archivo .csv

    def create_client(self, client):
        """Creates a new client
        Args:
            client (Client): Object from Client class
        """
        with open(self.table_name, mode='a', encoding='utf_8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())#schema() retorna las llaves del dict
            writer.writerow(client.to_dict())#escribimos una nueva fila
            #el cliente que recibimos como parametro lo convertimos a dict

    def list_clients(self):
        """Generates the client list
        Returns:
            list: a list of dicts with the clients in it
        """
        with open(self.table_name, mode='r', encoding='utf_8') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader) #reader es un iterable que contiene a cada cliente como un dict

    def update_client(self, updated_client):
        """Updates a client from the list
        Args:
            updated_client (Client): It is an object from Client class
        """
        clients = self.list_clients() #guardamos las lista de clientes por lo tanto abrimos el archivo

        updated_clients = [] #defino una nueva lista donde voy a guardar todos los clientes
        for client in clients: #se guardan todos los clientes, menos el que se quiera actualizar porque
            if client['id'] == updated_client.id: #ese se omite y se almacena el actualizado
                #ya que updated_client es un objeto Client, cuando lo agregamos a la lista
                #lo hacemos en una representación de dict con el método to_dict()
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)
        
        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients):
        """Saves the clients list to the teable_name file
        Args:
            clients (list): It is a list of dicts with the clients in it
        """
        temporary_table_name = self.table_name + '.tmp' #creo una tabla temporal y añado el .tmp para diferenciarlos

        with open(temporary_table_name, mode='w', encoding='utf_8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)# guardamos todos nuestros clientes actualizados en el nuevo archivo

    #por úlitmo sustituimos a la tabla original por la temporal ya que esta tiene los clientes actualizados
        os.remove(self.table_name)
        os.rename(temporary_table_name, self.table_name)

    def delete_client(client_id):
        pass
