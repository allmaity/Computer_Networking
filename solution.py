from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #######if recv[:3] != '220':
        #######print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #######print(recv1)
    #######if recv1[:3] != '250':
        #######print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start

    mailFrom = "MAIL FROM: <senderEmail@gmail.com> \r\n" # tells user who sent the mail
    clientSocket.send(mailFrom.encode()) #encodes the data
    recvMAILFROM = clientSocket.recv(1024) # recieves data in 1024 byte-sized packets

    #######print("MAIL RECIEVED!")

    #######if recvMAILFROM[:3] != '250': # checks return code to see if things ran well
       ####### print('250 reply not received from server.') 

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start

    rcptTo = "RCPT TO: <recieverEmail@gmail.com> \r\n"
    clientSocket.send(rcptTo)
    recvRCPTTO=clientSocket.recv(1024)

    #######print("mail sent!")
    
    #######if recvRCPTTO[:3] != '250': # checks return code to see if things ran well
        #######print('250 reply not received from server.')

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start

    data = " DATA command\r\n"
    clientSocket.send(data.encode())
    recvDATA = clientSocket.recv(1024)
    
    #######if recvDATA[:3] != '250': # checks return code to see if things ran well
        #######print('250 reply not received from server.')

    # Fill in end

    # Send message data.
    # Fill in start

    messageToSend = input("Enter your message here: ")
        
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    messageWithEndPeriod = messageToSend+'.\r\n' #adds period at ennd of message to send
    clientSocket.send(messageWithEndPeriod.encode())
    recvMessage = clientSocket.recv(1024)

    #######if recvMessage[:3] != '250': # checks return code to see if things ran well
        #######print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start

    toQuit = "QUIT\r\n"
    clientSocket.send(toQuit.encode())

    quitMessage = clientSocket.recv(1024)
    #######if quitMessage[:3] != '250': # checks return code to see if things ran well
        #######print('250 reply not received from server.')
    
    clientSocket.close()


    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
