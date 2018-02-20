import socket
#create client socket
socket = socket.socket(socket. AF_INET , socket. SOCK_DGRAM )
#initialize and empty list to hold the message (an array of strings)
message = []
#ask user for the operation they want to perform
operation = input (
"""
CPT 411 Net-Centric Assignment server side/mathserver coded by Agbo Gabriel Endeurance 
Please select your operation:
1 - Addition of integers  2 - Subtraction of integers     3 - Multiplication of integers
4 - Division of integers    5 - Modulus of integers
>_
"""
)
#add operation to message
message.append( str (operation))
#ask user for the two values on which the operation is performed
first_variable = input ( 'enter the first value: >_ ' )
second_variable = input ('enter the second value: >_ ' )
#add the values to the message
message.append( str (first_variable))
message.append( str (second_variable))
#format message into [operation,first_varible,second_variable]
message = ',' .join(message)
#send message to client-side
socket.sendto(message, ( '127.0.0.1' , 42225))
#receive result from server
server_result, server_address = socket.recvfrom( 1024 *3 )
print ( 'server result: ' + server_result)
#close connection between client and server
socket.close() ;



