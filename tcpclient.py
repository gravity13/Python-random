import socket;

target_host = "google.com"
taget_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,taget_port))

#send some data
client.send("GET / HTTP/1.1\r\nHost: google.ca\r\n\r\n")

#receive some data
response = client.recv(4096)

print response