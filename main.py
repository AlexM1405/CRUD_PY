import csv
import os

CLIENTS_TABLE = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients =  []

def _initialize_clients_from_storage():
     with open(CLIENTS_TABLE, mode="r") as f:
          reader = csv.DictReader(f, fieldnames=[])

          for row in reader:
               clients.append(row)

def _save_clients_to_storage():
     tmp_table_name = "{}.tmp".format(CLIENTS_TABLE)
     with open(tmp_table_name, mode="w") as f:
             writer = csv.writer(f, fildnames =CLIENT_SCHEMA)
             writer.writerows(clients)

             os.remove(CLIENTS_TABLE)
     os.rename(tmp_table_name, CLIENTS_TABLE)

def create_client(client):
    global clients
    if client_name not in clients:
        clients.append (client)
    else:
        print("Client already in clients list ")

def list_clients():
	for idx, client in enumerate(clients):
		 print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))
           
def ingress_client_data(): 
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }
    return client

def update_client(client_id, updated_client):
    global clients
    if len(clients) -1 >= client_id:                
        clients[client_id] = updated_client
    else:
        print("Client not in client\'s list")
    
def delete_client(client_name):
    global clients
    if  client_name in clients:
        clients.remove(client_name)
    else:
         print("Client not in client\'s list")
            
def search_client(client_name):
	for client in clients:
		if client != client_name:
			continue
		else:
			return True
          
def _get_client_field(field_name):
     while not field:
          field = input('What is the client {}? '.format(field_name) )

          return field


def _get_client_name():
    return input('What is the client name?')



def _print_welcome():
    print("Welcome to SneakersBA POS")
    print("What would like to do Today?")
    print ('*' * 52) 
    print ('[C]reate client')
    print ('[R]ead client\'s list ')
    print ('[U]pdate client')
    print ('[D]elete client')
    print ('[S]earch client')

if __name__ == '__main__':
    _initialize_clients_from_storage
    _print_welcome()
    command = input().lower()
    if command == 'c':
        client = {
             "name": _get_client_field("name"),
             "company": _get_client_field("company"),
             "email": _get_client_field("email"),
             "position": _get_client_field("position"),
        }
        create_client(client) 
        list_clients()
    elif command == 'r':
        list_clients()
    elif command == 'u':
        client_name = _get_client_name() 
        update_client(client_name)
    elif command == 'd':
        client_name = _get_client_name() 
        delete_client(client_name)
    elif command == 's':
        client_name = _get_client_name() 
        found = search_client(client_name) 

        if found:
            print (f'The client: {client_name}, has been found')
        else:
            print (f'The client: {client_name}, has not been found')
    else:
        print('ERROR: Invalid command')
    
    _save_clients_to_storage()

    input() 
     
    