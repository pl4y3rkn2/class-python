import csv
import os


CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
CLIENT_TABLE = '.clients.csv'
clients = []


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx, 
            name=client['name'], 
            company=client['company'], 
            email=client['email'], 
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message='What is the client {}?'):
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

def while_not(client_name):
    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
             client_name = None
             break
            
    if not client_name:
        sys.exit()
    return client_name     

def menu_list():
    global menu
    menu = input('do you want to return to the menu? (Y/N): ')
    menu = menu.upper()

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?:')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


if __name__ == '__main__':
    _initialize_clients_from_storage()
    menu = 'Y'
    while menu == 'Y':
        _print_welcome()

        command = input(': ')
        command = command.upper()

        if command == 'C':
            client = _get_client_from_user()

            create_client(client)
            list_clients()
            menu_list()
                       
        elif command == 'L':
            list_clients()
            menu_list()

        elif command == 'U':
            client_id = int(_get_client_field('id'))
            updated_client = _get_client_from_user()

            update_client(client_id, updated_client)
            list_clients()
            menu_list()

        elif command == 'D':
            client_id = int(_get_client_field('id'))

            delete_client(client_id)
            list_clients()
            menu_list()

        elif command == 'S':
            client_name = _get_client_field('name')
            found = search_client(client_name)
        
            if found:
                print('The client is in the client\'s list')
                menu_list()
            else:
                print('The client: {} is not in our client\'s list'.format(client_name))
                menu_list()
        else:
            print('Invalid command')
            menu_list()

    _save_clients_to_storage()