import socket

# Assign the target host and port, in this case, port 80 for HTTP.
target_host = "www.google.com"
target_port = 80

# Create a socket object, specifying TCP connection, not UDP.
# AF_INET is the address family for IPv4, and SOCK_STREAM is the socket type for TCP.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the target host and port.
client.connect((target_host, target_port))

print("Sending data...\n")

# Send some data to the target host.
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive some data from the target host.

response = client.recv(4096)

# Write the response to a file.
# Separate the header from the body of the response.
# Write the header to output.txt and the body to HTMLResponseData.html.

with open ("output.txt", "w") as file:
    file.write(response.decode().split("<")[0])

with open("HTMLResponseData.html", "w") as file:
    file.write("<HTML" + response.decode().split("<HTML")[1])

print("Receiving data...\n")

# print(response.decode())
client.close()