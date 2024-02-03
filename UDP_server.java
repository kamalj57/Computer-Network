import java.io.*;
import java.net.*;
import java.util.HashMap;
import java.util.Map;

public class udpserver {
   private static Map<String, Double> accountBalances = new HashMap<>(); 

    public static void main(String[] args) {
        final DatagramSocket serverSocket;

        try {
            serverSocket = new DatagramSocket(12345);
            System.out.println("Bank server is running...");

            while (true) {
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                serverSocket.receive(receivePacket);
                String clientRequest = new String(receivePacket.getData(), 0, receivePacket.getLength());

                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                System.out.println("Client Address: " + clientAddress + ", Client Port is: " + clientPort);

                 if (!accountBalances.containsKey(clientAddress.toString())) {
                    accountBalances.put(clientAddress.toString(), 1000.0); 
                }

                String response = processRequest(clientRequest, clientAddress.toString());
                byte[] sendData = response.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);
                serverSocket.send(sendPacket);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String processRequest(String request, String clientKey) {
        String[] parts = request.split(" ");

        String operation = parts[0].toLowerCase();
        double amount = 0.0;

        if (parts.length > 1) {
            try {
                amount = Double.parseDouble(parts[1]);
            } catch (NumberFormatException e) {
                return "Invalid amount";
            }
        }

        double accountBalance = accountBalances.get(clientKey);

        if (operation.equals("balance")) {
            return "Your balance is Rs." + accountBalance;
        } else if (operation.equals("withdraw")) {
            if (amount <= 0 || amount > accountBalance) {
                return "Invalid withdrawal amount";
            }
            accountBalance -= amount;
            accountBalances.put(clientKey, accountBalance);
            return "Withdrawn amount : Rs" + amount + ". And your new balance is Rs" + accountBalance;
        } else if (operation.equals("deposit")) {
            if (amount <= 0) {
                return "Invalid deposit amount";
            }
            accountBalance += amount;
            accountBalances.put(clientKey, accountBalance);
            return "Deposited amount is : Rs" + amount + ".  And your new balance is Rs" + accountBalance;
        } else {
            return "Invalid request";
        }
    }
}