import grpc
import chat_pb2
import chat_pb2_grpc



class ClientApp:
    def __init__(self):
        self.is_connected = False
        self.is_joined = False
        self.client = None
        self.channel = None
        self.start_app()

    def start_app(self):
        channel = grpc.insecure_channel('localhost:1997')
        stub = chat_pb2_grpc.ChatServicesStub(channel)
        resp = stub.connexion(chat_pb2.Client(name="blbla"))
        
        print("starting app ")
        while True:
            command = input().strip()
            if command == 'exit':
                if self.is_connected:
                    self.disconnect(stub, self.client.name)
                return

            if ' ' in command:
                args = command.split(' ', 1)
                if args[0] == 'connect':
                    if self.is_connected:
                        print(f'you are already connected as {self.client.name}')
                        continue
                    self.is_connected = True
                    self.connect(stub, args[1])
                elif args[0] == 'join':
                    if not self.is_connected:
                        print('you need to be connected first')
                        continue
                    if self.is_joined:
                        print(f'you are already joinned: {self.channel.chanel_name}')
                        continue
                    self.is_joined = True
                    self.join(stub, args[1])
                elif args[0] == 'list':
                    if not self.is_joined:
                        print('you need to join a channel')
                        continue
                    self.list_clients(stub, args[1])
                elif args[0] == 'send':
                    if not self.is_joined:
                        print('you need to join a channel')
                        continue
                    self.send_message(stub, args[1])
                elif args[0] == 'leave':
                    if not self.is_joined:
                        print('you need to join a channel')
                        continue
                    self.leave(stub, args[1])
                elif args[0] == 'disconnect':
                    if not self.is_connected:
                        print('you need to be connected first')
                        continue
                    self.disconnect(stub, args[1])
                else:
                    print('syntax error !!!')
            else:
                print('syntax error !!!')

    def connect(self, stub, nick_name):
        self.client = chat_pb2.Client(name=nick_name)
        responses = stub.connexion(self.client)
        for response in responses:
            if response.type == chat_pb2.ResponseType.Value('ISCONNECTED'):
                print('----------------------------')
                print(f'connect as {nick_name} status: {response.type}')
                print('----------------------------')
            else:
                print('----------------------------')
                print(response.message)
                print('----------------------------')


    def join(self, stub, channel_name):
        self.channel = chat_pb2.Channel(chanelName=channel_name, client=self.client)
        responses = stub.join(self.channel)
        self.is_joined = True
        for response in responses:
            print('----------------------------')
            print(f'join {channel_name} status: {response.type}')
            print('----------------------------')


    def leave(self, stub, channel_name):
        if self.channel.chanel_name != channel_name:
            print(f"wrong channel, the channel you\'ve joined is {self.channel.chanel_name}")
            return

        responses = stub.leave(self.channel)
        self.channel = None
        self.is_joined = False
        for response in responses:
            print('----------------------------')
            print(f'leave {channel_name} status: {response.type}')
            print('----------------------------')


    def send_message(self, stub, message):
        message_to_send = chat_pb2.Message(channel=self.channel, text=message)
        responses = stub.sendMessage(message_to_send)

        for response in responses:
            print('----------------------------')
            print(f'message sent status : {response.type}')
            print('----------------------------')


    def list_clients(self, stub, channel_name):
        if self.channel.chanel_name != channel_name:
            print(f"wrong channel, the channel you\'ve joined is {self.channel.chanel_name}")
            return
        responses = stub.listClient(self.channel)

        for response in responses:
            print('----------------------------')
            print(f'message sent status : {response.type}\n')
            print(f"the clients list in channel {self.channel.chanel_name} : {response.message}")
            print('----------------------------')


    def disconnect(self, stub, client_name):
        if self.client.name != client_name:
            print(f"wrong client name, the name you\'ve chosen is {self.client.name}")
            return
        if self.is_joined:
            self.leave(stub, self.channel.chanel_name)

        responses = stub.disconnect(self.client)
        self.is_connected = False
        self.client = None
        for response in responses:
            print('----------------------------')
            print(f'diconnect {client_name} status : {response.type}')
            print('----------------------------')


if __name__ == '__main__':
    clientApp = ClientApp()
