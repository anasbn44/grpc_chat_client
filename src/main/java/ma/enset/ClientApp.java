package ma.enset;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.stub.StreamObserver;
import ma.enset.stubs.Chat;
import ma.enset.stubs.ChatServicesGrpc;

import java.io.IOException;
import java.util.Scanner;

public class ClientApp {
    private boolean isConnected = false;
    private boolean isJoined = false;
    private Chat.Client client;
    private Chat.Channel channel;
    public static void main(String[] args) {
        new ClientApp();
    }

    private ClientApp (){
        try {
            this.startApp();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void startApp() throws IOException {
        ManagedChannel managedChannel = ManagedChannelBuilder.forAddress("localhost", 1997).usePlaintext().build();
        ChatServicesGrpc.ChatServicesStub servicesStub = ChatServicesGrpc.newStub(managedChannel);
        Scanner s = new Scanner(System.in);

        String command = s.nextLine();
        do{

            if(command.contains(" ")){
                String[] args = command.split(" ");

                switch (args[0]){
                    case "connect":
                        if (isConnected) {
                            System.out.println("you are already connected as " + client.getName());
                            break;
                        }
                        isConnected = true;
                        connect(servicesStub, args[1]);
                        break;
                    case "join" :
                        if (isConnected){
                            if(!isJoined){
                                isJoined = true;
                                join(servicesStub, args[1]);
                            }else {
                                System.out.println("you are already joinned : " + channel.getChanelName());
                            }
                        } else {
                            System.out.println("you need to be connected first");
                        }
                        break;
                    case "list" :
                        if (isJoined){
                            listClients(servicesStub, args[1]);
                        } else {
                            System.out.println("you need to join a channel");
                        }
                        break;
                    case "send" :
                        if (isJoined){
                            sendMessage(servicesStub, args[1]);
                        } else {
                            System.out.println("you need to join a channel");
                        }
                        break;
                    case "leave" :
                        if (isJoined){
                            isJoined = false;
                            leave(servicesStub, args[1]);
                        } else {
                            System.out.println("you need to join a channel");
                        }
                        break;
                    case "disconnect" :
                        if (isConnected){
                            isConnected = false;
                            disconnect(servicesStub, args[1]);
                        } else {
                            System.out.println("you need to be connected first");
                        }
                        break;
                }
            } else {
                System.out.println("syntax error !!!");
            }


        }while (!command.equals("exit"));
    }

    private void connect(ChatServicesGrpc.ChatServicesStub servicesStub, String nickName) throws IOException {


        StreamObserver<Chat.Client> connexion = servicesStub.connexion(new StreamObserver<Chat.Response>() {
            @Override
            public void onNext(Chat.Response response) {
                System.out.println("----------------------------");
                System.out.println("connect as " + nickName + " status : " + response.getType());
                System.out.println("----------------------------");
            }

            @Override
            public void onError(Throwable throwable) {

            }

            @Override
            public void onCompleted() {

            }
        });

        client = Chat.Client.newBuilder().setName(nickName).build();

        connexion.onNext(client);
    }

    private void join (ChatServicesGrpc.ChatServicesStub servicesStub, String channelName){
        StreamObserver<Chat.Channel> joining = servicesStub.join(new StreamObserver<Chat.Response>() {
            @Override
            public void onNext(Chat.Response response) {
                System.out.println("----------------------------");
                System.out.println("join " + channelName + " status : " + response.getType());
                System.out.println("----------------------------");
            }

            @Override
            public void onError(Throwable throwable) {

            }

            @Override
            public void onCompleted() {

            }
        });
        channel = Chat.Channel.newBuilder().setClient(client).setChanelName(channelName).build();
        joining.onNext(channel);
        joining.onCompleted();
    }

    private void leave (ChatServicesGrpc.ChatServicesStub servicesStub, String channelName){
        if(!channel.getChanelName().equals(channelName)){
            System.out.println("wrong channel, the channel you've joined is " + channel.getChanelName());
            return;
        }
        StreamObserver<Chat.Channel> leaving = servicesStub.leave(new StreamObserver<Chat.Response>() {
            @Override
            public void onNext(Chat.Response response) {
                System.out.println("----------------------------");
                System.out.println("leave " + channelName + " status : " + response.getType());
                System.out.println("----------------------------");
            }

            @Override
            public void onError(Throwable throwable) {

            }

            @Override
            public void onCompleted() {

            }
        });
        leaving.onNext(channel);
        leaving.onCompleted();
    }

    private void sendMessage (ChatServicesGrpc.ChatServicesStub servicesStub, String message){
        StreamObserver<Chat.Message> sending = servicesStub.sendMessage(new StreamObserver<Chat.Response>() {
            @Override
            public void onNext(Chat.Response response) {
                System.out.println("----------------------------");
                System.out.println("message sent status : " + response.getType());
                System.out.println("----------------------------");
            }

            @Override
            public void onError(Throwable throwable) {

            }

            @Override
            public void onCompleted() {

            }
        });

        Chat.Message messageToSend = Chat.Message.newBuilder()
                .setFrom(client)
                .setChannel(channel)
                .setText(message)
                .build();
        sending.onNext(messageToSend);
        sending.onCompleted();
    }

    private void listClients (ChatServicesGrpc.ChatServicesStub servicesStub, String channelName){
        if(!channel.getChanelName().equals(channelName)){
            System.out.println("wrong channel, the channel you've joined is " + channel.getChanelName());
            return;
        }
        StreamObserver<Chat.Channel> listing = servicesStub.listClient(new StreamObserver<Chat.Response>() {
            @Override
            public void onNext(Chat.Response response) {
                System.out.println(response.getType());
                System.out.println("----------------------------");
                System.out.println(String.format("the clients list in channel %s : \n%s", channelName, response.getMessage()));
                System.out.println("----------------------------");
            }

            @Override
            public void onError(Throwable throwable) {

            }

            @Override
            public void onCompleted() {

            }
        });
        listing.onNext(channel);
        listing.onCompleted();
    }

    private void disconnect (ChatServicesGrpc.ChatServicesStub servicesStub, String clientName){
        if(!client.getName().equals(clientName)){
            System.out.println("wrong channel, the channel you've joined is " + client.getName());
            return;
        }
        StreamObserver<Chat.Client> disconnecting = servicesStub.disconnect(new StreamObserver<Chat.Response>() {
            @Override
            public void onNext(Chat.Response response) {
                System.out.println("----------------------------");
                System.out.println("disconect " + clientName + " status : " + response.getType());
                System.out.println("----------------------------");
            }

            @Override
            public void onError(Throwable throwable) {

            }

            @Override
            public void onCompleted() {

            }
        });
        disconnecting.onNext(client);
        disconnecting.onCompleted();
    }

}