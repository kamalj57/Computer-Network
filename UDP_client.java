import java.io.*;
import java.net.*;

public class udpclient {
    public static void main(String[] args) {
        DatagramSocket clientSocket = null;
        
        try {
            clientSocket = new DatagramSocket();
            InetAddress serverAddress = InetAddress.getByName("localhost");
            int serverPort = 12345;
            
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            
            while (true) {
                System.out.print("Enter a command ('balance', 'withdraw <amount>', 'deposit <amount>', 'exit'): ");
                String request = userInput.readLine();
                
                if (request.equalsIgnoreCase("exit")) {
                    break;
                }
                
                byte[] sendData = request.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, serverAddress, serverPort);
                clientSocket.send(sendPacket);
                
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                clientSocket.receive(receivePacket);
                
                String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Server response: " + response);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (clientSocket != null && !clientSocket.isClosed()) {
                clientSocket.close();
            }
        }
    }
}
