
import csv
import os

from Clients.models import Client

class Client_Services:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, Client ):
        with open(self.table_name, mode="a") as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(Client.to_dict())
    
    def list_clients(self, Client):
        with open(self.table_name, mode="r") as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())

            return list(reader)
        
    def update_client(self, updated_client):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client ["uid"] == updated_client.uid:
                updated_clients.append(updated_client())
            else:
                updated_clients.sappend(client)

        self._save_to_disk(updated_clients)
    
def delete_client(self, deleted_client):
		clients = self.list_clients()
		updated_clients = []
		for client in clients:
			if client['uid'] == deleted_client.uid:
				continue 
			else:
				updated_clients.append(client)

		self._save_to_disk(updated_clients)
            

def _save_to_disk(self, clients):
        temp_table_name = self.table_name + '.tmp'
        with open(temp_table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)

        